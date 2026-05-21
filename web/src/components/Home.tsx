"use client";

// pyBegin homepage — ported from the original sticker-app.jsx.
// The design-tweak panel is dropped; its defaults are now fixed in CSS.

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { Bookmark } from "lucide-react";
import StickerLogo from "./StickerLogo";
import ScribbleSvg from "./ScribbleSvg";
import HeroStickers from "./HeroStickers";
import ProjectCard from "./ProjectCard";
import ProjectModal from "./ProjectModal";
import SiteFooter from "./SiteFooter";
import { CATEGORIES, CONTRIBUTORS, PATHS, PROJECTS, REPO_URL, getProject } from "@/lib/data";
import { getBookmarks, toggleBookmark } from "@/lib/bookmarks";
import contributors from "@/lib/contributors.json";
import type { Project, RepoContributor } from "@/types";

const CREW = contributors as RepoContributor[];

// Resolve a handle to its GitHub avatar. Uses the direct avatars.github URL
// (not github.com/<handle>.png — that 302-redirects and the redirect is
// blocked by the site's COEP: require-corp header).
const AVATARS = new Map(
  contributors.map((c) => [c.handle.toLowerCase(), c.avatar]),
);
const avatarFor = (handle: string, size: number) => {
  const url = AVATARS.get(handle.toLowerCase());
  return url ? `${url}&s=${size}` : `https://github.com/${handle}.png`;
};

const ACCENT = "#ff7a59";
const SORTS = ["default", "alpha", "short", "bookmarks"] as const;
type Sort = (typeof SORTS)[number];

function scrollTo(id: string) {
  document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
}

