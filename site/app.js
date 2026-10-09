import {
  DEFAULT_STATE, parseState, serializeState, filterProjects, sortProjects,
  categoryCounts, safeHttpsUrl, localizedText,
} from './catalog-core.mjs';

const REPO_URL = 'https://github.com/henryli777/awesome-agent-stack';
const CATEGORY_IDS = ['frameworks', 'mcp', 'coding', 'observability', 'evaluation', 'security'];
const CATEGORY_ICONS = { all: '▦', frameworks: '◇', mcp: '⇄', coding: '⌘', observability: '◎', evaluation: '≋', security: '⛨' };
const copy = {
  zh: {
    skip: '跳到工具目录', navCatalog: '探索目录', navAbout: '关于收录',
    heroLine1: '从想法到可靠的', heroLine2: 'AI Agent。',
    heroDescription: '发现真正用得上的开源工具。从构建、连接到评估与安全，为你的下一步找到合适的积木。',
    heroCta: '找到你的工具', noteTitle: '好工具，值得被发现。',
    noteDescription: '少一点盲目试用，多一点场景判断。每个项目都有用途说明、许可证和可回溯的来源。',
    noteBottom: '开源 · 可检索 · 持续整理', statProjects: '个开源项目', statCategories: '个工具方向', statSnapshot: '目录快照',
    statsNote: '按场景整理，而非排名推荐。Star 与代码推送时间均为核验时的快照。',
    catalogTitle: '探索工具目录', categoriesTitle: '工具方向', sidebarNote: '从使用场景出发，找到适合自己的工具。',
    submit: '推荐一个项目', searchLabel: '搜索名称、用途、标签或仓库', searchPlaceholder: '搜索工具、用途或标签…',
    clearSearch: '清空搜索', licenseLabel: '许可证', allLicenses: '全部许可证', sortLabel: '排序',
    sortAz: '名称 A–Z', sortStars: 'Star 快照最多', sortUpdated: '最近代码推送', reset: '重置筛选',
    allProjects: '全部项目', allDescription: '构建、连接、观察与验证你的智能体工作流。',
    loading: '正在加载目录…', loadingDescription: '正在准备工具和来源信息。',
    errorTitle: '目录暂时未能加载', errorDescription: '请重新加载，或前往 GitHub 阅读完整目录。', errorCount: '暂不可用',
    retry: '重新加载', readmeFallback: '查看 GitHub 目录 ↗', emptyTitle: '没有找到匹配的项目',
    emptyDescription: '试试更短的关键词，或清空筛选后重新探索。中英文关键词都可以搜索。', emptyReset: '清空搜索与筛选',
    catalogFootnote: 'Star 为核验时的数量，可能与 GitHub 当前值不同。「本站项目」表示由目录维护者开发。',
    aboutTitle: '一起把这个目录变得更有用。',
    aboutDescription: '依据官方代码、README 和许可证，记录用途与核实快照。收录不代表运行验证或安全审计。发现好项目，或信息需要更新，都欢迎提交。',
    aboutCta: '参与整理', footerTagline: '为下一次构建，存一份好工具。', footerPrivacy: '无追踪 · 无广告', footerSource: '查看源码 ↗',
    results: (count, total) => `${count} / ${total} 个项目`, curated: '本站项目', archived: '已归档', fork: 'Fork 项目',
    useCase: '适合用来', starsSnapshot: 'Stars 快照', pushedSnapshot: '代码推送（快照）', checked: '核验',
    source: '来源 README ↗', licenseSource: '许可证来源 ↗', website: '官网 ↗', apiLicense: 'API 许可证',
    notProvided: '未提供', projectList: '开源项目列表', mainNav: '主导航', pageTitle: 'Awesome Agent Stack · 开源智能体工具目录',
  },
  en: {
    skip: 'Skip to catalogue', navCatalog: 'Explore tools', navAbout: 'About the list',
    heroLine1: 'Your next agent,', heroLine2: 'starts here.',
    heroDescription: 'Find open-source tools worth building with. From frameworks and connections to evaluation and security, choose the right blocks for your next step.',
    heroCta: 'Find your tools', noteTitle: 'Good tools deserve to be found.',
    noteDescription: 'Start with the use case. Every project includes a practical description, a license, and a source you can check.',
    noteBottom: 'Open source · Searchable · Curated', statProjects: 'open-source projects', statCategories: 'tool categories', statSnapshot: 'Catalogue snapshot',
    statsNote: 'Organized by use case, without ranking endorsements. Stars and code push dates are recorded snapshots.',
    catalogTitle: 'Explore the catalogue', categoriesTitle: 'TOOL CATEGORIES', sidebarNote: 'Start with what you need to do. Find the tools that fit.',
    submit: 'Suggest a project', searchLabel: 'Search names, use cases, tags, or repositories', searchPlaceholder: 'Search tools, use cases, or tags…',
    clearSearch: 'Clear search', licenseLabel: 'License', allLicenses: 'All licenses', sortLabel: 'Sort',
    sortAz: 'Name A–Z', sortStars: 'Most stars · snapshot', sortUpdated: 'Latest code push', reset: 'Reset filters',
    allProjects: 'All projects', allDescription: 'Build, connect, observe, and evaluate your agent workflows.',
    loading: 'Loading the catalogue…', loadingDescription: 'Preparing tools and source information.',
    errorTitle: 'The catalogue could not load', errorDescription: 'Try loading it again, or read the complete list on GitHub.', errorCount: 'Unavailable',
    retry: 'Try again', readmeFallback: 'Read the GitHub catalogue ↗', emptyTitle: 'No matching projects',
    emptyDescription: 'Try a shorter query, or clear the filters to explore again. You can search in English and Chinese.', emptyReset: 'Clear search and filters',
    catalogFootnote: 'Star counts were recorded when checked and may differ from GitHub today. “By curator” identifies projects built by the directory maintainer.',
    aboutTitle: 'Make this little list more useful.',
    aboutDescription: 'Official code, READMEs, and licenses inform each entry. Inclusion does not imply runtime validation or a security audit. Suggest a useful project or help update an entry.',
    aboutCta: 'Contribute', footerTagline: 'Good tools for your next build.', footerPrivacy: 'No tracking · No ads', footerSource: 'View source ↗',
    results: (count, total) => `${count} / ${total} projects`, curated: 'By curator', archived: 'Archived', fork: 'Fork',
    useCase: 'BEST USED FOR', starsSnapshot: 'stars · snapshot', pushedSnapshot: 'Code push (snapshot)', checked: 'Checked',
    source: 'Source README ↗', licenseSource: 'License source ↗', website: 'Website ↗', apiLicense: 'API license',
    notProvided: 'Not provided', projectList: 'Open-source project list', mainNav: 'Main navigation', pageTitle: 'Awesome Agent Stack · Open-source agent tools',
  },
};

