import copy
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog", ROOT / "scripts/catalog.py")
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def fixture():
    return {
        "schema_version": 1,
        "title": {"en": "Awesome Agent Stack", "zh": "Agent 开源工具精选"},
        "repo_url": "https://github.com/henryli777/awesome-agent-stack",
        "updated_at": "2026-10-09",
        "categories": [{"id": "mcp", "label": {"en": "MCP", "zh": "MCP 工具"},
                        "description": {"en": "Connect tools", "zh": "连接工具"}}],
        "projects": [{"id": "sample", "name": "Sample", "repo": "team/sample", "category": "mcp",
                      "description": {"en": "Tools", "zh": "工具"},
                      "use_case": {"en": "Build agents", "zh": "构建智能体"}, "tags": ["python"],
                      "license": "MIT", "stars": 10, "pushed_at": "2026-10-08T12:00:00Z",
                      "checked_at": "2026-10-09", "evidence_url": "https://github.com/team/sample/blob/" + "a" * 40 + "/README.md",
                      "license_evidence_url": "https://github.com/team/sample/blob/" + "a" * 40 + "/LICENSE",
                      "archived": False, "curator_project": False}],
    }


class CatalogTests(unittest.TestCase):
    def assertInvalid(self, data, text):
        self.assertIn(text, "\n".join(catalog.validate_catalog(data)))

    def test_valid_catalog(self):
        self.assertEqual(catalog.validate_catalog(fixture()), [])

    def test_duplicate_identity_case_insensitive_repo(self):
        data = fixture()
        other = copy.deepcopy(data["projects"][0])
        other["repo"] = "Team/Sample"
        data["projects"].append(other)
        self.assertInvalid(data, "duplicate id")
        self.assertInvalid(data, "duplicate repo")

    def test_unknown_category(self):
        data = fixture()
        data["projects"][0]["category"] = "other"
        self.assertInvalid(data, "unknown category")

    def test_rejects_unsafe_and_credential_urls(self):
        for field in ["evidence_url", "license_evidence_url", "website"]:
            for url in ["javascript:alert(1)", "http://github.com/team/sample", "https://secret@github.com/team/sample", "https://github.com\\@evil.test/path"]:
                data = fixture()
                data["projects"][0][field] = url
                self.assertInvalid(data, field)

    def test_sources_must_point_to_project(self):
        data = fixture()
        data["projects"][0]["evidence_url"] = "https://github.com/other/project/blob/main/README.md"
        self.assertInvalid(data, "evidence_url")

    def test_repository_and_evidence_paths_reject_dot_segments(self):
        for repo in ["team/.", "team/.."]:
            data = fixture()
            data["projects"][0]["repo"] = repo
            self.assertInvalid(data, "invalid repo")
        for path in ["../LICENSE", "docs/../../LICENSE", "%2e%2e/LICENSE", "docs/%2f../LICENSE"]:
            data = fixture()
            data["projects"][0]["evidence_url"] = "https://github.com/team/sample/blob/" + "a" * 40 + "/" + path
            self.assertInvalid(data, "evidence_url")

    def test_source_and_license_evidence_required(self):
        for field in ["evidence_url", "license_evidence_url"]:
            data = fixture()
            del data["projects"][0][field]
            self.assertInvalid(data, field)

    def test_unknown_license_and_scoped_licenses_need_note(self):
        for license_name in ["unknown", "NOASSERTION", "Apache-2.0 / MIT", "MIT (SDK only)"]:
            data = fixture()
            data["projects"][0]["license"] = license_name
            self.assertInvalid(data, "license")

    def test_mixed_oss_license_with_scope_note(self):
        data = fixture()
        data["projects"][0].update(license="Apache-2.0 / MIT", license_note={"en": "Code transition; docs CC-BY-4.0", "zh": "代码许可过渡；文档为 CC-BY-4.0"})
        self.assertEqual(catalog.validate_catalog(data), [])

    def test_bad_dates_and_future_snapshot_rejected(self):
        for field, value in [("checked_at", "2026-02-30"), ("checked_at", "2026-10-10"), ("pushed_at", "tomorrow"), ("pushed_at", "2026-10-10T01:00:00Z")]:
            data = fixture()
            data["projects"][0][field] = value
            self.assertInvalid(data, field)

    def test_types_and_bilingual_content_are_checked(self):
        for field, value in [("stars", True), ("stars", -1), ("tags", "python"), ("archived", "false"), ("description", {"en": "Only English"})]:
            data = fixture()
            data["projects"][0][field] = value
            self.assertInvalid(data, field)

    def test_container_values_report_validation_errors(self):
        for field in ["category", "license"]:
            for value in [[], {}]:
                data = fixture()
                data["projects"][0][field] = value
                self.assertInvalid(data, field)

    def test_evidence_urls_cannot_inject_markdown_links(self):
        data = fixture()
        data["projects"][0]["evidence_url"] += ")[Injected](https://evil.test)"
        rendered = catalog.render_readme(data, "en")
        self.assertNotIn(")[Injected](https://evil.test)", rendered)
        self.assertIn("%29%5BInjected%5D%28", rendered)

    def test_markdown_content_is_escaped_and_bilingual(self):
        data = fixture()
        data["projects"][0]["description"]["en"] = "Tools | <script>alert(1)</script> [link] *bold*\nnew"
        en = catalog.render_readme(data, "en")
        zh = catalog.render_readme(data, "zh")
        self.assertNotIn("<script>", en)
        self.assertIn("\\|", en)
        self.assertIn("\\[link\\]", en)
        self.assertIn("工具", zh)
        self.assertIn("https://github.com/team/sample", en)

    def test_single_source_generates_both_readmes_and_identical_site_data(self):
        data = fixture()
        outputs = catalog.generated_files(data)
        self.assertEqual(set(outputs), {"README.md", "README.zh-CN.md", "site/catalog.json"})
        self.assertEqual(json.loads(outputs["site/catalog.json"]), data)
        self.assertEqual(outputs, catalog.generated_files(data))

    def test_check_detects_stale_generated_files_without_rewriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "data").mkdir()
            (root / "data/catalog.json").write_text(json.dumps(fixture()), encoding="utf-8")
            command = [sys.executable, str(ROOT / "scripts/catalog.py"), "--root", tmp]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            readme = root / "README.md"
            readme.write_text("stale", encoding="utf-8")
            result = subprocess.run(command + ["--check"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("README.md", result.stderr)
            self.assertEqual(readme.read_text(), "stale")


if __name__ == "__main__":
    unittest.main()
