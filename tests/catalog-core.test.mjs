import test from 'node:test';
import assert from 'node:assert/strict';
import {
  normalizeSearch, filterProjects, sortProjects, categoryCounts,
  parseState, serializeState, safeHttpsUrl, localizedText,
} from '../site/catalog-core.mjs';

const projects = [
  { id: 'alpha', name: 'Alpha Agent', repo: 'team/alpha', category: 'frameworks', license: 'MIT', stars: 12,
    pushed_at: '2026-10-07T10:00:00Z', description: { en: 'Composable workflow framework', zh: '可组合的智能体框架' },
    use_case: { en: 'Build a research assistant', zh: '构建研究助手' }, tags: ['python', 'workflow'] },
  { id: 'beta', name: 'Beta Lab', repo: 'example/beta', category: 'evaluation', license: 'Apache-2.0', stars: 99,
    pushed_at: '2026-10-08T10:00:00Z', description: { en: 'Measure agent quality', zh: '评估智能体质量' },
    use_case: { en: 'Compare research results', zh: '比较研究结果' }, tags: ['evaluation', 'python'] },
  { id: 'gamma', name: 'Gamma Tools', repo: 'team/gamma', category: 'security', license: 'MIT', stars: 99,
    pushed_at: '2026-09-20T10:00:00Z', description: { en: 'Café security checks', zh: '开源安全检查' },
    use_case: { en: 'Inspect risky agent actions', zh: '检查智能体行为' }, tags: ['security', 'typescript'] },
];
const validation = { categories: ['frameworks', 'evaluation', 'security'], licenses: ['MIT', 'Apache-2.0'] };
const ids = values => values.map(value => value.id);

test('search normalizes case, equivalent Unicode and full-width text', () => {
  assert.equal(normalizeSearch(' ＡＧＥＮＴ Cafe\u0301 '), 'agent café');
});

test('search finds Chinese and English regardless of display language', () => {
  assert.deepEqual(ids(filterProjects(projects, { q: '研究 assistant', lang: 'en' })), ['alpha']);
  assert.deepEqual(ids(filterProjects(projects, { q: '智能体 quality', lang: 'zh' })), ['beta']);
});

test('all search terms must match, including repository and tags', () => {
  assert.deepEqual(ids(filterProjects(projects, { q: 'TEAM/ALPHA python research' })), ['alpha']);
  assert.deepEqual(ids(filterProjects(projects, { q: 'research security' })), []);
});

test('canonical Unicode search matches accented project descriptions', () => {
  assert.deepEqual(ids(filterProjects(projects, { q: 'Cafe\u0301' })), ['gamma']);
});

test('category and license filters combine with search', () => {
  assert.deepEqual(ids(filterProjects(projects, { category: 'frameworks', license: 'MIT', q: 'python' })), ['alpha']);
  assert.deepEqual(ids(filterProjects(projects, { category: 'evaluation', license: 'MIT' })), []);
});

test('blank search and all filters keep all projects', () => {
  assert.deepEqual(ids(filterProjects(projects, { q: '  ', category: 'all', license: 'all' })), ['alpha', 'beta', 'gamma']);
});

test('category counts reflect search and license without excluding other categories', () => {
  assert.deepEqual(categoryCounts(projects, { q: '智能体', license: 'MIT', category: 'security' }, validation.categories), {
    all: 2, frameworks: 1, evaluation: 0, security: 1,
  });
});

test('A–Z sort uses names and leaves the source array untouched', () => {
  const reversed = [...projects].reverse();
  assert.deepEqual(ids(sortProjects(reversed, 'az')), ['alpha', 'beta', 'gamma']);
  assert.deepEqual(ids(reversed), ['gamma', 'beta', 'alpha']);
});

test('stars sort is descending and ties have deterministic alphabetical order', () => {
  assert.deepEqual(ids(sortProjects(projects, 'stars')), ['beta', 'gamma', 'alpha']);
});

test('latest sort uses code push timestamps and puts unknown dates last', () => {
  assert.deepEqual(ids(sortProjects([...projects, { id: 'unknown', name: 'A missing date', pushed_at: 'unknown' }], 'updated')),
    ['beta', 'alpha', 'gamma', 'unknown']);
});

test('unknown URL filters fall back to safe defaults', () => {
  assert.deepEqual(parseState('?category=evil&license=wrong&sort=popular&lang=fr&q=%20Agent%20', validation),
    { q: 'Agent', category: 'all', license: 'all', sort: 'az', lang: 'zh' });
});

test('valid URL filters preserve a shareable bilingual search', () => {
  assert.deepEqual(parseState('?q=%E6%99%BA%E8%83%BD%E4%BD%93+python&category=security&license=MIT&sort=stars&lang=en', validation),
    { q: '智能体 python', category: 'security', license: 'MIT', sort: 'stars', lang: 'en' });
});

test('state serialization is encoded, round-trips and omits defaults', () => {
  const value = { q: '智能体 & python', category: 'security', license: 'MIT', sort: 'updated', lang: 'en' };
  const encoded = serializeState(value);
  assert.equal(encoded, 'q=%E6%99%BA%E8%83%BD%E4%BD%93+%26+python&category=security&license=MIT&sort=updated&lang=en');
  assert.deepEqual(parseState(`?${encoded}`, validation), value);
  assert.equal(serializeState({ q: '', category: 'all', license: 'all', sort: 'az', lang: 'zh' }), '');
});

test('project links only accept HTTPS URLs without credentials', () => {
  assert.equal(safeHttpsUrl('https://example.com/docs'), 'https://example.com/docs');
  for (const value of ['javascript:alert(1)', 'http://example.com', '//example.com', 'https://user:password@example.com', '', null]) {
    assert.equal(safeHttpsUrl(value), null);
  }
});

test('localized copy falls back to available text without producing objects', () => {
  assert.equal(localizedText({ zh: '说明', en: 'Description' }, 'zh'), '说明');
  assert.equal(localizedText({ zh: '说明' }, 'en'), '说明');
  assert.equal(localizedText(null, 'zh'), '');
  assert.equal(localizedText({ en: { unexpected: true } }, 'en'), '');
});
