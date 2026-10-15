export const DEFAULT_STATE = Object.freeze({ q: '', category: 'all', license: 'all', sort: 'az', lang: 'zh' });
const allowedSorts = ['az', 'stars', 'updated'];
const nameOrder = new Intl.Collator('en', { sensitivity: 'base', numeric: true });

export function normalizeSearch(value) {
  return typeof value === 'string' ? value.normalize('NFKC').toLocaleLowerCase('en').trim().replace(/\s+/gu, ' ') : '';
}

export function localizedText(value, lang) {
  if (typeof value === 'string') return value;
  if (!value || typeof value !== 'object') return '';
  const candidates = [value[lang], value.en, value.zh];
  return candidates.find(candidate => typeof candidate === 'string' && candidate.length > 0) || '';
}

export function filterProjects(projects, state = {}) {
  const terms = normalizeSearch(state.q).split(' ').filter(Boolean);
  return projects.filter(project => {
    if (state.category && state.category !== 'all' && project.category !== state.category) return false;
    if (state.license && state.license !== 'all' && project.license !== state.license) return false;
    const text = normalizeSearch([
      project.name, project.repo, project.description?.en, project.description?.zh,
      project.use_case?.en, project.use_case?.zh, ...(Array.isArray(project.tags) ? project.tags : []),
    ].filter(value => typeof value === 'string').join(' '));
    return terms.every(term => text.includes(term));
  });
}

export function sortProjects(projects, sort = 'az') {
  const alphabetically = (a, b) => nameOrder.compare(a.name || '', b.name || '') || nameOrder.compare(a.id || '', b.id || '');
  const timestamp = value => Number.isFinite(Date.parse(value)) ? Date.parse(value) : -Infinity;
  return [...projects].sort((a, b) => {
    if (sort === 'stars') return (Number(b.stars) || 0) - (Number(a.stars) || 0) || alphabetically(a, b);
    if (sort === 'updated') {
      const left = timestamp(a.pushed_at);
      const right = timestamp(b.pushed_at);
      return (left === right ? 0 : right > left ? 1 : -1) || alphabetically(a, b);
    }
    return alphabetically(a, b);
  });
}

export function categoryCounts(projects, state, categories) {
  const matching = filterProjects(projects, { ...state, category: 'all' });
  const result = Object.fromEntries(['all', ...categories].map(category => [category, 0]));
  result.all = matching.length;
  for (const project of matching) if (Object.hasOwn(result, project.category)) result[project.category] += 1;
  return result;
}

export function parseState(search, { categories = [], licenses = [] } = {}) {
  const params = new URLSearchParams(search);
  const category = params.get('category');
  const license = params.get('license');
  const sort = params.get('sort');
  return {
    q: (params.get('q') || '').trim().slice(0, 300),
    category: categories.includes(category) ? category : 'all',
    license: licenses.includes(license) ? license : 'all',
    sort: allowedSorts.includes(sort) ? sort : 'az',
    lang: params.get('lang') === 'en' ? 'en' : 'zh',
  };
}

export function serializeState(state) {
  const params = new URLSearchParams();
  for (const key of ['q', 'category', 'license', 'sort', 'lang']) {
    if (state[key] && state[key] !== DEFAULT_STATE[key]) params.set(key, state[key]);
  }
  return params.toString();
}

export function safeHttpsUrl(value) {
  if (typeof value !== 'string' || !value.startsWith('https://')) return null;
  try {
    const url = new URL(value);
    return url.protocol === 'https:' && !url.username && !url.password ? url.href : null;
  } catch {
    return null;
  }
}

export function createCatalogRefresh({ fetchImpl = globalThis.fetch, onCatalog, onFailure, timeoutMs = 15000 }) {
  let pending = null;
  let fingerprint = null;
  return function refresh() {
    if (pending) return pending;
    pending = (async () => {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), timeoutMs);
      try {
        const response = await fetchImpl('./catalog.json', { cache: 'no-cache', signal: controller.signal });
        if (!response.ok) throw new Error('Catalogue unavailable');
        const value = await response.json();
        if (value?.schema_version !== 1 || !Array.isArray(value.projects) || !value.projects.length ||
          !Array.isArray(value.categories) || !value.categories.length ||
          value.categories.some(category => !category || typeof category.id !== 'string') ||
          value.projects.some(project => !project || typeof project.name !== 'string' || typeof project.repo !== 'string' ||
            typeof project.category !== 'string' || typeof project.license !== 'string')) {
          throw new Error('Invalid catalogue');
        }
        const next = JSON.stringify(value);
        if (next !== fingerprint) {
          onCatalog(value);
          fingerprint = next;
        }
        return true;
      } catch {
        onFailure();
        return false;
      } finally {
        clearTimeout(timer);
      }
    })().finally(() => { pending = null; });
    return pending;
  };
}

export function startForegroundRefresh({ refresh, document = globalThis.document,
  window = globalThis.window, setIntervalImpl = globalThis.setInterval }) {
  const foreground = () => { if (document.visibilityState === 'visible') refresh(); };
  document.addEventListener('visibilitychange', foreground);
  window.addEventListener('focus', foreground);
  setIntervalImpl(foreground, 60000);
}

export function metadataSummary(data, lang) {
  const zh = lang === 'zh';
  const report = data?.metadata_refresh;
  if (!report) return zh ? 'GitHub 元数据尚未自动刷新；当前为人工核验时的快照。' : 'GitHub metadata has not yet been refreshed automatically; values are the original checked snapshot.';
  const format = value => typeof value === 'string' ? value.replace('T', ' ').replace('Z', ' UTC') : (zh ? '尚无' : 'none yet');
  const count = report.failed_repos?.length || 0;
  if (report.status === 'complete') return zh
    ? `GitHub 官方元数据已刷新：${format(report.last_complete_at)}。README 与许可的人工核验日期独立记录。`
    : `Official GitHub metadata refreshed: ${format(report.last_complete_at)}. Human checks of README and license evidence have separate dates.`;
  return zh ? `GitHub 元数据${report.status === 'partial' ? '部分刷新' : '刷新失败'}：${format(report.attempted_at)}；${count} 个项目保留上次成功快照。最近完整刷新：${format(report.last_complete_at)}。`
    : `GitHub metadata refresh ${report.status === 'partial' ? 'partial' : 'failed'}: ${format(report.attempted_at)}; last successful values preserved for ${count} projects. Last complete refresh: ${format(report.last_complete_at)}.`;
}
