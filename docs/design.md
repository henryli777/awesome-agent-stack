# Awesome Agent Stack

Build a bilingual, curated directory for people choosing tools to build, operate,
evaluate and secure AI agents. Each entry explains what it does and when to use it,
links to official sources, and records a verification date. The catalog is a
selection aid, not a claim that a project has been security-audited.

## Scope

- Six categories: frameworks, MCP, coding and skills, observability, evaluation,
  and security.
- Initial entries are verified against official repository metadata, README and
  licenses. Prefer working implementations over placeholders and list explicit
  open-source components when a repository also has other license scopes.
- The maintainer's own projects are visibly marked as curator projects.
- Stars and last-push timestamps are dated snapshots, not live values or a quality
  ranking. Default sorting is alphabetical.
- English and Chinese copy, text search, category/license filters, sorting and
  shareable URL state. Responsive layout and keyboard-accessible controls.

## Architecture

`data/catalog.json` is the content source. A Python standard-library validator and
generator produce `README.md`, `README.zh-CN.md` and `site/catalog.json` without a
network call. The website uses native JavaScript modules and CSS, without runtime
dependencies, analytics, third-party fonts or a server. GitHub Actions verifies
content and tests, then publishes the static `site/` directory to GitHub Pages.

## Acceptance

Invalid/duplicate repositories, missing sources, unsafe URLs, invalid dates and
stale generated artifacts fail validation. Markdown output safely handles content
characters. Browser checks cover desktop/mobile, bilingual search, combined
filters, empty results and URL restoration. Contributors can propose an entry
with official evidence and regenerate all outputs in one documented command.