const byId = id => document.getElementById(id);
const elements = {
  language: byId('language-toggle'), search: byId('search-input'), clear: byId('clear-search'),
  license: byId('license-filter'), sort: byId('sort-select'), reset: byId('reset-filters'),
  categories: byId('category-list'), grid: byId('project-grid'), count: byId('result-count'),
  title: byId('results-title'), description: byId('category-description'), status: byId('status-panel'),
  statusTitle: byId('status-title'), statusDescription: byId('status-description'),
  statusActions: byId('status-actions'), emptyReset: byId('empty-reset'), footnote: byId('catalog-footnote'),
};
let catalog = null;
let loading = true;
let failed = false;
let state = parseState(window.location.search, validation());
let categoryButtons = new Map();

function node(tag, className, text) {
  const result = document.createElement(tag);
  if (className) result.className = className;
  if (typeof text === 'string') result.textContent = text;
  return result;
}

function externalLink(text, value, className = '') {
  const url = safeHttpsUrl(value);
  if (!url) return null;
  const link = node('a', className, text);
  link.href = url;
  return link;
}

function repoUrl(project) {
  return typeof project.repo === 'string' && /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(project.repo)
    ? `https://github.com/${project.repo}` : null;
}

function dateLabel(value) {
  if (typeof value !== 'string' || !Number.isFinite(Date.parse(value))) return copy[state.lang].notProvided;
  return new Date(value).toISOString().slice(0, 10);
}

function validation() {
  return {
    categories: catalog ? catalog.categories.map(category => category.id) : CATEGORY_IDS,
    // Keep a shared license choice while loading or offline; validate after fetch.
    licenses: catalog ? [...new Set(catalog.projects.map(project => project.license))].sort()
      : [new URLSearchParams(window.location.search).get('license')].filter(Boolean),
  };
}

function updateUrl(replace = false) {
  const query = serializeState(state);
  const next = `${window.location.pathname}${query ? `?${query}` : ''}${window.location.hash}`;
  const current = `${window.location.pathname}${window.location.search}${window.location.hash}`;
  if (next !== current) window.history[replace ? 'replaceState' : 'pushState'](null, '', next);
}

function updateState(next, replace = false) {
  state = { ...state, ...next };
  updateUrl(replace);
  render();
}

function resetFilters() {
  updateState({ ...DEFAULT_STATE, lang: state.lang });
}

