"use client";

// Playground sidebar — lists every project in the repo, searchable.
// Projects are split into two collapsible groups:
//   • Runnable    → open live in the in-browser playground
//   • Desktop     → can't run in-browser; link to the project's detail page
// Collapse state is persisted to localStorage; an active search force-opens
// every group so matches stay visible.

import { useEffect, useState, type CSSProperties } from "react";
import Link from "next/link";
import { Search, X, PanelLeftClose, PanelLeftOpen } from "lucide-react";
import { CATALOG } from "@/lib/catalog";
import ResizeHandle from "./ResizeHandle";

const SIDE_MIN = 210;
const SIDE_MAX = 520;

interface SideItem {
  id: string;
  name: string;
  emoji: string;
  href: string;
  runnable: boolean;
}

const RUNNABLE_ITEMS: SideItem[] = CATALOG.filter((p) => p.hasPlayground).map(
  (p) => ({
    id: p.id,
    name: p.name,
    emoji: p.emoji,
    href: `/playground/${p.id}`,
    runnable: true,
  }),
);

const DESKTOP_ITEMS: SideItem[] = CATALOG.filter((p) => !p.hasPlayground).map(
  (p) => ({
    id: p.id,
    name: p.name,
    emoji: p.emoji,
    href: `/projects/${p.id}`,
    runnable: false,
  }),
);

const GROUPS: { id: string; label: string; items: SideItem[] }[] = [
  {
    id: "scratch",
    label: "Scratchpad",
    items: [
      {
        id: "scratch",
        name: "Blank scratchpad",
        emoji: "✏️",
        href: "/playground",
        runnable: true,
      },
    ],
  },
  { id: "runnable", label: "Runnable in browser", items: RUNNABLE_ITEMS },
  { id: "desktop", label: "Desktop projects", items: DESKTOP_ITEMS },
];

function Chevron() {
  return (
    <svg className="chev" viewBox="0 0 12 12" fill="none" aria-hidden="true">
      <path
        d="M3 4.5L6 7.5L9 4.5"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export default function PlaygroundSidebar({
  activeId = "scratch",
}: {
  activeId?: string;
}) {
  const [q, setQ] = useState("");
  // Desktop group is huge — start it collapsed unless the user changed it.
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({
    desktop: true,
  });
  // Whole-sidebar collapse — folds the panel down to a slim rail.
  const [railed, setRailed] = useState(false);
  // User-draggable sidebar width — resets to the default on every refresh.
  const [width, setWidth] = useState(280);

  useEffect(() => {
    try {
      const saved = localStorage.getItem("pg_collapsed_v2");
      if (saved) setCollapsed(JSON.parse(saved));
      setRailed(localStorage.getItem("pg_side_railed") === "1");
    } catch {
      /* ignore */
    }
  }, []);

  const setRail = (v: boolean) => {
    setRailed(v);
    try {
      localStorage.setItem("pg_side_railed", v ? "1" : "0");
    } catch {
      /* ignore */
    }
  };

  if (railed) {
    return (
      <aside className="pg-side railed">
        <button
          className="pg-side-expand"
          onClick={() => setRail(false)}
          title="Show project list"
          aria-label="Show project list"
        >
          <PanelLeftOpen size={18} strokeWidth={2.25} />
        </button>
        <span className="pg-side-rail-label">Projects</span>
      </aside>
    );
  }

  const toggle = (gid: string) =>
    setCollapsed((prev) => {
      const next = { ...prev, [gid]: !prev[gid] };
      try {
        localStorage.setItem("pg_collapsed_v2", JSON.stringify(next));
      } catch {
        /* ignore */
      }
      return next;
    });

  const matches = (it: SideItem) =>
    !q || it.name.toLowerCase().includes(q.toLowerCase());

  return (
    <aside
      className="pg-side"
      style={{ ["--pg-side-w"]: `${width}px` } as CSSProperties}
    >
      <div className="pg-side-head">
        <div className="pg-side-head-text">
          <div className="pg-side-title">Playground</div>
          <div className="pg-side-sub">
            {CATALOG.length} projects · {RUNNABLE_ITEMS.length} runnable
          </div>
        </div>
        <button
          className="pg-side-collapse"
          onClick={() => setRail(true)}
          title="Hide project list"
          aria-label="Hide project list"
        >
          <PanelLeftClose size={16} strokeWidth={2.25} />
        </button>
      </div>
      <div className="pg-side-search">
        <Search size={14} strokeWidth={2.25} aria-hidden="true" />
        <input
          placeholder="Search all projects…"
          value={q}
          onChange={(e) => setQ(e.target.value)}
          aria-label="Search playground projects"
        />
        {q && (
          <button
            type="button"
            className="pg-side-search-clear"
            onClick={() => setQ("")}
            aria-label="Clear search"
          >
            <X size={14} strokeWidth={2.5} />
          </button>
        )}
      </div>
      <div className="pg-side-list">
        {GROUPS.map((g) => {
          const items = g.items.filter(matches);
          if (items.length === 0) return null;
          const isCollapsed = !q && !!collapsed[g.id];
          return (
            <div
              key={g.id}
              className={`pg-group ${isCollapsed ? "collapsed" : ""}`}
            >
              <button
                className="pg-group-h"
                onClick={() => toggle(g.id)}
                aria-expanded={!isCollapsed}
              >
                <Chevron />
                <span className="label">{g.label}</span>
                <span className="ct">{items.length}</span>
              </button>
              <div
                className="pg-group-items"
                style={{ maxHeight: isCollapsed ? 0 : items.length * 42 + 8 }}
              >
                {items.map((it) => (
                  <Link
                    key={it.id}
                    href={it.href}
                    className={`pg-item ${it.id === activeId ? "active" : ""}`}
                  >
                    <span className="em">{it.emoji}</span>
                    <span className="nm">{it.name}</span>
                    {it.runnable && it.id !== "scratch" && (
                      <span
                        className="pg-run-dot"
                        title="Runs in the browser"
                        aria-label="Runnable"
                      />
                    )}
                  </Link>
                ))}
              </div>
            </div>
          );
        })}
      </div>
      <div className="pg-side-foot">
        <span className="dot" />
        <span>Pyodide · CPython 3.x</span>
      </div>
      <ResizeHandle
        orientation="x"
        className="pg-side-resize"
        ariaLabel="Resize sidebar"
        onResize={(dx) =>
          setWidth((w) => Math.max(SIDE_MIN, Math.min(SIDE_MAX, w + dx)))
        }
      />
    </aside>
  );
}
