// === Sticker Pack · main App ===

function StickerApp() {
  const [t, setTweak] = useTweaks(window.STICKER_TWEAK_DEFAULTS);
  const [search, setSearch] = useState('');
  const [cat, setCat] = useState('all');
  const [bm, setBm] = useState(() => window.PBP_BM.get());
  const [sort, setSort] = useState('default');
  const [open, setOpen] = useState(null);
  const [showBmOnly, setShowBmOnly] = useState(false);

  const toggleBm = (id) => setBm(window.PBP_BM.toggle(id));

  // Filter + sort
  const filtered = useMemo(() => {
    let arr = window.PBP_PROJECTS.filter(p => {
      if (showBmOnly && !bm.includes(p.id)) return false;
      if (cat !== 'all' && p.cat !== cat) return false;
      if (search) {
        const q = search.toLowerCase();
        return p.name.toLowerCase().includes(q) || p.blurb.toLowerCase().includes(q) || p.deps.toLowerCase().includes(q);
      }
      return true;
    });
    if (sort === 'alpha') arr = [...arr].sort((a,b) => a.name.localeCompare(b.name));
    if (sort === 'short') arr = [...arr].sort((a,b) => a.lines - b.lines);
    if (sort === 'bookmarks') arr = [...arr].sort((a,b) => (bm.includes(b.id) ? 1 : 0) - (bm.includes(a.id) ? 1 : 0));
    return arr;
  }, [search, cat, bm, sort, showBmOnly]);

  // Tweak CSS vars
  const rootStyle = useMemo(() => ({
    '--s-accent': t.accent,
    '--s-display': t.fontDisplay,
    '--s-body': t.fontBody,
    '--s-bg': t.surface === 'cream' ? '#fef9ef' : t.surface === 'mint' ? '#eefbf2' : t.surface === 'sky' ? '#eff6ff' : t.surface === 'lilac' ? '#f4eefe' : '#fef9ef',
  }), [t]);

  return (
    <div style={rootStyle}>
      <div className="s-shell">

        {/* NAV */}
        <nav className="s-nav">
          <div className="s-logo">
            <div className="s-logomark"><StickerLogo /></div>
            <div>
              <div className="s-brand-name">pyBegin</div>
              <div className="s-brand-sub">100 projects · 1 weekend each</div>
            </div>
          </div>
          <div className="s-navlinks">
            <button className="active">Home</button>
            <button onClick={() => document.getElementById('gallery').scrollIntoView({behavior:'smooth', block:'start'})}>Projects</button>
            <button onClick={() => document.getElementById('paths').scrollIntoView({behavior:'smooth', block:'start'})}>Learn</button>
            <button onClick={() => document.getElementById('crew').scrollIntoView({behavior:'smooth', block:'start'})}>Contribute</button>
          </div>
          <div className="s-nav-right">
            <div className={`s-bm-count ${bm.length ? 'has' : ''}`} title="Bookmarks" onClick={() => { setShowBmOnly(v => !v); document.getElementById('gallery').scrollIntoView({behavior:'smooth'}); }}>
              ★<span style={{fontSize:11, marginLeft:2}}>{bm.length}</span>
            </div>
            <button className="s-cta">★ Star · 2.3k</button>
          </div>
        </nav>

        {/* HERO */}
        <section className="s-hero">
          <div>
            <div className="s-tag"><span className="dot"></span>Live · 100 projects from 241 humans</div>
            <h1 className="s-headline">
              Python
              <br />
              that <span className="scribble">feels good<ScribbleSvg color={t.accent} /></span>
              <br />
              to type.
            </h1>
            <p className="s-sub">A scrappy collection of tiny Python projects. Each one is small enough to read in a coffee break and big enough to teach you something real. Pick a vibe. Type it out. Run it.</p>
            <div className="s-hero-cta">
              <button className="s-btn-pri" onClick={() => document.getElementById('paths').scrollIntoView({behavior:'smooth'})}>
                <span>🚀</span> Start with a path
              </button>
              <button className="s-btn-sec" onClick={() => document.getElementById('gallery').scrollIntoView({behavior:'smooth'})}>
                Browse all →
              </button>
            </div>
          </div>
          <HeroStickers />
        </section>

        {/* STATS */}
        <div className="s-stats">
          <div className="s-stat"><div className="s-stat-n">100</div><div className="s-stat-l">Projects</div></div>
          <div className="s-stat"><div className="s-stat-n">241</div><div className="s-stat-l">Contributors</div></div>
          <div className="s-stat"><div className="s-stat-n">2.3k</div><div className="s-stat-l">★ Stars</div></div>
          <div className="s-stat"><div className="s-stat-n">903</div><div className="s-stat-l">Forks</div></div>
        </div>

        {/* PATHS */}
        <section className="s-section" id="paths">
          <div className="s-section-h">
            <h2 className="s-section-title">Three <em>paths</em> in.</h2>
            <div className="s-section-side">Not sure where to start? Each path is three projects, building on each other. Finish one in a weekend.</div>
          </div>
          <div className="s-paths">
            {window.PBP_PATHS.map((p, idx) => (
              <div key={p.id} className="s-path">
                <div className="s-path-head">
                  <div className="s-path-tag">{p.tag.toUpperCase()}</div>
                  <div className="s-path-num">0{idx+1}</div>
                </div>
                <h3 className="s-path-name">{p.name}</h3>
                <p className="s-path-desc">{p.desc}</p>
                <div className="s-path-list">
                  {p.items.map((id, i) => {
                    const pr = window.PBP_PROJECTS.find(d => d.id === id);
                    return pr && (
                      <div key={id} className="s-path-item" onClick={() => setOpen(pr)}>
                        <i>0{i+1}</i>
                        <span style={{flex:1}}>{pr.name}</span>
                        <span className="em">{pr.emoji}</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* GALLERY */}
        <section className="s-section" id="gallery">
          <div className="s-section-h">
            <h2 className="s-section-title">All the <em>projects</em>.</h2>
            <div className="s-section-side">{filtered.length} of {window.PBP_PROJECTS.length} shown · {bm.length} bookmarked</div>
          </div>
          <div className="s-toolbar">
            <div className="s-search">
              <span className="s-search-icon">🔍</span>
              <input placeholder="What do you want to build?" value={search} onChange={e => setSearch(e.target.value)} />
              {search && <span style={{cursor:'pointer', opacity:0.5}} onClick={() => setSearch('')}>✕</span>}
              <span className="s-search-key">⌘ K</span>
            </div>
            <button className="s-sort" onClick={() => {
              const order = ['default', 'alpha', 'short', 'bookmarks'];
              setSort(order[(order.indexOf(sort) + 1) % order.length]);
            }}>
              <span>↕</span> {sort === 'default' ? 'Featured' : sort === 'alpha' ? 'A → Z' : sort === 'short' ? 'Shortest first' : '★ Bookmarked first'}
            </button>
          </div>
          <div className="s-chips">
            {window.PBP_CATEGORIES.map(c => (
              <button key={c.id} className={`s-chip ${c.id === cat && !showBmOnly ? 'active' : ''}`} onClick={() => { setCat(c.id); setShowBmOnly(false); }}>
                {c.name} <span className="ct">{c.count}</span>
              </button>
            ))}
            {bm.length > 0 && (
              <button className={`s-chip bm ${showBmOnly ? 'active' : ''}`} onClick={() => setShowBmOnly(v => !v)}>
                <span className="ic">★</span> Bookmarked <span className="ct">{bm.length}</span>
              </button>
            )}
          </div>
          {filtered.length === 0 ? (
            <div className="s-empty">
              <div className="em">🫧</div>
              <h3>No projects match that.</h3>
              <p>Try a different search or clear the filters.</p>
            </div>
          ) : (
            <div className={`s-gallery ${t.layout}`}>
              {filtered.map(p => (
                <ProjectCard
                  key={p.id} p={p}
                  cardStyle={t.cardStyle}
                  isBm={bm.includes(p.id)}
                  toggleBm={toggleBm}
                  onOpen={setOpen}
                />
              ))}
            </div>
          )}
          <div className="s-more">
            <button>Load 88 more projects →</button>
          </div>
        </section>

        {/* CONTRIBUTORS */}
        <section className="s-section" id="crew">
          <div className="s-section-h">
            <h2 className="s-section-title">Made by <em>humans</em>.</h2>
            <div className="s-section-side">241 contributors so far. PRs welcome. Add your own beginner project.</div>
          </div>
          <div className="s-contributors">
            <div className="s-contrib lead">
              <div className="s-avatar">{window.PBP_CONTRIBUTORS[0].name[0]}</div>
              <div className="s-cname">{window.PBP_CONTRIBUTORS[0].name}</div>
              <div className="s-chandle">@{window.PBP_CONTRIBUTORS[0].handle}</div>
              <p className="s-quote">"I started this repo to learn Python myself. It turned into a place where 240+ people teach each other. Best happy accident I've ever shipped."</p>
              <div className="s-badge">Maintainer · 412 commits</div>
            </div>
            {window.PBP_CONTRIBUTORS.slice(1, 13).map(c => (
              <div key={c.handle} className="s-contrib">
                <div className="s-avatar">{c.name[0]}</div>
                <div className="s-cname">{c.name.split(' ')[0]}</div>
                <div className="s-chandle">@{c.handle.length > 12 ? c.handle.slice(0,12) + '…' : c.handle}</div>
                <div className="s-commits">{c.commits} ★</div>
              </div>
            ))}
          </div>
          <div className="s-more">
            <button>See all 241 contributors →</button>
          </div>
        </section>

        {/* CTA BANNER */}
        <section className="s-cta-banner">
          <div>
            <h2>Want to <em>contribute</em>?</h2>
            <p>Drop your own beginner project as a PR. One folder, one Python file, one README. We merge if it runs.</p>
            <div style={{display:'flex', gap: 12, marginTop: 16}}>
              <button className="s-btn-pri" style={{background:'var(--s-accent)'}}>Read the guide →</button>
            </div>
          </div>
          <div className="s-cta-banner-codes">
            <div className="s-cta-banner-code">
              <span>$</span>
              <span>git clone python-beginner-projects.git</span>
              <span className="copy">copy</span>
            </div>
            <div className="s-cta-banner-code">
              <span>$</span>
              <span>cd projects &amp;&amp; mkdir my-project</span>
              <span className="copy">copy</span>
            </div>
          </div>
        </section>

        <footer className="s-footer">
          <div>Built with <span className="s-heart">♥</span> &amp; the standard library · MIT licensed · Archived 2025</div>
          <div className="s-footer-links">
            <a>GitHub</a>
            <a>Issues</a>
            <a>Wiki</a>
            <a>Code of Conduct</a>
          </div>
        </footer>
      </div>

      {open && <ProjectModal p={open} onClose={() => setOpen(null)} isBm={bm.includes(open.id)} toggleBm={toggleBm} />}

      <TweaksPanel>
        <TweakSection label="Visuals" />
        <TweakColor label="Accent color" value={t.accent}
          options={['#ff7a59', '#3aa6ff', '#1cc97c', '#a55cff', '#ff4d8b', '#ffd166']}
          onChange={(v) => setTweak('accent', v)} />
        <TweakSelect label="Surface" value={t.surface}
          options={[
            { value: 'cream', label: 'Cream (default)' },
            { value: 'mint',  label: 'Mint' },
            { value: 'sky',   label: 'Sky' },
            { value: 'lilac', label: 'Lilac' },
          ]}
          onChange={(v) => setTweak('surface', v)} />

        <TweakSection label="Gallery" />
        <TweakRadio label="Layout" value={t.layout}
          options={['grid', 'list', 'masonry']}
          onChange={(v) => setTweak('layout', v)} />
        <TweakSelect label="Card density" value={t.cardStyle}
          options={[
            { value: 'minimal',  label: 'Minimal (compact list)' },
            { value: 'detailed', label: 'Detailed (default)' },
            { value: 'image',    label: 'Image-forward (banner)' },
          ]}
          onChange={(v) => setTweak('cardStyle', v)} />

        <TweakSection label="Typography" />
        <TweakSelect label="Headline font" value={t.fontDisplay}
          options={[
            { value: "'Fraunces', Georgia, serif",        label: 'Fraunces · editorial serif' },
            { value: "'DM Serif Display', Georgia, serif",label: 'DM Serif Display' },
            { value: "'Outfit', sans-serif",              label: 'Outfit · geometric sans' },
            { value: "'Space Grotesk', sans-serif",       label: 'Space Grotesk' },
            { value: "'Caveat', cursive",                 label: 'Caveat · handwritten' },
          ]}
          onChange={(v) => setTweak('fontDisplay', v)} />
        <TweakSelect label="Body font" value={t.fontBody}
          options={[
            { value: "'DM Sans', sans-serif",        label: 'DM Sans (default)' },
            { value: "'Inter', sans-serif",          label: 'Inter' },
            { value: "'Plus Jakarta Sans', sans-serif", label: 'Plus Jakarta Sans' },
            { value: "'Outfit', sans-serif",         label: 'Outfit' },
          ]}
          onChange={(v) => setTweak('fontBody', v)} />
      </TweaksPanel>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<StickerApp />);
