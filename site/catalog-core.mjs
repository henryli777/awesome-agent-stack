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
