"use client";

import { useEffect } from "react";
import Link from "next/link";
import ProjectCredit from "./ProjectCredit";
import RunnableBadge from "./RunnableBadge";
import { REPO_URL } from "@/lib/data";
import type { Project } from "@/types";

export default function ProjectModal({
  p,
  onClose,
  isBm,
  toggleBm,
}: {
  p: Project;
  onClose: () => void;
  isBm: boolean;
  toggleBm: (id: string) => void;
}) {
  useEffect(() => {
    const k = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", k);
    return () => window.removeEventListener("keydown", k);
  }, [onClose]);

  return (
    <div className="s-modal-bg" onClick={onClose}>
      <div
        className="s-modal"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-label={p.name}
      >
        <button className="s-modal-x" onClick={onClose} aria-label="Close">
          ✕
        </button>
        <div className="s-modal-emoji">{p.emoji}</div>
        <h2>{p.name}</h2>
        <p className="s-modal-blurb">{p.blurb}</p>
        <div className="s-modal-meta">
          <span className="s-meta-pill">{p.lines} lines</span>
          <span className="s-meta-pill dep">{p.deps}</span>
          <span className="s-meta-pill dep">{p.cat}</span>
          {p.playground && <RunnableBadge size="sm" />}
        </div>
        <ProjectCredit author={p.author} />
        <div className="s-modal-code">
          <div style={{ color: "var(--s-accent)" }}>
            $ git clone python-beginner-projects.git
          </div>
          <div style={{ color: "rgba(254,249,239,0.6)" }}>
            $ cd projects/{p.id}
          </div>
          <div>$ python {p.id}.py</div>
        </div>
        <div className="s-modal-actions">
          {p.playground && (
            <Link className="s-btn-pri" href={`/playground/${p.id}`}>
              ▶ Open in playground
            </Link>
          )}
          <Link className="s-btn-sec" href={`/projects/${p.id}`}>
            Full details →
          </Link>
          <button
            className="s-btn-sec"
            onClick={() => toggleBm(p.id)}
          >
            {isBm ? "★ Bookmarked" : "☆ Bookmark"}
          </button>
          <a
            className="s-btn-sec"
            href={REPO_URL}
            target="_blank"
            rel="noreferrer"
          >
            GitHub →
          </a>
        </div>
      </div>
    </div>
  );
}
