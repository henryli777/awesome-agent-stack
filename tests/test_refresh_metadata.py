import copy
import importlib.util
import pathlib
import sys
import unittest
from unittest import mock
import urllib.error

from test_catalog import fixture, catalog

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))


class MetadataTests(unittest.TestCase):
    def updater(self):
        path = ROOT / 'scripts/refresh_metadata.py'
        self.assertTrue(path.exists(), 'Official metadata updater must exist')
        spec = importlib.util.spec_from_file_location('refresh_metadata', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def response(self, **changes):
        return dict(full_name='team/sample', private=False, stargazers_count=42,
                    pushed_at='2026-10-14T10:00:00Z', archived=False, fork=True, **changes)

    def test_refresh_changes_only_official_metadata_and_preserves_human_evidence(self):
        module = self.updater()
        source = fixture()
        result = module.refresh(source, lambda repo: self.response(), '2026-10-15T01:00:00Z')
        self.assertEqual(source, fixture())
        project = result['projects'][0]
        self.assertEqual(project['stars'], 42)
        self.assertTrue(project['fork'])
        self.assertEqual(project['pushed_at'], '2026-10-14T10:00:00Z')
        self.assertEqual(project['metadata_refreshed_at'], '2026-10-15T01:00:00Z')
        self.assertEqual(project['metadata_source'], 'https://api.github.com/repos/team/sample')
        for field in fixture()['projects'][0]:
            if field not in {'stars', 'pushed_at', 'archived', 'fork'}:
                self.assertEqual(project[field], fixture()['projects'][0][field])
        self.assertEqual(result['updated_at'], '2026-10-09')
        self.assertEqual(catalog.validate_catalog(result), [])

    def test_failure_keeps_last_success_and_reports_partial_refresh(self):
        module = self.updater()
        source = module.refresh(fixture(), lambda repo: self.response(), '2026-10-15T01:00:00Z')
        other = copy.deepcopy(source['projects'][0])
        other.update(id='other', repo='team/other')
        for field in ['metadata_source', 'evidence_url', 'license_evidence_url']:
            other[field] = other[field].replace('team/sample', 'team/other')
        source['projects'].append(other)
        def fetch(repo):
            if repo == 'team/sample':
                raise OSError('secret must not reach status')
            return {**self.response(), 'full_name': 'team/other'}
        result = module.refresh(source, fetch, '2026-10-16T01:00:00Z')
        self.assertEqual(result['projects'][0], source['projects'][0])
        self.assertEqual(result['metadata_refresh']['status'], 'partial')
        self.assertEqual(result['metadata_refresh']['failed_repos'], ['team/sample'])
        self.assertNotIn('secret', str(result))
        self.assertEqual(result['metadata_refresh']['last_complete_at'], '2026-10-15T01:00:00Z')

    def test_repeated_unchanged_refresh_same_day_has_no_artifact_churn(self):
        module = self.updater()
        first = module.refresh(fixture(), lambda repo: self.response(), '2026-10-15T01:00:00Z')
        again = module.refresh(first, lambda repo: self.response(), '2026-10-15T02:00:00Z')
        self.assertEqual(first, again)

    def test_private_moved_and_malformed_api_payloads_preserve_last_snapshot(self):
        module = self.updater()
        for change in [{'private': True}, {'full_name': 'elsewhere/repo'}, {'stargazers_count': True},
                       {'pushed_at': '2026-10-16T00:00:00Z'}, {'archived': 'false'}]:
            payload = {**self.response(), **change}
            result = module.refresh(fixture(), lambda repo: payload, '2026-10-15T01:00:00Z')
            self.assertEqual(result['projects'], fixture()['projects'])
            self.assertEqual(result['metadata_refresh']['status'], 'failed')

    def test_refreshed_archived_project_remains_visible_with_original_license_scope(self):
        module = self.updater()
        result = module.refresh(fixture(), lambda repo: {**self.response(), 'archived': True}, '2026-10-15T01:00:00Z')
        self.assertTrue(result['projects'][0]['archived'])
        self.assertEqual(catalog.validate_catalog(result), [])

    def test_unproven_refresh_dates_and_sources_do_not_relax_snapshot_validation(self):
        for source in ['https://evil.test/repos/team/sample', 'https://api.github.com/repos/other/repo']:
            data = fixture()
            data['projects'][0].update(metadata_refreshed_at='2026-10-15T01:00:00Z', metadata_source=source,
                                        pushed_at='2026-10-14T10:00:00Z')
            self.assertTrue(catalog.validate_catalog(data))

    def test_refresh_report_invalid_types_are_validation_errors(self):
        data = fixture()
        data['metadata_refresh'] = {'status': [], 'attempted_at': 'invalid', 'failed_repos': []}
        self.assertTrue(catalog.validate_catalog(data))

    def test_network_outage_stops_subsequent_requests_and_keeps_tokens_out_of_errors(self):
        module = self.updater()
        client = module.PublicGitHub('secret-value')
        with mock.patch.object(module.urllib.request, 'build_opener') as opener, mock.patch.object(module.time, 'sleep'):
            opener.return_value.open.side_effect = urllib.error.URLError('secret-value')
            with self.assertRaises(OSError):
                client('team/sample')
            with self.assertRaises(OSError):
                client('team/other')
            self.assertEqual(opener.return_value.open.call_count, 1)
            self.assertEqual(client.stop_reason, 'network')

    def test_refresh_limit_rejects_oversized_catalog_before_network_calls(self):
        module = self.updater()
        data = fixture()
        data['projects'] = [copy.deepcopy(data['projects'][0]) for _ in range(101)]
        for index, project in enumerate(data['projects']):
            project.update(id=f'sample-{index}', repo=f'team/sample-{index}')
            for field in ['evidence_url', 'license_evidence_url']:
                project[field] = project[field].replace('team/sample', project['repo'])
        def forbidden(repo):
            self.fail('An oversized catalog must not make API requests')
        with self.assertRaises(ValueError):
            module.refresh(data, forbidden, '2026-10-15T01:00:00Z')

    def test_readme_shows_metadata_refresh_separately_from_human_evidence(self):
        result = self.updater().refresh(fixture(), lambda repo: self.response(), '2026-10-15T01:00:00Z')
        for lang, label in [('en', 'Metadata refreshed'), ('zh', '元数据刷新')]:
            readme = catalog.render_readme(result, lang)
            self.assertIn(label, readme)
            self.assertIn('2026-10-15T01:00:00Z', readme)
            self.assertIn('2026-10-09', readme)
            self.assertIn('https://api.github.com/repos/team/sample', readme)

    def test_new_human_review_does_not_require_relabeling_older_metadata(self):
        result = self.updater().refresh(fixture(), lambda repo: self.response(), '2026-10-15T01:00:00Z')
        result['updated_at'] = '2026-10-20'
        result['projects'][0]['checked_at'] = '2026-10-20'
        self.assertEqual(catalog.validate_catalog(result), [])

    def test_refresh_report_cannot_claim_complete_with_failed_or_unobserved_repositories(self):
        data = fixture()
        data['metadata_refresh'] = {'status': 'complete', 'attempted_at': '2026-10-15T01:00:00Z',
                                    'failed_repos': []}
        self.assertTrue(catalog.validate_catalog(data))
        data = self.updater().refresh(fixture(), lambda repo: self.response(), '2026-10-15T01:00:00Z')
        data['metadata_refresh']['failed_repos'] = ['team/sample']
        self.assertTrue(catalog.validate_catalog(data))


if __name__ == '__main__':
    unittest.main()