function prepareControls() {
  categoryButtons = new Map();
  const categories = [{ id: 'all' }, ...catalog.categories];
  const buttons = categories.map(category => {
    const button = node('button', 'category-button');
    button.type = 'button';
    button.dataset.category = category.id;
    const icon = node('span', 'category-icon', CATEGORY_ICONS[category.id] || '◇');
    icon.setAttribute('aria-hidden', 'true');
    const label = node('span', 'category-label');
    const count = node('span', 'category-count');
    count.setAttribute('aria-hidden', 'true');
    button.append(icon, label, count);
    button.addEventListener('click', () => updateState({ category: category.id }));
    categoryButtons.set(category.id, { button, label, count, category });
    return button;
  });
  elements.categories.replaceChildren(...buttons);
  elements.license.replaceChildren(...['all', ...validation().licenses].map(value => {
    const option = node('option', '', value);
    option.value = value;
    return option;
  }));
}

function translateInterface() {
  const text = copy[state.lang];
  document.documentElement.lang = state.lang === 'zh' ? 'zh-CN' : 'en';
  document.title = text.pageTitle;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const value = text[element.dataset.i18n];
    if (typeof value === 'string') element.textContent = value;
  });
  elements.language.textContent = state.lang === 'zh' ? 'EN' : '中文';
  elements.language.setAttribute('aria-label', state.lang === 'zh' ? 'Switch to English' : '切换到中文');
  elements.search.placeholder = text.searchPlaceholder;
  elements.clear.setAttribute('aria-label', text.clearSearch);
  elements.grid.setAttribute('aria-label', text.projectList);
  byId('main-nav').setAttribute('aria-label', text.mainNav);
  elements.license.options[0].textContent = text.allLicenses;
  for (const option of elements.sort.options) option.textContent = text[{ az: 'sortAz', stars: 'sortStars', updated: 'sortUpdated' }[option.value]];
}

function projectCard(project) {
  const text = copy[state.lang];
  const card = node('article', 'project-card');
  const top = node('div', 'card-category-row');
  const category = catalog.categories.find(value => value.id === project.category);
  top.append(node('span', 'card-category', localizedText(category?.label, state.lang) || project.category));
  if (project.curator_project === true) top.append(node('span', 'curator-label', text.curated));
  if (project.archived === true) top.append(node('span', 'state-label', text.archived));
  if (project.fork === true) top.append(node('span', 'state-label', text.fork));
  const title = node('h3', 'card-title');
  const link = externalLink(project.name, repoUrl(project));
  title.append(link || node('span', '', project.name));
  if (link) {
    const arrow = node('span', 'card-arrow', '↗');
    arrow.setAttribute('aria-hidden', 'true');
    title.append(arrow);
  }
  const useCase = node('div', 'card-use-case');
  useCase.append(node('strong', '', text.useCase), node('p', '', localizedText(project.use_case, state.lang)));
  const tags = node('div', 'card-tags');
  for (const tag of Array.isArray(project.tags) ? project.tags : []) {
    if (typeof tag === 'string') tags.append(node('span', 'card-tag', tag));
  }
  const meta = node('div', 'card-meta');
  const star = node('span', 'star-meta');
  const starIcon = node('span', 'star-icon', '☆');
  starIcon.setAttribute('aria-hidden', 'true');
  const number = Number.isFinite(project.stars) && project.stars >= 0 ? project.stars : 0;
  const count = new Intl.NumberFormat(state.lang === 'zh' ? 'zh-CN' : 'en', { notation: 'compact', maximumFractionDigits: 1 }).format(number);
  star.append(starIcon, node('strong', '', count), node('span', '', text.starsSnapshot));
  star.title = `${new Intl.NumberFormat(state.lang).format(number)} · ${dateLabel(project.checked_at)}`;
  meta.append(star, node('span', 'card-license', project.license), node('span', 'push-date', `${text.pushedSnapshot}: ${dateLabel(project.pushed_at)}`));
  const source = node('div', 'card-source');
  const sourceLinks = node('div', 'card-source-links');
  for (const [label, url] of [[text.source, project.evidence_url], [text.licenseSource, project.license_evidence_url], [text.website, project.website]]) {
    const sourceLink = externalLink(label, url);
    if (sourceLink) sourceLinks.append(sourceLink);
  }
  source.append(sourceLinks, node('span', '', `${text.checked} ${dateLabel(project.checked_at)}`));
  card.append(top, title, node('p', 'card-repo', project.repo), node('p', 'card-description', localizedText(project.description, state.lang)), useCase, tags, meta);
  const licenseNote = localizedText(project.license_note, state.lang);
  if (licenseNote) {
    const note = node('div', 'card-license-note');
    if (licenseNote) note.append(node('p', '', licenseNote));
    card.append(note);
  }
  card.append(source);
  return card;
}

function showStatus(kind) {
  const text = copy[state.lang];
  elements.status.hidden = false;
  elements.status.dataset.state = kind;
  elements.status.setAttribute('role', kind === 'error' ? 'alert' : 'status');
  elements.statusTitle.textContent = text[kind === 'error' ? 'errorTitle' : kind === 'empty' ? 'emptyTitle' : 'loading'];
  elements.statusDescription.textContent = text[kind === 'error' ? 'errorDescription' : kind === 'empty' ? 'emptyDescription' : 'loadingDescription'];
  elements.statusActions.hidden = kind !== 'error';
  elements.emptyReset.hidden = kind !== 'empty';
  elements.grid.hidden = true;
}

