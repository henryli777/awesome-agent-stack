# Awesome Agent Stack Implementation Plan

> **For agentic workers:** Use native implementation and delegated frontend/research work. Track verified results below.

**Goal:** Publish a verified bilingual Awesome collection and usable GitHub Pages directory.

**Architecture:** One JSON content source generates Markdown and browser data. A buildless static frontend filters and displays it. CI checks consistency and deploys Pages.

**Tech Stack:** Python 3.10+ standard library, Node.js 22+ built-in test runner, HTML/CSS/JavaScript, GitHub Actions.

**Spec:** `docs/design.md`

## Global Constraints

- No private workspace content or credentials in the public repository.
- No external runtime dependencies or automated network calls on page load except same-origin catalog fetch.
- Source and license evidence must be official HTTPS URLs; license scope must be explicit.
- Timestamps and stars are verification snapshots; curator projects must be marked.

## Review Focus

- Pages subpaths resolve relative assets and catalog fetches.
- Untrusted catalog strings cannot execute as HTML or unsafe links.
- Chinese/English search works independently of display language.
- Mixed/open-core license scope is clear in cards and both READMEs.
- Invalid query parameters and empty/error states remain usable.

### Task 1: Catalog and deterministic outputs

**Files:** `data/catalog.json`, `scripts/catalog.py`, `tests/test_catalog.py`, generated READMEs and `site/catalog.json`.

**Interfaces:** `validate_catalog(dict) -> list[str]`; `render_readme(dict, lang) -> str`; `generated_files(dict) -> dict[str, str]`; CLI `python3 scripts/catalog.py [--check]`.

- [x] Write tests for duplicate identities, invalid categories/dates/URLs, license evidence, escaping and stale output detection; run them and verify failure before implementation.
- [x] Implement validation and deterministic generation; merge independently verified entries and two marked curator projects.
- [x] Run `python3 -m unittest discover -s tests -p 'test_*.py' -v` and `python3 scripts/catalog.py --check`.

### Task 2: Searchable static directory

**Files:** `site/index.html`, `site/style.css`, `site/app.js`, `site/catalog-core.mjs`, `tests/catalog-core.test.mjs`.

**Interfaces:** Frontend consumes source schema categories/projects, localized `description`, `use_case` and `license_note`, plus verified repository metadata.

- [x] Delegate implementation and meaningful Node tests to frontend agent.
- [x] Run `node --test tests/*.test.mjs`.
- [x] Use Playwright to check desktop/mobile, search, combined filters, language, empty state and URL restoration.

### Task 3: Contribution and publication

**Files:** `CONTRIBUTING.md`, `LICENSE`, `.gitignore`, `.github/ISSUE_TEMPLATE/submit-project.yml`, `.github/workflows/pages.yml`.

- [x] Document adding/updating entries, license scope and snapshot limitations.
- [x] Run complete checks and independent code/content review; address material findings.
- [ ] Create the authorized public repository, push and enable Pages; confirm Actions success and deployed site behavior.

## Verification record

Local verification: 16 Python and 15 Node tests passed; generated artifacts checked; desktop/mobile and error-recovery browser assertions passed. Independent review findings were reproduced and fixed. See `docs/VALIDATION.md`. Publication remains to be confirmed.
