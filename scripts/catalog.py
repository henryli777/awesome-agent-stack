#!/usr/bin/env python3
"""Validate the content source and deterministically generate public artifacts.

No network calls. Official sources are verified by contributors before submission.
"""
import argparse
import datetime as dt
import html
import json
import pathlib
import re
import sys
from urllib.parse import quote, unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
SIMPLE_LICENSES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-3.0"}
MIXED_LICENSES = {"Apache-2.0 / MIT"}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REPO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+$")


def bilingual(value):
    return isinstance(value, dict) and all(isinstance(value.get(lang), str) and value[lang].strip() for lang in ("en", "zh"))


def https_url(value):
    if not isinstance(value, str) or not value.startswith("https://"):
        return False
    if "\\" in value or any(ord(char) <= 32 for char in value):
        return False
    try:
        url = urlsplit(value)
        return bool(url.hostname) and url.scheme == "https" and not url.username and not url.password and url.port in (None, 443)
    except ValueError:
        return False


def official_evidence(value, repo):
    if not https_url(value) or not isinstance(repo, str):
        return False
    url = urlsplit(value)
    decoded_path = unquote(url.path)
    if "\\" in decoded_path or any(segment in {".", ".."} for segment in decoded_path.split("/")):
        return False
    # Pinned source links prevent a later branch change silently altering evidence.
    prefix = "/" + repo.lower() + "/blob/"
    path = url.path.lower()
    if url.hostname != "github.com" or not path.startswith(prefix):
        return False
    remaining = path[len(prefix):]
    return bool(re.fullmatch(r"[0-9a-f]{40}/[^?#]+", remaining)) and not url.query and not url.fragment