function render() {
  translateInterface();
  const text = copy[state.lang];
  const unavailable = loading || !catalog;
  elements.language.disabled = loading;
  elements.search.disabled = unavailable;
  elements.license.disabled = unavailable;
  elements.sort.disabled = unavailable;
  if (elements.search.value !== state.q) elements.search.value = state.q;
  elements.license.value = state.license;
  elements.sort.value = state.sort;
  elements.clear.hidden = !state.q || unavailable;
  elements.reset.hidden = unavailable || ![state.q, state.category !== 'all', state.license !== 'all', state.sort !== 'az'].some(Boolean);
  elements.footnote.hidden = unavailable;
  if (loading) {
    elements.count.textContent = text.loading;
    showStatus('loading');
    return;
  }
  if (failed || !catalog) {
    elements.count.textContent = text.errorCount;
    showStatus('error');
    return;
  }
  const counts = categoryCounts(catalog.projects, state, catalog.categories.map(category => category.id));
  for (const [id, item] of categoryButtons) {
    const label = id === 'all' ? text.allProjects : localizedText(item.category.label, state.lang);
    item.label.textContent = label;
    item.count.textContent = String(counts[id] || 0);
    item.button.setAttribute('aria-pressed', String(state.category === id));
    item.button.setAttribute('aria-label', `${label}, ${counts[id] || 0} ${state.lang === 'zh' ? '个项目' : 'projects'}`);
  }
  const category = catalog.categories.find(value => value.id === state.category);
  elements.title.textContent = category ? localizedText(category.label, state.lang) : text.allProjects;
  elements.description.textContent = category ? localizedText(category.description, state.lang) : text.allDescription;
  const projects = sortProjects(filterProjects(catalog.projects, state), state.sort);
  elements.count.textContent = text.results(projects.length, catalog.projects.length);
  if (!projects.length) {
    elements.grid.replaceChildren();
    showStatus('empty');
    return;
  }
  elements.status.hidden = true;
  elements.grid.replaceChildren(...projects.map(projectCard));
  elements.grid.hidden = false;
}

async function loadCatalogue() {
  if (loading && catalog) return;
  loading = true;
  failed = false;
  render();
  try {
    const response = await fetch('./catalog.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error('Catalogue unavailable');
    const value = await response.json();
    if (value?.schema_version !== 1 || !Array.isArray(value.projects) || !Array.isArray(value.categories) || !value.categories.length ||
      value.categories.some(category => !category || typeof category.id !== 'string') ||
      value.projects.some(project => !project || typeof project.name !== 'string' || typeof project.repo !== 'string' || typeof project.category !== 'string' || typeof project.license !== 'string')) {
      throw new Error('Invalid catalogue');
    }
    catalog = value;
    state = parseState(window.location.search, validation());
    prepareControls();
    const repo = safeHttpsUrl(catalog.repo_url) || REPO_URL;
    for (const id of ['header-repo', 'footer-repo']) byId(id).href = repo;
    for (const id of ['sidebar-contribute', 'about-contribute']) byId(id).href = `${repo.replace(/\/$/, '')}/issues/new?template=submit-project.yml`;
    byId('fallback-readme').href = `${repo}#readme`;
    byId('project-total').textContent = String(catalog.projects.length);
    byId('category-total').textContent = String(catalog.categories.length);
    byId('snapshot-date').textContent = dateLabel(catalog.updated_at);
    updateUrl(true);
  } catch {
    failed = true;
    catalog = null;
  } finally {
    loading = false;
    render();
  }
}

elements.language.addEventListener('click', () => updateState({ lang: state.lang === 'zh' ? 'en' : 'zh' }));
elements.search.addEventListener('input', event => updateState({ q: event.target.value }, true));
elements.license.addEventListener('change', event => updateState({ license: event.target.value }));
elements.sort.addEventListener('change', event => updateState({ sort: event.target.value }));
elements.clear.addEventListener('click', () => { updateState({ q: '' }); elements.search.focus(); });
elements.reset.addEventListener('click', () => { resetFilters(); elements.search.focus(); });
elements.emptyReset.addEventListener('click', () => { resetFilters(); elements.search.focus(); });
byId('retry-button').addEventListener('click', async () => {
  await loadCatalogue();
  (catalog ? elements.search : byId('retry-button')).focus();
});
window.addEventListener('popstate', () => { state = parseState(window.location.search, validation()); render(); });
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && event.target === elements.search && state.q) updateState({ q: '' }, true);
});
loadCatalogue();
