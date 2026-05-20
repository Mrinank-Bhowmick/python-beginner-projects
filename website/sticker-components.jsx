// === Sticker Pack · standalone prototype components ===

const { useState, useEffect, useMemo, useRef } = React;

function StickerLogo() {
  return (
    <svg viewBox="0 0 32 32" fill="none">
      <path d="M8 9c0-2 1.5-3 4-3h4c2.5 0 4 1 4 3v3H8V9z" fill="#1d1830" />
      <path d="M8 12h12v6c0 2-1.5 3-4 3h-2v-3h2v-3h-8v3c0 2-1.5 3-4 3v-9z" fill="#fef9ef" stroke="#1d1830" strokeWidth="1.4" />
      <circle cx="11" cy="9.5" r="1.2" fill="#fef9ef" />
      <circle cx="11" cy="9.5" r="0.5" fill="#1d1830" />
    </svg>
  );
}

function ScribbleSvg({ color }) {
  // SVG inline so accent color works without rebuilding background-image
  return (
    <svg style={{position:'absolute', bottom:-10, left:-4, right:-4, width:'calc(100% + 8px)', height:14, overflow:'visible'}} viewBox="0 0 200 14" preserveAspectRatio="none">
      <path d="M2,8 Q40,1 80,7 T160,6 T198,8" stroke={color} strokeWidth="4" fill="none" strokeLinecap="round"/>
    </svg>
  );
}

function HeroStickers() {
  // Bobbing pile of stickers in the hero — pulls a few highlight projects
  const items = [
    { e: '🐍', l: 'Snake Game',  n: '92 lines · pygame',  bg: 'var(--s-surface-warm)',  pos: { top: 6,  left: 18 },  bob: 1, rot: -4 },
    { e: '☁️', l: 'Weather App', n: '88 lines · requests',bg: 'var(--s-surface-cool)',  pos: { top: 80, right: 0 },  bob: 2, rot: 3 },
    { e: '🪢', l: 'Hangman',     n: '78 lines · stdlib',  bg: 'var(--s-surface-purple)',pos: { top: 215, left: -10 },bob: 3, rot: 2 },
    { e: '▦',  l: 'QR Generator',n: '22 lines · qrcode',  bg: 'var(--s-surface-green)', pos: { top: 290, right: 50 },bob: 4, rot: -2 },
    { e: '🧮', l: 'Calculator',  n: '110 lines · tk',     bg: 'var(--s-surface-yellow)',pos: { top: 400, left: 60 }, bob: 5, rot: 4 },
    { e: '🔐', l: 'Password Gen',n: '30 lines · secrets', bg: '#ffd4f0',                pos: { top: 410, right: 10 },bob: 1, rot: -3 },
  ];
  return (
    <div className="s-stickers">
      {items.map((s, i) => (
        <div key={i} className="s-sticker"
          style={{
            ...s.pos,
            background: s.bg,
            animation: `s-bob${s.bob} ${4 + i*0.3}s ease-in-out infinite`,
            animationDelay: `${-i * 0.7}s`,
            transform: `rotate(${s.rot}deg)`,
          }}>
          <span className="emoji">{s.e}</span>
          <div>
            <div className="lbl">{s.l}</div>
            <div className="num">{s.n}</div>
          </div>
        </div>
      ))}
    </div>
  );
}

function ProjectCard({ p, cardStyle, isBm, toggleBm, onOpen }) {
  return (
    <div className={`s-card ${cardStyle}`} onClick={() => onOpen(p)}>
      {cardStyle === 'image' && <div className="s-img">{p.emoji}</div>}
      {cardStyle !== 'image' && <div className="s-card-emoji">{p.emoji}</div>}
      <div className="s-card-h">
        <h3 className="s-card-name">{p.name}</h3>
        <button className={`s-card-bm ${isBm ? 'on' : ''}`} onClick={e => { e.stopPropagation(); toggleBm(p.id); }} aria-label="Bookmark">
          {isBm ? '★' : '☆'}
        </button>
      </div>
      <p className="s-card-blurb">{p.blurb}</p>
      <div className="s-card-meta">
        <span className="s-meta-pill">{p.lines} lines</span>
        <span className="s-meta-pill dep">{p.deps}</span>
        {p.runnable && <span className="s-meta-pill run">▶ Try it</span>}
      </div>
    </div>
  );
}

