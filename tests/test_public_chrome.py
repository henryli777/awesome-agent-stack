from html.parser import HTMLParser
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SUPPORT_URL = "https://support.coinexo.top/"


class ChromeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.region = None
        self.link = None
        self.support_links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in {"header", "footer"}:
            self.region = tag
        if tag == "a" and attributes.get("href") == SUPPORT_URL:
            self.link = {"region": self.region, "attributes": attributes, "text": ""}

    def handle_data(self, data):
        if self.link is not None:
            self.link["text"] += data

    def handle_endtag(self, tag):
        if tag == "a" and self.link is not None:
            self.support_links.append(self.link)
            self.link = None
        if tag in {"header", "footer"}:
            self.region = None


class PublicChromeTests(unittest.TestCase):
    def assertSupportChrome(self, name):
        parser = ChromeParser()
        parser.feed((ROOT / "site" / name).read_text(encoding="utf-8"))
        self.assertEqual([link["region"] for link in parser.support_links], ["header", "footer"])
        for link in parser.support_links:
            self.assertIn("支持项目", link["text"])
            self.assertNotIn("hidden", link["attributes"])
            self.assertNotIn("data-i18n", link["attributes"])
            self.assertEqual(link["attributes"].get("target"), "_blank")
            self.assertIn("noopener", link["attributes"].get("rel", "").split())

    def test_catalog_has_static_support_links_outside_loading_and_error_states(self):
        self.assertSupportChrome("index.html")

    def test_missing_page_has_the_same_public_support_chrome(self):
        self.assertTrue((ROOT / "site" / "404.html").is_file(), "Public 404 page must exist")
        self.assertSupportChrome("404.html")


if __name__ == "__main__":
    unittest.main()
