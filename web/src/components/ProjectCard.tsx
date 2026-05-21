"use client";

import type { Project } from "@/types";
import RunnableBadge from "./RunnableBadge";

export default function ProjectCard({
  p,
  isBm,
  toggleBm,
  onOpen,
}: {
  p: Project;
  isBm: boolean;
  toggleBm: (id: string) => void;
  onOpen: (p: Project) => void;
}) {
  return (
    <div className="s-card" onClick={() => onOpen(p)}>
      <div className="s-card-emoji">{p.emoji}</div>
      <div className="s-card-h">
        <h3 className="s-card-name">{p.name}</h3>
        <button
          className={`s-card-bm ${isBm ? "on" : ""}`}
          onClick={(e) => {
            e.stopPropagation();
            toggleBm(p.id);
          }}
          aria-label={isBm ? "Remove bookmark" : "Add bookmark"}
        >
          {isBm ? "★" : "☆"}
        </button>
      </div>
      <p className="s-card-blurb">{p.blurb}</p>
      <div className="s-card-meta">
        <span className="s-meta-pill">{p.lines} lines</span>
        <span className="s-meta-pill dep">{p.deps}</span>
        {p.playground && <RunnableBadge size="sm" />}
      </div>
    </div>
  );
}