function ProjectModal({ p, onClose, isBm, toggleBm }) {
  useEffect(() => {
    const k = (e) => e.key === 'Escape' && onClose();
    window.addEventListener('keydown', k);
    return () => window.removeEventListener('keydown', k);
  }, [onClose]);
  if (!p) return null;
  return (
    <div className="s-modal-bg" onClick={onClose}>
      <div className="s-modal" onClick={e => e.stopPropagation()}>
        <button className="s-modal-x" onClick={onClose}>✕</button>
        <div className="s-modal-emoji">{p.emoji}</div>
        <h2>{p.name}</h2>
        <p className="s-modal-blurb">{p.blurb}</p>
        <div className="s-modal-meta">
          <span className="s-meta-pill">{p.lines} lines</span>
          <span className="s-meta-pill dep">{p.deps}</span>
          <span className="s-meta-pill dep">{p.cat}</span>
        </div>
        <div className="s-modal-code">
          <div style={{color:'var(--s-accent)'}}>$ git clone python-beginner-projects.git</div>
          <div style={{color:'rgba(254,249,239,0.6)'}}>$ cd projects/{p.id}</div>
          <div>$ python {p.id}.py</div>
        </div>
        {p.runnable && <TryItPanel project={p} />}
        <div className="s-modal-actions">
          <button className="s-btn-pri" onClick={() => toggleBm(p.id)}>
            {isBm ? '★ Bookmarked' : '☆ Bookmark this'}
          </button>
          <button className="s-btn-sec">View on GitHub →</button>
        </div>
      </div>
    </div>
  );
}

// ============================================================
// Try It — live demo panel inside the project modal.
// Renders a simple input form for stateless projects (rps, bmi, qr,
// madlibs) and hands off to dedicated widgets for the turn-based ones
// (tictactoe, hangman). All POSTs go to the single Vercel backend.
// ============================================================

function TryItPanel({ project }) {
  const api = window.PBP_API;
  if (api.isInteractive(project.id)) {
    if (project.id === 'tictactoe') return <TicTacToePlay />;
    if (project.id === 'hangman') return <HangmanPlay />;
  }
  return <SimpleRunner project={project} />;
}

