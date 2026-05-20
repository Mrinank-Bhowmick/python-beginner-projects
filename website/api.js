// Tiny client wrapper around the Cloudflare Workers Python backend.
// Exposed as window.PBP_API so the JSX modules can reach it.
//
// Base URL is read from `window.PBP_API_BASE` (set in index.html). Leave empty
// for same-origin (e.g., local wrangler dev with assets), or set to the deployed
// Worker URL like "https://pybegin-api.<account>.workers.dev" for the
// split Pages-frontend + Worker-API production setup.

(function () {
  const BASE = (typeof window !== 'undefined' && window.PBP_API_BASE) || '';
  const RUNNABLE = {
    rps: {
      endpoint: '/api/rps',
      inputs: [
        { key: 'choice', label: 'Your throw', type: 'select', options: ['rock', 'paper', 'scissors'], default: 'rock' },
      ],
    },
    bmi: {
      endpoint: '/api/bmi',
      inputs: [
        { key: 'height_m', label: 'Height (m)', type: 'number', step: 0.01, min: 0.5, max: 2.5, default: 1.75 },
        { key: 'weight_kg', label: 'Weight (kg)', type: 'number', step: 0.1, min: 10, max: 400, default: 70 },
      ],
    },
    qr: {
      endpoint: '/api/qr',
      inputs: [
        { key: 'text', label: 'Text or URL', type: 'text', default: 'https://github.com/Mrinank-Bhowmick/python-beginner-projects' },
      ],
    },
    madlibs: {
      endpoint: '/api/madlibs',
      inputs: [
        { key: 'story', label: 'Story', type: 'select', options: [
            { value: 1, label: '1 · Mystical land' },
            { value: 2, label: '2 · Wizard academy' },
            { value: 3, label: '3 · Time machine' },
          ], default: 1 },
        { key: 'adjective', label: 'Adjective', type: 'text', default: 'sparkly' },
        { key: 'noun', label: 'Noun', type: 'text', default: 'penguin' },
        { key: 'verb', label: 'Verb', type: 'text', default: 'dancing' },
        { key: 'adverb', label: 'Adverb', type: 'text', default: 'wildly' },
      ],
    },
    tictactoe: {
      endpoint: '/api/tictactoe',
      interactive: 'tictactoe', // custom UI component
    },
    hangman: {
      endpoint: '/api/hangman',
      interactive: 'hangman',
    },
  };

  async function call(id, payload) {
    const cfg = RUNNABLE[id];
    if (!cfg) throw new Error('Not runnable: ' + id);
    const res = await fetch(BASE + cfg.endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload || {}),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.error || ('HTTP ' + res.status));
    return data;
  }

  function defaults(id) {
    const cfg = RUNNABLE[id];
    if (!cfg || !cfg.inputs) return {};
    const out = {};
    for (const f of cfg.inputs) out[f.key] = f.default;
    return out;
  }

  function isRunnable(id) { return !!RUNNABLE[id]; }
  function isInteractive(id) { return !!(RUNNABLE[id] && RUNNABLE[id].interactive); }
  function inputsFor(id) { return (RUNNABLE[id] && RUNNABLE[id].inputs) || []; }

  window.PBP_API = { call, defaults, isRunnable, isInteractive, inputsFor, RUNNABLE };
})();
