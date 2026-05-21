// Client wrapper around the Cloudflare Workers Python backend ("Try it").
//
// Base URL comes from NEXT_PUBLIC_API_BASE (set in .env.production). Leave it
// empty for same-origin local dev.

const BASE = process.env.NEXT_PUBLIC_API_BASE || "";

export interface SelectOption {
  value: string | number;
  label: string;
}

export interface InputField {
  key: string;
  label: string;
  type: "select" | "number" | "text";
  options?: Array<string | SelectOption>;
  step?: number;
  min?: number;
  max?: number;
  default: string | number;
}

interface RunnableConfig {
  endpoint: string;
  inputs?: InputField[];
  interactive?: "tictactoe" | "hangman";
}

const RUNNABLE: Record<string, RunnableConfig> = {
  rps: {
    endpoint: "/api/rps",
    inputs: [
      { key: "choice", label: "Your throw", type: "select", options: ["rock", "paper", "scissors"], default: "rock" },
    ],
  },
  bmi: {
    endpoint: "/api/bmi",
    inputs: [
      { key: "height_m", label: "Height (m)", type: "number", step: 0.01, min: 0.5, max: 2.5, default: 1.75 },
      { key: "weight_kg", label: "Weight (kg)", type: "number", step: 0.1, min: 10, max: 400, default: 70 },
    ],
  },
  qr: {
    endpoint: "/api/qr",
    inputs: [
      { key: "text", label: "Text or URL", type: "text", default: "https://github.com/Mrinank-Bhowmick/python-beginner-projects" },
    ],
  },
  madlibs: {
    endpoint: "/api/madlibs",
    inputs: [
      {
        key: "story",
        label: "Story",
        type: "select",
        options: [
          { value: 1, label: "1 · Mystical land" },
          { value: 2, label: "2 · Wizard academy" },
          { value: 3, label: "3 · Time machine" },
        ],
        default: 1,
      },
      { key: "adjective", label: "Adjective", type: "text", default: "sparkly" },
      { key: "noun", label: "Noun", type: "text", default: "penguin" },
      { key: "verb", label: "Verb", type: "text", default: "dancing" },
      { key: "adverb", label: "Adverb", type: "text", default: "wildly" },
    ],
  },
  tictactoe: { endpoint: "/api/tictactoe", interactive: "tictactoe" },
  hangman: { endpoint: "/api/hangman", interactive: "hangman" },
};

export async function call<T = Record<string, unknown>>(
  id: string,
  payload?: Record<string, unknown>,
): Promise<T> {
  const cfg = RUNNABLE[id];
  if (!cfg) throw new Error("Not runnable: " + id);
  const res = await fetch(BASE + cfg.endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload || {}),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || "HTTP " + res.status);
  return data as T;
}

export function defaults(id: string): Record<string, string | number> {
  const cfg = RUNNABLE[id];
  if (!cfg || !cfg.inputs) return {};
  const out: Record<string, string | number> = {};
  for (const f of cfg.inputs) out[f.key] = f.default;
  return out;
}

export function isRunnable(id: string): boolean {
  return !!RUNNABLE[id];
}

export function isInteractive(id: string): boolean {
  return !!RUNNABLE[id]?.interactive;
}

export function inputsFor(id: string): InputField[] {
  return RUNNABLE[id]?.inputs || [];
}