function SimpleRunner({ project }) {
  const fields = window.PBP_API.inputsFor(project.id);
  const [form, setForm] = useState(() => window.PBP_API.defaults(project.id));
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [out, setOut] = useState(null);

  const run = async () => {
    setError(null);
    setLoading(true);
    try {
      const res = await window.PBP_API.call(project.id, form);
      setOut(res);
    } catch (e) {
      setError(e.message || 'Request failed');
      setOut(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="s-try">
      <div className="s-try-h">▶ Try it live</div>
      <div className="s-try-form">
        {fields.map(f => (
          <label key={f.key} className="s-try-field">
            <span>{f.label}</span>
            {f.type === 'select' ? (
              <select value={form[f.key]} onChange={e => setForm({ ...form, [f.key]: castOption(f, e.target.value) })}>
                {f.options.map(opt => {
                  const v = typeof opt === 'object' ? opt.value : opt;
                  const l = typeof opt === 'object' ? opt.label : opt;
                  return <option key={String(v)} value={String(v)}>{l}</option>;
                })}
              </select>
            ) : f.type === 'number' ? (
              <input type="number" step={f.step} min={f.min} max={f.max}
                value={form[f.key]}
                onChange={e => setForm({ ...form, [f.key]: e.target.value === '' ? '' : Number(e.target.value) })} />
            ) : (
              <input type="text" value={form[f.key] || ''}
                onChange={e => setForm({ ...form, [f.key]: e.target.value })} />
            )}
          </label>
        ))}
      </div>
      <button className="s-btn-pri s-try-run" onClick={run} disabled={loading}>
        {loading ? 'Running…' : 'Run'}
      </button>
      {error && <div className="s-try-error">⚠ {error}</div>}
      {out && <SimpleOutput projectId={project.id} out={out} />}
    </div>
  );
}

function castOption(field, raw) {
  if (Array.isArray(field.options) && field.options.length && typeof field.options[0] === 'object') {
    const match = field.options.find(o => String(o.value) === raw);
    return match ? match.value : raw;
  }
  return raw;
}

function SimpleOutput({ projectId, out }) {
  if (projectId === 'qr' && out.png_b64) {
    return (
      <div className="s-try-out">
        <img alt="QR code" src={`data:image/png;base64,${out.png_b64}`} style={{width: 220, height: 220, imageRendering: 'pixelated', borderRadius: 12, background:'#fff', padding: 8}} />
      </div>
    );
  }
  if (projectId === 'bmi') {
    return (
      <div className="s-try-out">
        <div style={{fontSize: 32, fontWeight: 800}}>{out.bmi}</div>
        <div style={{opacity: 0.8}}>{out.category}</div>
      </div>
    );
  }
  if (projectId === 'rps') {
    const verdict = { win: '🎉 You win', lose: '😅 You lose', draw: '🤝 Draw' }[out.result] || out.result;
    return (
      <div className="s-try-out">
        <div>You: <b>{out.player}</b> · CPU: <b>{out.cpu}</b></div>
        <div style={{fontSize: 20, fontWeight: 700, marginTop: 4}}>{verdict}</div>
      </div>
    );
  }
  if (projectId === 'madlibs') {
    return <div className="s-try-out s-try-story"><pre>{out.story}</pre></div>;
  }
  return <pre className="s-try-out">{JSON.stringify(out, null, 2)}</pre>;
}

// ---- Tic Tac Toe interactive ----

const EMPTY_BOARD = ['', '', '', '', '', '', '', '', ''];

function TicTacToePlay() {
  const [board, setBoard] = useState(EMPTY_BOARD);
  const [status, setStatus] = useState('ongoing');
  const [winner, setWinner] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const reset = () => { setBoard(EMPTY_BOARD); setStatus('ongoing'); setWinner(null); setError(null); };

  const play = async (idx) => {
    if (board[idx] || status !== 'ongoing' || loading) return;
    setError(null);
    setLoading(true);
    try {
      const res = await window.PBP_API.call('tictactoe', { board, player: 'X', move: idx });
      setBoard(res.board);
      setStatus(res.status);
      setWinner(res.winner || null);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const headline = status === 'win'
    ? (winner === 'X' ? '🎉 You win' : '🤖 CPU wins')
    : status === 'draw' ? '🤝 Draw' : 'Your move (X)';

  return (
    <div className="s-try">
      <div className="s-try-h">▶ Try it live · vs the bot</div>
      <div style={{display:'flex', alignItems:'center', justifyContent:'space-between', marginBottom: 10}}>
        <div style={{fontWeight:700}}>{headline}</div>
        <button className="s-btn-sec" onClick={reset} style={{padding:'6px 14px', fontSize: 13}}>Reset</button>
      </div>
      <div className="s-ttt-grid">
        {board.map((cell, i) => (
          <button key={i} className="s-ttt-cell" onClick={() => play(i)} disabled={!!cell || status !== 'ongoing' || loading}>
            <span data-mark={cell}>{cell}</span>
          </button>
        ))}
      </div>
      {error && <div className="s-try-error">⚠ {error}</div>}
    </div>
  );
}

// ---- Hangman interactive ----

const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

function HangmanPlay() {
  const [seed, setSeed] = useState(() => Math.floor(Math.random() * 1e9));
  const [difficulty, setDifficulty] = useState('medium');
  const [guessed, setGuessed] = useState([]);
  const [state, setState] = useState(null); // {mask, wrong, tries_left, max_tries, status, word_length, word?}
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const refresh = async (nextGuessed, nextDifficulty = difficulty, nextSeed = seed) => {
    setError(null);
    setLoading(true);
    try {
      const res = await window.PBP_API.call('hangman', { word_seed: nextSeed, guessed: nextGuessed, difficulty: nextDifficulty });
      setState(res);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { refresh([], difficulty, seed); /* eslint-disable-next-line */ }, []);

  const guess = (letter) => {
    if (loading || !state || state.status !== 'ongoing' || guessed.includes(letter)) return;
    const next = [...guessed, letter];
    setGuessed(next);
    refresh(next);
  };

  return (
    <div className="s-try">
      <div className="s-try-h">▶ Try it live · pick letters</div>
      <div className="s-hg-row">
        <label className="s-try-field" style={{flex: '0 0 auto'}}>
          <span>Difficulty</span>
          <select value={difficulty} onChange={e => { const v = e.target.value; const s = Math.floor(Math.random() * 1e9); setDifficulty(v); setSeed(s); setGuessed([]); refresh([], v, s); }}>
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
        </label>
        <button className="s-btn-sec" onClick={() => { const s = Math.floor(Math.random() * 1e9); setSeed(s); setGuessed([]); refresh([], difficulty, s); }} style={{alignSelf:'end'}}>New word</button>
      </div>
      {state && (
        <>
          <div className="s-hg-word">
            {state.mask.split('').map((c, i) => <span key={i} className="s-hg-slot">{c === '_' ? '·' : c}</span>)}
          </div>
          <div className="s-hg-meta">
            <span>{state.tries_left} / {state.max_tries} tries left</span>
            <span className="s-hg-wrong">{state.wrong.length ? 'wrong: ' + state.wrong.join(' ') : ''}</span>
          </div>
          <div className="s-hg-keys">
            {ALPHABET.map(l => {
              const used = guessed.includes(l);
              const hit = used && state.mask.includes(l);
              return (
                <button key={l}
                  className={`s-hg-key ${used ? 'used' : ''} ${hit ? 'hit' : used ? 'miss' : ''}`}
                  onClick={() => guess(l)}
                  disabled={used || state.status !== 'ongoing' || loading}>
                  {l}
                </button>
              );
            })}
          </div>
          {state.status === 'win' && <div className="s-try-out">🎉 You got it!</div>}
          {state.status === 'lose' && <div className="s-try-out">😅 Out of tries — the word was <b>{state.word}</b></div>}
        </>
      )}
      {error && <div className="s-try-error">⚠ {error}</div>}
    </div>
  );
}

window.StickerLogo = StickerLogo;
window.ScribbleSvg = ScribbleSvg;
window.HeroStickers = HeroStickers;
window.ProjectCard = ProjectCard;
window.ProjectModal = ProjectModal;
