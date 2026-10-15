import test from 'node:test';
import assert from 'node:assert/strict';
import * as refresh from '../site/catalog-core.mjs';

const sample = () => ({ schema_version: 1, updated_at: '2026-10-09',
  categories: [{ id: 'mcp' }], projects: [{ name: 'Sample', repo: 'team/sample', category: 'mcp', license: 'MIT', stars: 10 }] });

test('published data refresh applies changed first-party data and ignores identical snapshots', async () => {
  assert.equal(typeof refresh.createCatalogRefresh, 'function');
  const values = [];
  let value = sample();
  const load = refresh.createCatalogRefresh({
    fetchImpl: async (url, options) => {
      assert.equal(url, './catalog.json');
      assert.equal(options.cache, 'no-cache');
      return { ok: true, json: async () => value };
    }, onCatalog: data => values.push(data), onFailure: assert.fail,
  });
  await load();
  await load();
  value = { ...sample(), metadata_refresh: { status: 'complete' } };
  await load();
  assert.equal(values.length, 2);
  assert.equal(values[0].projects[0].stars, 10);
});

test('offline, invalid and concurrent refreshes retain last accepted data', async () => {
  assert.equal(typeof refresh.createCatalogRefresh, 'function');
  let accept = 0;
  let errors = 0;
  let response = { ok: true, json: async () => sample() };
  let release;
  const load = refresh.createCatalogRefresh({ fetchImpl: async () => response,
    onCatalog: () => accept++, onFailure: () => errors++ });
  await load();
  response = { ok: false };
  await load();
  response = { ok: true, json: async () => ({ schema_version: 1, projects: [null], categories: [] }) };
  await load();
  response = new Promise(resolve => { release = resolve; });
  const first = load();
  const second = load();
  release({ ok: true, json: async () => sample() });
  await Promise.all([first, second]);
  assert.equal(accept, 1);
  assert.equal(errors, 2);
});

test('automatic refresh polls every minute only in foreground and refreshes on return', () => {
  assert.equal(typeof refresh.startForegroundRefresh, 'function');
  const document = new EventTarget();
  const window = new EventTarget();
  document.visibilityState = 'visible';
  let tick;
  let calls = 0;
  refresh.startForegroundRefresh({ refresh: () => calls++, document, window,
    setIntervalImpl: (callback, milliseconds) => { assert.equal(milliseconds, 60000); tick = callback; } });
  tick();
  document.visibilityState = 'hidden';
  tick();
  document.dispatchEvent(new Event('visibilitychange'));
  window.dispatchEvent(new Event('focus'));
  assert.equal(calls, 1);
  document.visibilityState = 'visible';
  document.dispatchEvent(new Event('visibilitychange'));
  window.dispatchEvent(new Event('focus'));
  assert.equal(calls, 3);
});

test('freshness copy distinguishes metadata from human evidence and explains failures', () => {
  assert.equal(typeof refresh.metadataSummary, 'function');
  for (const lang of ['en', 'zh']) {
    const data = sample();
    data.metadata_refresh = { status: 'partial', attempted_at: '2026-10-15T01:00:00Z',
      last_complete_at: '2026-10-14T01:00:00Z', failed_repos: ['team/sample'] };
    const text = refresh.metadataSummary(data, lang);
    assert.ok(text.includes('2026-10-15'));
    assert.ok(text.includes('2026-10-14'));
    assert.ok(text.includes('1'));
    assert.ok(text.includes(lang === 'en' ? 'preserved' : '保留'));
    assert.ok(refresh.metadataSummary(sample(), lang).includes(lang === 'en' ? 'not yet' : '尚未'));
  }
});
