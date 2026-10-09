# Validation record

Initial catalog snapshot: **2026-10-09**, 34 entries across six categories.
Official repository metadata, pinned README, implementation paths and licenses
were checked for curation. This verifies the entry's basis, not runtime behavior
or the security of the listed tools.

## Automated checks

Local verification used Python 3.14.6 and Node.js 24.8.0:

- 16 Python `unittest` cases passed: identity/category/type/date/source validation,
  scoped license notes, Markdown escaping, dot-segment URLs, deterministic outputs
  and read-only stale-output checking.
- 15 Node built-in tests passed: bilingual/Unicode search, combined filters,
  category counts, deterministic sorting, URL state and safe links.
- `python3 scripts/catalog.py --check` confirmed 34 entries and all three
  generated artifacts match the content source.
- `node --check site/app.js` passed.

CI repeats these checks on Ubuntu with Python 3.13 and Node.js 22 before Pages
publication. Browser checks below are manual Playwright CLI checks, not part of CI.

## Browser checks

Chromium checks at 1440 × 1100 and 390 × 844 confirmed:

- All 34 projects, six categories, verified source links and two curator labels.
- English display with mixed Chinese/English search (`智能体 python`), six results.
- Combined framework/Python/MIT/star sorting, five results, restored unchanged
  after reload via the shared URL.
- Empty results and reset; mobile security filter, five results, narrowed to one
  curator project by `evidence`; no mobile horizontal overflow.
- Simulated HTTP 503 for the catalog: visible failure/retry state, language change
  preserved `license=MIT`, and successful retry restored the filter and search focus.
- Keyboard reset retains focus in the search field.

Independent review reproduced dot-segment link acceptance, failed-load license
state loss and focus loss. The first was fixed with a failing then passing Python
regression. Both browser issues were reproduced before the changes, and the same
Playwright scenario passed afterward. The global single-character `/` shortcut
was removed to avoid unexpected focus changes for speech-input users.

Screenshots are visual evidence of the directory UI, not execution evidence for
the third-party tools. See [preview.png](preview.png).
