#!/usr/bin/env python3
"""Refresh bounded public GitHub repository metadata, never curated evidence."""
import argparse
import copy
import datetime as dt
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

from catalog import ROOT, timestamp_value, validate_catalog

MAX_REPOS = 100
MAX_RESPONSE_BYTES = 2_000_000


def refresh(data, fetch, now):
    if not timestamp_value(now):
        raise ValueError('Refresh time must be a UTC timestamp')
    errors = validate_catalog(data)
    if errors:
        raise ValueError('Invalid input catalog: ' + '; '.join(errors))
    if len(data['projects']) > MAX_REPOS:
        raise ValueError('Catalog exceeds the bounded refresh limit')
    result = copy.deepcopy(data)
    failures = []
    for project in result['projects']:
        repo = project['repo']
        try:
            payload = fetch(repo)
            if (not isinstance(payload, dict) or payload.get('private') is not False
                    or not isinstance(payload.get('full_name'), str)
                    or payload['full_name'].lower() != repo.lower()
                    or type(payload.get('stargazers_count')) is not int
                    or payload['stargazers_count'] < 0
                    or type(payload.get('archived')) is not bool
                    or type(payload.get('fork')) is not bool):
                raise ValueError('Invalid public repository metadata')
            pushed = payload.get('pushed_at')
            if not timestamp_value(pushed) or pushed > now:
                raise ValueError('Invalid push timestamp')
            fields = dict(stars=payload['stargazers_count'], pushed_at=pushed,
                          archived=payload['archived'], fork=payload['fork'],
                          metadata_source=f'https://api.github.com/repos/{repo}')
            same_day = project.get('metadata_refreshed_at', '')[:10] == now[:10]
            unchanged = all(project.get(key) == value for key, value in fields.items())
            if not (same_day and unchanged):
                project.update(fields, metadata_refreshed_at=now)
        except (OSError, ValueError, TypeError, KeyError):
            # Do not persist exception messages: HTTP diagnostics can contain secrets.
            failures.append(repo)
    status = 'complete' if not failures else 'failed' if len(failures) == len(result['projects']) else 'partial'
    previous = data.get('metadata_refresh', {})
    report = dict(status=status, attempted_at=now, failed_repos=failures)
    last_complete = previous.get('last_complete_at')
    if status == 'complete':
        last_complete = now
    if last_complete:
        report['last_complete_at'] = last_complete
    # A rerun that observes identical results on the same UTC day need not create a commit.
    if (previous.get('attempted_at', '')[:10] == now[:10]
            and previous.get('status') == status and previous.get('failed_repos') == failures
            and result['projects'] == data['projects']):
        report = previous
    result['metadata_refresh'] = report
    errors = validate_catalog(result)
    if errors:
        raise ValueError('Invalid refreshed catalog: ' + '; '.join(errors))
    return result


class PublicGitHub:
    def __init__(self, token=None):
        self.token = token
        self.blocked = False
        self.stop_reason = None

    def __call__(self, repo):
        if self.blocked:
            raise OSError('API refresh stopped')
        headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28',
                   'User-Agent': 'awesome-agent-stack-metadata'}
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        request = urllib.request.Request(f'https://api.github.com/repos/{repo}', headers=headers)
        try:
            # Forbid redirects, including repository moves; never forward a token to another host.
            opener = urllib.request.build_opener(NoRedirect)
            with opener.open(request, timeout=15) as response:
                body = response.read(MAX_RESPONSE_BYTES + 1)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise ValueError('Oversized API response')
                value = json.loads(body)
                if response.headers.get('X-RateLimit-Remaining') == '0':
                    self.blocked = True
                    self.stop_reason = 'rate-limit'
                return value
        except urllib.error.HTTPError as exc:
            if exc.code in (401, 403, 429) or exc.code >= 500:
                self.blocked = True
                self.stop_reason = f'http-{exc.code}'
            raise OSError('Official API unavailable') from None
        except (urllib.error.URLError, TimeoutError):
            self.blocked = True
            self.stop_reason = 'network'
            raise OSError('Official API unavailable') from None
        finally:
            time.sleep(1)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=pathlib.Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    path = args.root / 'data/catalog.json'
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        client = PublicGitHub(os.environ.get('GITHUB_TOKEN'))
        result = refresh(data, client, now)
        if result != data:
            temporary = path.with_suffix('.json.tmp')
            temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            temporary.replace(path)
        report = result['metadata_refresh']
        print(f"Official metadata refresh: {report['status']}; {len(report['failed_repos'])} unavailable repositories")
        if client.stop_reason:
            print(f'Further API requests stopped: {client.stop_reason}')
        return 0
    except (OSError, ValueError, TypeError):
        print('Metadata refresh could not produce a valid catalog; original preserved.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
