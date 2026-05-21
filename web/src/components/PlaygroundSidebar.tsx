"use client";

// Playground sidebar — searchable, with collapsible category groups
// (open by default, collapse state persisted to localStorage; an active
// search force-opens every group so matches stay visible).

import { useEffect, useState } from "react";
import Link from "next/link";
import { CATEGORIES, PROJECTS } from "@/lib/data";

const PLAYABLE = PROJECTS.filter((p) => p.playground);

interface SideItem {
  id: string;
  name: string;
  emoji: string;
  lines: number;
  href: string;
}

interface SideGroup {
  id: string;
  label: string;
  items: SideItem[];
}

const GROUPS: SideGroup[] = [
  {
    id: "scratch",
    label: "Scratchpad",
    items: [
      { id: "scratch", name: "Blank scratchpad", emoji: "✏️", lines: 9, href: "/playground" },
    ],
  },
  ...CATEGORIES.filter((c) => c.id !== "all")
    .map((c) => ({
      id: c.id,
      label: c.name,
      items: PLAYABLE.filter((p) => p.cat === c.id).map((p) => ({
        id: p.id,
        name: p.name,
        emoji: p.emoji,
        lines: p.lines,
        href: `/playground/${p.id}`,
      })),
    }))
    .filter((g) => g.items.length > 0),
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
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});

  // Load persisted collapse state once on mount.
  useEffect(() => {
    try {
      const saved = localStorage.getItem("pg_collapsed_v1");
      if (saved) setCollapsed(JSON.parse(saved));
    } catch {
      /* ignore */
    }
  }, []);

  const toggle = (gid: string) =>
    setCollapsed((prev) => {
      const next = { ...prev, [gid]: !prev[gid] };
      try {
        localStorage.setItem("pg_collapsed_v1", JSON.stringify(next));
      } catch {
        /* ignore */
      }
      return next;
    });

  const matches = (it: SideItem) =>
    !q || it.name.toLowerCase().includes(q.toLowerCase());

  return (
    <aside className="pg-side">
      <div className="pg-side-head">
        <div className="pg-side-title">Playground</div>
        <div className="pg-side-sub">
          {PLAYABLE.length} runnable · in-browser CPython
        </div>
      </div>
      <div className="pg-side-search">
        <span aria-hidden="true">🔍</span>
        <input
          placeholder="Filter projects…"
          value={q}
          onChange={(e) => setQ(e.target.value)}
          aria-label="Filter playground projects"
        />
        {q && (
          <span
            style={{ cursor: "pointer", opacity: 0.5 }}
            onClick={() => setQ("")}
          >
            ✕
          </span>
        )}
      </div>
      <div className="pg-side-list">
        {GROUPS.map((g) => {
          const items = g.items.filter(matches);
          if (items.length === 0) return null;
          const isCollapsed = !q && !!collapsed[g.id];
          return (
            <div key={g.id} className={`pg-group ${isCollapsed ? "collapsed" : ""}`}>
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
                style={{ maxHeight: isCollapsed ? 0 : items.length * 46 + 8 }}
              >
                {items.map((it) => (
                  <Link
                    key={it.id}
                    href={it.href}
                    className={`pg-item ${it.id === activeId ? "active" : ""}`}
                  >
                    <span className="em">{it.emoji}</span>
                    <span className="nm">{it.name}</span>
                    <span className="ln">{it.lines}ln</span>
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
    </aside>
  );
}
