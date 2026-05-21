"use client";

// A draggable splitter bar. Reports the pointer delta (in px) on every move so
// the parent can grow/shrink whatever panel sits next to it. Pointer capture
// keeps the drag alive even when the cursor outruns the thin bar. Arrow keys
// nudge it too, so the splitter is keyboard-accessible.

import { useState } from "react";

export default function ResizeHandle({
  orientation,
  onResize,
  className = "",
  ariaLabel,
}: {
  /** "x" = drag left/right (col-resize), "y" = drag up/down (row-resize). */
  orientation: "x" | "y";
  /** Called with the pixel delta since the last move. */
  onResize: (delta: number) => void;
  className?: string;
  ariaLabel?: string;
}) {
  const [dragging, setDragging] = useState(false);

  return (
    <div
      role="separator"
      aria-orientation={orientation === "x" ? "vertical" : "horizontal"}
      aria-label={ariaLabel}
      tabIndex={0}
      className={`pg-resize pg-resize-${orientation}${
        dragging ? " dragging" : ""
      } ${className}`}
      data-last="0"
      onPointerDown={(e) => {
        e.preventDefault();
        const el = e.currentTarget;
        el.setPointerCapture(e.pointerId);
        el.dataset.last = String(orientation === "x" ? e.clientX : e.clientY);
        setDragging(true);
      }}
      onPointerMove={(e) => {
        const el = e.currentTarget;
        if (!el.hasPointerCapture(e.pointerId)) return;
        const pos = orientation === "x" ? e.clientX : e.clientY;
        const delta = pos - Number(el.dataset.last);
        if (delta !== 0) {
          el.dataset.last = String(pos);
          onResize(delta);
        }
      }}
      onPointerUp={(e) => {
        e.currentTarget.releasePointerCapture(e.pointerId);
        setDragging(false);
      }}
      onKeyDown={(e) => {
        const step = e.shiftKey ? 48 : 16;
        const back = orientation === "x" ? "ArrowLeft" : "ArrowUp";
        const fwd = orientation === "x" ? "ArrowRight" : "ArrowDown";
        if (e.key === back) {
          e.preventDefault();
          onResize(-step);
        } else if (e.key === fwd) {
          e.preventDefault();
          onResize(step);
        }
      }}
    >
      <span className="pg-resize-grip" aria-hidden="true" />
    </div>
  );
}
