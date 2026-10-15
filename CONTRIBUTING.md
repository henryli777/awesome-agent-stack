# Contributing / 参与贡献

Propose a useful tool, correct a description, or refresh an existing snapshot.
Please explain the concrete workflow it helps; star count alone is not a reason
to include it. / 欢迎推荐工具、纠正文案或更新快照；请说明它解决的具体问题。

## Inclusion rules / 收录规则

- Working implementation in an official public GitHub repository, with a clear
  role in building, connecting, coding, observing, evaluating or securing agents.
- Explicit open-source license. When only part of a repository is open source,
  identify that exact component in the name/description and in `license_note` in
  both languages. Link to the pinned license as evidence. Source-available-only
  products and placeholder implementations are outside the initial scope.
- Official README and license evidence pinned to a 40-character commit SHA.
  Prefer a source-code evidence link too. Do not copy whole upstream README text;
  write a concise original summary and a use case.
- Initial curation excludes archived projects. An old push date alone does not
  prove abandonment; a recent date alone does not prove quality or maintenance.
- Disclose an affiliation. Maintainer-owned repositories must set
  `curator_project: true`; they are not placed ahead of others.

不收仅有宣传或占位代码的仓库。混合许可项目须写清收录的开源部分。收录不代表安装、
运行或安全审计结论，也不代表认可项目的所有行为或托管服务。

## Add or update an entry / 新增或更新条目

1. Edit **only `data/catalog.json`** for content. Categories have `id`, bilingual
   `label` and `description`. Projects use the following fields:

   | Field | Requirement |
   | --- | --- |
   | `id`, `name`, `repo`, `category` | Unique slug; readable name; canonical `owner/repository`; existing category ID |
   | `description`, `use_case` | Objects with concise original `en` and `zh` strings |
   | `tags` | Nonempty array of useful search terms |
   | `license` | Verified identifier for the included scope, e.g. `MIT` or `Apache-2.0`; documented MCP transition uses `Apache-2.0 / MIT` |
   | `license_evidence_url` | Official commit-pinned license file |
   | `license_note` | Bilingual scope note for exceptions, mixed licenses or manual SPDX confirmation |
   | `api_license` | Optional original GitHub SPDX result; `NOASSERTION` needs a manual evidence note |
   | `evidence_url` | Official commit-pinned README |
   | `source_evidence_url` | Optional official commit-pinned implementation file |
   | `stars`, `pushed_at`, `checked_at` | Integer stars, UTC last-push timestamp, verification date `YYYY-MM-DD` |
   | `metadata_refreshed_at`, `metadata_source` | Optional successful metadata observation time (UTC) and exact official `https://api.github.com/repos/OWNER/REPO` provenance |
   | `archived`, `curator_project` | Explicit booleans |
   | `website` | Optional official HTTPS documentation/product URL |

2. Read the official README and license at the referenced commit; inspect actual
   implementation paths. Get snapshot metadata from the official GitHub API.
   Update `checked_at` **only after doing that check**, and set top-level
   `updated_at` to the latest verification date. The generator is offline and
   does not verify upstream repositories or update dates for you.
3. Regenerate and verify with Python 3.10+ and Node.js 22+:

   ```sh
   python3 scripts/catalog.py
   python3 scripts/catalog.py --check
   python3 -m unittest discover -s tests -p 'test_*.py' -v
   node --test tests/*.test.mjs
   python3 -m http.server 8000 --directory site
   ```

4. Open `http://localhost:8000`. Check Chinese/English copy, search and license
   scope. Submit the source and generated READMEs/site JSON together in your PR.
   CI rejects stale generated files. No npm install is needed.

Stars and timestamps are recorded snapshots. Refreshing metadata does not
establish runtime compatibility or security; describe any runtime checks
separately with the exact environment and result. / 更新元数据不等于验证运行效果。

## Daily metadata refresh / 每日元数据刷新

The Pages workflow runs daily at 01:23 UTC (09:23 Asia/Shanghai), and can be run
manually on `main`. GitHub schedules may start late. It reads only the listed
public repositories from the official REST API, then refreshes stars, push time,
archive and fork status. It never changes descriptions, license scope, evidence
links, `checked_at` or the human-curation `updated_at`. Archived entries remain
visible with a status label. API license detection is not a license review.

Run `python3 scripts/refresh_metadata.py` before generation to perform the same
refresh locally. Optional `GITHUB_TOKEN` is read from the environment and never
printed or stored; the workflow uses its built-in token. The client makes at
most one request per listed repository (100 repositories maximum), waits one
second between requests, times out requests, and stops on rate or network
failure. It refuses redirects and non-public/mismatched repository responses.
Keep TLS certificate verification enabled. Some macOS Python installations
need their certificate bundle configured before local API calls work.

`metadata_refresh` records the observed `complete`, `partial` or `failed` result,
the attempt time, failed repository names and the most recent complete refresh
when available. Failed entries retain their last successful fields and dates.
Identical observations on the same UTC day do not create timestamp-only churn;
the next day's successful observation advances freshness. Generated README and
site data carry the same provenance and dates.

The scheduled run validates before committing with the GitHub Actions bot and
publishes its exact verified artifact. The built-in token prevents recursive
push-triggered runs. SHA checks and a normal non-force push reject concurrent
`main` updates; deployment checks again after environment approval. The workflow
needs repository contents write permission for its trusted refresh job, Pages
deployment enabled, and branch rules that allow the bot's update. It does not
bypass branch protections. PR verification keeps read-only contents access.

Public pages check their own published JSON every 60 seconds while visible and
on foreground return. They preserve the current language, filters, focus and
loaded data when refresh fails; browsers never call upstream GitHub APIs.

## Website changes / 页面修改

The static site has no build step or third-party assets. Keep DOM creation safe,
retain keyboard labels/focus visibility, and use relative paths for Pages
subdirectories. Shared filtering/state helpers live in `site/catalog-core.mjs`;
meaningful behavior tests use Node's built-in runner. Python generator tests use
`unittest`. Do not add dependencies merely to change styling.

Directory code and original summaries are MIT licensed. Linked projects retain
their own licenses; this directory does not relicense upstream code.