def date_value(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def timestamp_value(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value):
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def validate_catalog(data):
    errors = []
    if not isinstance(data, dict):
        return ["catalog must be an object"]
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        errors.append("schema_version must be 1")
    if not bilingual(data.get("title")):
        errors.append("title must contain en and zh text")
    if not https_url(data.get("repo_url")):
        errors.append("repo_url must be a safe HTTPS URL")
    updated = date_value(data.get("updated_at"))
    if updated is None:
        errors.append("updated_at must be a valid YYYY-MM-DD date")
    refresh_report = data.get("metadata_refresh")
    if refresh_report is not None:
        if (not isinstance(refresh_report, dict) or refresh_report.get("status") not in ("complete", "partial", "failed")
                or not timestamp_value(refresh_report.get("attempted_at"))
                or not isinstance(refresh_report.get("failed_repos"), list)
                or any(not isinstance(repo, str) or not REPO.fullmatch(repo) for repo in refresh_report.get("failed_repos", []))):
            errors.append("metadata_refresh must contain a valid status, attempted_at and failed_repos")
        elif "last_complete_at" in refresh_report and (not timestamp_value(refresh_report["last_complete_at"])
                or refresh_report["last_complete_at"] > refresh_report["attempted_at"]):
            errors.append("metadata_refresh.last_complete_at must be valid and no later than attempted_at")
    categories = data.get("categories")
    if not isinstance(categories, list) or not categories:
        errors.append("categories must be a nonempty array")
        categories = []
    category_ids = set()
    for i, category in enumerate(categories):
        at = f"categories[{i}]"
        if not isinstance(category, dict):
            errors.append(at + " must be an object")
            continue
        key = category.get("id")
        if not isinstance(key, str) or not SLUG.fullmatch(key) or key == "all":
            errors.append(at + " invalid id")
        elif key in category_ids:
            errors.append(at + " duplicate id")
        else:
            category_ids.add(key)
        for field in ("label", "description"):
            if not bilingual(category.get(field)):
                errors.append(f"{at}.{field} must contain en and zh text")
    projects = data.get("projects")
    if not isinstance(projects, list) or not projects:
        errors.append("projects must be a nonempty array")
        projects = []
    ids, repos = set(), set()
    for i, project in enumerate(projects):
        at = f"projects[{i}]"
        if not isinstance(project, dict):
            errors.append(at + " must be an object")
            continue
        key, repo = project.get("id"), project.get("repo")
        if not isinstance(key, str) or not SLUG.fullmatch(key):
            errors.append(at + " invalid id")
        elif key in ids:
            errors.append(at + " duplicate id")
        else:
            ids.add(key)
        if not isinstance(repo, str) or not REPO.fullmatch(repo) or repo.split("/")[-1] in {".", ".."}:
            errors.append(at + " invalid repo")
        elif repo.lower() in repos:
            errors.append(at + " duplicate repo")
        else:
            repos.add(repo.lower())
        if not isinstance(project.get("category"), str) or project["category"] not in category_ids:
            errors.append(at + " unknown category")
        if not isinstance(project.get("name"), str) or not project["name"].strip():
            errors.append(at + ".name must be nonempty text")
        for field in ("description", "use_case"):
            if not bilingual(project.get(field)):
                errors.append(f"{at}.{field} must contain en and zh text")
        tags = project.get("tags")
        if not isinstance(tags, list) or not tags or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            errors.append(at + ".tags must be a nonempty text array")
        if type(project.get("stars")) is not int or project["stars"] < 0:
            errors.append(at + ".stars must be a nonnegative integer")
        for field in ("archived", "curator_project"):
            if type(project.get(field)) is not bool:
                errors.append(f"{at}.{field} must be a boolean")
        refreshed = timestamp_value(project.get("metadata_refreshed_at"))
        source = f"https://api.github.com/repos/{repo}"
        has_metadata = "metadata_refreshed_at" in project or "metadata_source" in project
        if has_metadata and (refreshed is None or project.get("metadata_source") != source):
            errors.append(at + ".metadata_refreshed_at and metadata_source must identify official GitHub metadata")
        if "fork" in project and type(project["fork"]) is not bool:
            errors.append(at + ".fork must be a boolean")
        if project.get("archived") is True and not (refreshed and project.get("metadata_source") == source):
            errors.append(at + ".archived projects are outside the initial collection")
        checked = date_value(project.get("checked_at"))
        if checked is None or (updated and checked > updated):
            errors.append(at + ".checked_at must be valid and no later than updated_at")
        pushed = timestamp_value(project.get("pushed_at"))
        if pushed is None or (refreshed and pushed > refreshed) or (not refreshed and checked and pushed.date() > checked):
            errors.append(at + ".pushed_at must be UTC and no later than its metadata refresh or checked_at")
        for field in ("evidence_url", "license_evidence_url"):
            if not official_evidence(project.get(field), repo):
                errors.append(f"{at}.{field} must be a commit-pinned official repository link")
        if "source_evidence_url" in project and not official_evidence(project["source_evidence_url"], repo):
            errors.append(at + ".source_evidence_url must be a commit-pinned official repository link")
        if project.get("website") and not https_url(project["website"]):
            errors.append(at + ".website must be a safe HTTPS URL")
        license_name = project.get("license")
        if not isinstance(license_name, str) or license_name not in SIMPLE_LICENSES | MIXED_LICENSES:
            errors.append(at + ".license must identify the included open-source scope")
        if "license_note" in project and not bilingual(project["license_note"]):
            errors.append(at + ".license_note must contain en and zh text")
        if ((isinstance(license_name, str) and license_name in MIXED_LICENSES) or project.get("api_license") == "NOASSERTION") and not bilingual(project.get("license_note")):
            errors.append(at + ".license requires a bilingual scope/evidence note")
        is_curator = isinstance(repo, str) and repo.lower().startswith("henryli777/")
        if is_curator and project.get("curator_project") is not True:
            errors.append(at + ".curator_project must mark maintainer-owned repositories")
    if (isinstance(refresh_report, dict) and isinstance(refresh_report.get("failed_repos"), list)
            and all(isinstance(repo, str) for repo in refresh_report['failed_repos'])):
        failures = refresh_report['failed_repos']
        known_repos = {project.get('repo') for project in projects if isinstance(project, dict) and isinstance(project.get('repo'), str)}
        if len(set(failures)) != len(failures) or not set(failures) <= known_repos:
            errors.append('metadata_refresh.failed_repos must name unique listed repositories')
        expected = 'complete' if not failures else 'failed' if len(failures) == len(projects) else 'partial'
        if refresh_report.get('status') != expected:
            errors.append('metadata_refresh.status must match failed_repos')
        if expected == 'complete' and (not timestamp_value(refresh_report.get('last_complete_at'))
                or any(not isinstance(project, dict) or not timestamp_value(project.get('metadata_refreshed_at')) for project in projects)):
            errors.append('metadata_refresh complete requires successful per-project metadata and last_complete_at')
    return errors


def markdown(value):
    text = html.escape(str(value), quote=False).replace("\n", " ").replace("\r", " ")
    return re.sub(r"([\\`*_{}\[\]()|])", r"\\\1", text)


def render_readme(data, lang):
    zh = lang == "zh"
    title = "Awesome Agent Stack"
    switch = "[English](README.md)" if zh else "[简体中文](README.zh-CN.md)"
    url = "https://henryli777.github.io/awesome-agent-stack/"
    lines = [f"# {title}", "", switch + f" · [{'浏览导航站' if zh else 'Browse the directory'}]({url}) · [Contributing](CONTRIBUTING.md)", ""]
    lines += (["精选 AI Agent 开源工具：按用途查找框架、MCP、编码工具、观测、评测和安全项目。每项说明适用场景，并链接到核实版本的官方 README 和许可证。", ""] if zh else
              ["A curated collection of open-source tools to build, connect, code, observe, evaluate and secure AI agents. Each entry explains when to use it and links to a verified version of its official README and license.", ""])
    lines += ["![Directory preview](docs/preview.png)", ""]
    count = len(data["projects"])
    lines += [f"**{'收录' if zh else 'Catalog'}: {count} {'项' if zh else 'projects'} · {'人工证据核验日期' if zh else 'Human evidence snapshot'}: {data['updated_at']}**", ""]
    report = data.get('metadata_refresh')
    if report:
        status = {'complete': '完整成功', 'partial': '部分成功', 'failed': '失败'}[report['status']] if zh else report['status']
        lines += [f"**{'GitHub 元数据刷新' if zh else 'GitHub metadata refresh'}: {status} · {report['attempted_at']}** · "
                  + (f"{len(report['failed_repos'])} 项保留上次成功快照。" if zh else f"Last successful snapshots preserved for {len(report['failed_repos'])} projects."), '']
    lines += (["网页支持中英文、跨语言搜索、类别和许可证筛选、排序及可分享的筛选链接。默认按名称排列。", "", "## 如何选择", ""] if zh else
              ["The website supports bilingual copy, cross-language search, category/license filters, sorting and shareable filter URLs. Default order is alphabetical.", "", "## Choose by your next task", ""])
    for category in data["categories"]:
        lines.append(f"- [{markdown(category['label'][lang])}](#{category['id']}): {markdown(category['description'][lang])}")
    lines += ["", "## " + ("收录与核实规则" if zh else "Curation and verification"), ""]
    lines += (["- 收录有实际代码、明确开源许可和具体用途的项目；官方仓库、README、许可证是依据。", "- 部分仓库包含企业功能或托管服务；收录范围和许可备注会明确指出。开源 SDK 不等同于开源服务。", "- 星数、推送时间、归档和 Fork 状态按每日计划读取 GitHub 官方 API，独立记录元数据刷新时间；不自动重核 README、许可或用途。失败时保留上次成功快照。数据不能证明质量、当前维护状态或安全性，收录工具未逐一安装、运行或安全审计。", "- 标注「维护者项目」的条目由本目录维护者开发，与其他条目接受相同收录规则。", "- 初始排除归档项目、占位实现和仅采用非开源许可证的项目；后续归档会标记而不自动删除。欢迎提交带官方证据的 PR。", ""] if zh else
              ["- Include concrete implementations with an explicit open-source license and a useful role; official repositories, READMEs and licenses are the evidence.", "- Some repositories also contain enterprise features or hosted services. Scope notes identify what is included; an open-source SDK does not imply an open-source service.", "- Stars, push dates, archive and fork status are read from the official GitHub API on a daily schedule, with separate metadata refresh timestamps. This does not recheck README, license or use-case evidence. Failures preserve last successful snapshots. These values do not prove quality, maintenance or security; listed tools have not all been installed, executed or security-audited.", "- Entries marked **Curator project** are developed by this directory's maintainer and follow the same inclusion rules.", "- Initial curation excludes archived projects, placeholders and software offered only under non-open-source licenses. Later archive status is marked without automatically deleting entries. Evidence-backed PRs are welcome.", ""])
    for category in data["categories"]:
        lines += [f'<a id="{category["id"]}"></a>', "", f"## {markdown(category['label'][lang])}", ""]
        projects = sorted((p for p in data["projects"] if p["category"] == category["id"]), key=lambda p: (p["name"].casefold(), p["id"]))
        for project in projects:
            marker = (" · **维护者项目**" if zh else " · **Curator project**") if project["curator_project"] else ""
            lines += [f"### [{markdown(project['name'])}](https://github.com/{project['repo']}){marker}", "", markdown(project["description"][lang]), "",
                      f"- **{'适合' if zh else 'Use it for'}:** {markdown(project['use_case'][lang])}",
                      f"- **{'许可范围' if zh else 'License scope'}:** [{markdown(project['license'])}]({quote(project['license_evidence_url'], safe=':/%')})" + (" — " + markdown(project["license_note"][lang]) if project.get("license_note") else ""),
                      f"- **{'核实' if zh else 'Evidence'}:** [README]({quote(project['evidence_url'], safe=':/%')}) · {project['checked_at']} · {'标签' if zh else 'Tags'}: {', '.join(markdown(t) for t in project['tags'])}", ""]
            if project.get('metadata_refreshed_at'):
                lines += [f"- **{'元数据刷新' if zh else 'Metadata refreshed'}:** {project['metadata_refreshed_at']} · [GitHub API]({project['metadata_source']}) · Stars: {project['stars']} · {'代码推送' if zh else 'Code push'}: {project['pushed_at']} · {'归档' if zh else 'Archived'}: {str(project['archived']).lower()}", '']
    lines += ["## " + ("本地预览与维护" if zh else "Preview and maintain"), "", "Python 3.10+ · Node.js 22+ (tests only). No npm install required.", "", "```sh", "git clone https://github.com/henryli777/awesome-agent-stack.git", "cd awesome-agent-stack", "python3 scripts/catalog.py", "python3 scripts/catalog.py --check", "python3 -m unittest discover -s tests -p 'test_*.py' -v", "node --test tests/*.test.mjs", "python3 -m http.server 8000 --directory site", "```", "", "[Local preview](http://localhost:8000) · [Contribution guide](CONTRIBUTING.md) · [MIT license](LICENSE)", "", ("修改 `data/catalog.json` 后运行生成命令。核实日期由贡献者检查官方证据后填写；生成器不进行网络查询，也不会自动声称内容已重新核实。" if zh else "Edit `data/catalog.json`, then regenerate. Contributors set verification dates after checking official evidence; the generator makes no network calls and never claims it re-verified the content."), "", "<!-- Generated by scripts/catalog.py from data/catalog.json. Do not edit directly. -->", ""]
    return "\n".join(lines)


def generated_files(data):
    return {"README.md": render_readme(data, "en"), "README.zh-CN.md": render_readme(data, "zh"),
            "site/catalog.json": json.dumps(data, ensure_ascii=False, indent=2) + "\n"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail on invalid data or stale artifacts without writing")
    parser.add_argument("--root", type=pathlib.Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        data = json.loads((args.root / "data/catalog.json").read_text(encoding="utf-8"))
        errors = validate_catalog(data)
        if errors:
            raise ValueError("\n".join(errors))
        outputs = generated_files(data)
        stale = []
        for name, content in outputs.items():
            path = args.root / name
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    stale.append(name)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
        if stale:
            raise ValueError("Stale generated files: " + ", ".join(stale) + ". Run python3 scripts/catalog.py")
        print(f"{'Checked' if args.check else 'Generated'} {len(outputs)} artifacts; {len(data['projects'])} projects")
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