export default function Home() {
  const [search, setSearch] = useState("");
  const [cat, setCat] = useState("all");
  const [bm, setBm] = useState<string[]>([]);
  const [sort, setSort] = useState<Sort>("default");
  const [open, setOpen] = useState<Project | null>(null);
  const [showBmOnly, setShowBmOnly] = useState(false);

  // Bookmarks load client-side only — keeps SSR/hydration consistent.
  useEffect(() => setBm(getBookmarks()), []);

  const toggleBm = (id: string) => setBm(toggleBookmark(id));

  const filtered = useMemo(() => {
    let arr = PROJECTS.filter((p) => {
      if (showBmOnly && !bm.includes(p.id)) return false;
      if (cat !== "all" && p.cat !== cat) return false;
      if (search) {
        const q = search.toLowerCase();
        return (
          p.name.toLowerCase().includes(q) ||
          p.blurb.toLowerCase().includes(q) ||
          p.deps.toLowerCase().includes(q)
        );
      }
      return true;
    });
    if (sort === "alpha") arr = [...arr].sort((a, b) => a.name.localeCompare(b.name));
    if (sort === "short") arr = [...arr].sort((a, b) => a.lines - b.lines);
    if (sort === "bookmarks")
      arr = [...arr].sort(
        (a, b) => (bm.includes(b.id) ? 1 : 0) - (bm.includes(a.id) ? 1 : 0),
      );
    return arr;
  }, [search, cat, bm, sort, showBmOnly]);

  return (
    <div>
      <div className="s-shell">
        {/* NAV */}
        <nav className="s-nav">
          <Link className="s-logo" href="/">
            <div className="s-logomark">
              <StickerLogo />
            </div>
            <div>
              <div className="s-brand-name">pyBegin</div>
              <div className="s-brand-sub">250+ projects · 1 weekend each</div>
            </div>
          </Link>
          <div className="s-navlinks">
            <button className="active">Home</button>
            <button onClick={() => scrollTo("gallery")}>Projects</button>
            <button onClick={() => scrollTo("paths")}>Learn</button>
            <Link href="/playground">Playground</Link>
            <button onClick={() => scrollTo("crew")}>Contribute</button>
          </div>
          <div className="s-nav-right">
            <button
              type="button"
              className={`s-bm-btn${showBmOnly ? " active" : ""}`}
              aria-pressed={showBmOnly}
              title={
                showBmOnly
                  ? "Showing saved projects — click to show all"
                  : "Show your saved projects"
              }
              onClick={() => {
                setShowBmOnly((v) => !v);
                scrollTo("gallery");
              }}
            >
              <Bookmark
                size={15}
                strokeWidth={2.5}
                fill={bm.length ? "currentColor" : "none"}
                aria-hidden="true"
              />
              <span className="s-bm-n">{bm.length}</span>
              <span className="s-bm-word">saved</span>
            </button>
            <a className="s-cta" href={REPO_URL} target="_blank" rel="noreferrer">
              ★ Star · 2.3k
            </a>
          </div>
        </nav>

        {/* HERO */}
        <section className="s-hero">
          <div>
            <div className="s-tag">
              <span className="dot" />
              Live · 250+ projects from 241 humans
            </div>
            <h1 className="s-headline">
              Python
              <br />
              that{" "}
              <span className="scribble">
                feels good
                <ScribbleSvg color={ACCENT} />
              </span>
              <br />
              to type.
            </h1>
            <p className="s-sub">
              A scrappy collection of tiny Python projects. Each one is small
              enough to read in a coffee break and big enough to teach you
              something real. Pick a vibe. Type it out. Run it.
            </p>
            <div className="s-hero-cta">
              <Link className="s-btn-pri" href="/playground">
                <span>🚀</span> Open the playground
              </Link>
              <button
                className="s-btn-sec"
                onClick={() => scrollTo("gallery")}
              >
                Browse all →
              </button>
            </div>
          </div>
          <HeroStickers />
        </section>

        {/* STATS */}
        <div className="s-stats">
          <div className="s-stat">
            <div className="s-stat-n">250+</div>
            <div className="s-stat-l">Projects</div>
          </div>
          <div className="s-stat">
            <div className="s-stat-n">241</div>
            <div className="s-stat-l">Contributors</div>
          </div>
          <div className="s-stat">
            <div className="s-stat-n">2.3k</div>
            <div className="s-stat-l">★ Stars</div>
          </div>
          <div className="s-stat">
            <div className="s-stat-n">903</div>
            <div className="s-stat-l">Forks</div>
          </div>
        </div>

        {/* PATHS */}
        <section className="s-section" id="paths">
          <div className="s-section-h">
            <h2 className="s-section-title">
              Three <em>paths</em> in.
            </h2>
            <div className="s-section-side">
              Not sure where to start? Each path is three projects, building on
              each other. Finish one in a weekend.
            </div>
          </div>
          <div className="s-paths">
            {PATHS.map((p, idx) => (
              <div key={p.id} className="s-path">
                <div className="s-path-head">
                  <div className="s-path-tag">{p.tag.toUpperCase()}</div>
                  <div className="s-path-num">0{idx + 1}</div>
                </div>
                <h3 className="s-path-name">{p.name}</h3>
                <p className="s-path-desc">{p.desc}</p>
                <div className="s-path-list">
                  {p.items.map((id, i) => {
                    const pr = getProject(id);
                    return (
                      pr && (
                        <button
                          key={id}
                          className="s-path-item"
                          onClick={() => setOpen(pr)}
                        >
                          <i>0{i + 1}</i>
                          <span style={{ flex: 1 }}>{pr.name}</span>
                          <span className="em">{pr.emoji}</span>
                        </button>
                      )
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
            <h2 className="s-section-title">
              All the <em>projects</em>.
            </h2>
            <div className="s-section-side">
              {filtered.length} of {PROJECTS.length} shown · {bm.length}{" "}
              bookmarked
            </div>
          </div>
          <div className="s-toolbar">
            <div className="s-search">
              <span className="s-search-icon">🔍</span>
              <input
                placeholder="What do you want to build?"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                aria-label="Search projects"
              />
              {search && (
                <span
                  style={{ cursor: "pointer", opacity: 0.5 }}
                  onClick={() => setSearch("")}
                >
                  ✕
                </span>
              )}
            </div>
            <button
              className="s-sort"
              onClick={() =>
                setSort(SORTS[(SORTS.indexOf(sort) + 1) % SORTS.length])
              }
            >
              <span>↕</span>{" "}
              {sort === "default"
                ? "Featured"
                : sort === "alpha"
                  ? "A → Z"
                  : sort === "short"
                    ? "Shortest first"
                    : "★ Bookmarked first"}
            </button>
          </div>
          <div className="s-chips">
            {CATEGORIES.map((c) => (
              <button
                key={c.id}
                className={`s-chip ${
                  c.id === cat && !showBmOnly ? "active" : ""
                }`}
                onClick={() => {
                  setCat(c.id);
                  setShowBmOnly(false);
                }}
              >
                {c.name} <span className="ct">{c.count}</span>
              </button>
            ))}
            {bm.length > 0 && (
              <button
                className={`s-chip bm ${showBmOnly ? "active" : ""}`}
                onClick={() => setShowBmOnly((v) => !v)}
              >
                <span className="ic">★</span> Bookmarked{" "}
                <span className="ct">{bm.length}</span>
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
            <div className="s-gallery grid">
              {filtered.map((p) => (
                <ProjectCard
                  key={p.id}
                  p={p}
                  isBm={bm.includes(p.id)}
                  toggleBm={toggleBm}
                  onOpen={setOpen}
                />
              ))}
            </div>
          )}
          <div className="s-more">
            <a href={REPO_URL}>Browse all 250+ on GitHub →</a>
          </div>
        </section>

        {/* CONTRIBUTORS */}
        <section className="s-section" id="crew">
          <div className="s-section-h">
            <h2 className="s-section-title">
              Made by <em>humans</em>.
            </h2>
            <div className="s-section-side">
              241 contributors so far. PRs welcome. Add your own beginner
              project.
            </div>
          </div>
          <div className="s-contributors">
            <div className="s-contrib lead">
              <img
                className="s-avatar"
                src={avatarFor(CONTRIBUTORS[0].handle, 200)}
                alt=""
                width={84}
                height={84}
              />
              <div className="s-cname">{CONTRIBUTORS[0].name}</div>
              <div className="s-chandle">@{CONTRIBUTORS[0].handle}</div>
              <p className="s-quote">
                &ldquo;I started this repo to learn Python myself. It turned
                into a place where 240+ people teach each other. Best happy
                accident I&rsquo;ve ever shipped.&rdquo;
              </p>
              <div className="s-badge">Maintainer · 412 commits</div>
            </div>
            {CREW.slice(1, 31).map((c) => (
              <a
                key={c.handle}
                className="s-contrib"
                href={`https://github.com/${c.handle}`}
                target="_blank"
                rel="noreferrer"
              >
                <img
                  className="s-avatar"
                  src={`${c.avatar}&s=120`}
                  alt=""
                  width={56}
                  height={56}
                  loading="lazy"
                />
                <div className="s-cname">{c.name.split(" ")[0]}</div>
                <div className="s-chandle">
                  @
                  {c.handle.length > 12
                    ? c.handle.slice(0, 12) + "…"
                    : c.handle}
                </div>
              </a>
            ))}
          </div>
          <div className="s-more">
            <Link href="/contributors">See all contributors →</Link>
          </div>
        </section>

        {/* CTA BANNER */}
        <section className="s-cta-banner">
          <div>
            <h2>
              Want to <em>contribute</em>?
            </h2>
            <p>
              Drop your own beginner project as a PR. One folder, one Python
              file, one README. We merge if it runs.
            </p>
            <div style={{ display: "flex", gap: 12, marginTop: 16 }}>
              <a
                className="s-btn-pri"
                style={{ background: "var(--s-accent)" }}
                href={`${REPO_URL}/blob/main/CONTRIBUTING.md`}
              >
                Read the guide →
              </a>
            </div>
          </div>
          <div className="s-cta-banner-codes">
            <div className="s-cta-banner-code">
              <span>$</span>
              <span>git clone python-beginner-projects.git</span>
            </div>
            <div className="s-cta-banner-code">
              <span>$</span>
              <span>cd projects &amp;&amp; mkdir my-project</span>
            </div>
          </div>
        </section>

        <SiteFooter />
      </div>

      {open && (
        <ProjectModal
          p={open}
          onClose={() => setOpen(null)}
          isBm={bm.includes(open.id)}
          toggleBm={toggleBm}
        />
      )}
    </div>
  );
}
