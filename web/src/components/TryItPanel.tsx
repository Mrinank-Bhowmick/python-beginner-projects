"use client";

// Try It — live demo panel for the runnable projects. Renders a simple input
// form for stateless projects (rps, bmi, qr, madlibs) and dedicated widgets
// for the turn-based ones (tictactoe, hangman). All POSTs go to the
// Cloudflare Worker backend.

import { useEffect, useState } from "react";
import {
  call,
  defaults,
  inputsFor,
  isInteractive,
  type InputField,
  type SelectOption,
} from "@/lib/api";
import type { Project } from "@/types";

export default function TryItPanel({ project }: { project: Project }) {
  if (isInteractive(project.id)) {
    if (project.id === "tictactoe") return <TicTacToePlay />;
    if (project.id === "hangman") return <HangmanPlay />;
  }
  return <SimpleRunner project={project} />;
}

function castOption(field: InputField, raw: string): string | number {
  const opts = field.options;
  if (opts && opts.length && typeof opts[0] === "object") {
    const match = (opts as SelectOption[]).find((o) => String(o.value) === raw);
    return match ? match.value : raw;
  }
  return raw;
}

type FormState = Record<string, string | number>;

function SimpleRunner({ project }: { project: Project }) {
  const fields = inputsFor(project.id);
  const [form, setForm] = useState<FormState>(() => defaults(project.id));
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [out, setOut] = useState<Record<string, unknown> | null>(null);

  const run = async () => {
    setError(null);
    setLoading(true);
    try {
      const res = await call<Record<string, unknown>>(project.id, form);
      setOut(res);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
      setOut(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="s-try">
      <div className="s-try-h">▶ Try it live</div>
      <div className="s-try-form">
        {fields.map((f) => (
          <label key={f.key} className="s-try-field">
            <span>{f.label}</span>
            {f.type === "select" ? (
              <select
                value={String(form[f.key])}
                onChange={(e) =>
                  setForm({ ...form, [f.key]: castOption(f, e.target.value) })
                }
              >
                {(f.options || []).map((opt) => {
                  const v = typeof opt === "object" ? opt.value : opt;
                  const l = typeof opt === "object" ? opt.label : opt;
                  return (
                    <option key={String(v)} value={String(v)}>
                      {l}
                    </option>
                  );
                })}
              </select>
            ) : f.type === "number" ? (
              <input
                type="number"
                step={f.step}
                min={f.min}
                max={f.max}
                value={form[f.key]}
                onChange={(e) =>
                  setForm({
                    ...form,
                    [f.key]: e.target.value === "" ? "" : Number(e.target.value),
                  })
                }
              />
            ) : (
              <input
                type="text"
                value={form[f.key] ?? ""}
                onChange={(e) => setForm({ ...form, [f.key]: e.target.value })}
              />
            )}
          </label>
        ))}
      </div>
      <button
        className="s-btn-pri s-try-run"
        onClick={run}
        disabled={loading}
      >
        {loading ? "Running…" : "Run"}
      </button>
      {error && <div className="s-try-error">⚠ {error}</div>}
      {out && <SimpleOutput projectId={project.id} out={out} />}
    </div>
  );
}

function SimpleOutput({
  projectId,
  out,
}: {
  projectId: string;
  out: Record<string, unknown>;
}) {
  if (projectId === "qr" && out.png_b64) {
    return (
      <div className="s-try-out">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          alt="Generated QR code"
          src={`data:image/png;base64,${out.png_b64}`}
          style={{
            width: 220,
            height: 220,
            imageRendering: "pixelated",
            borderRadius: 12,
            background: "#fff",
            padding: 8,
          }}
        />
      </div>
    );
  }
  if (projectId === "bmi") {
    return (
      <div className="s-try-out">
        <div style={{ fontSize: 32, fontWeight: 800 }}>{String(out.bmi)}</div>
        <div style={{ opacity: 0.8 }}>{String(out.category)}</div>
      </div>
    );
  }
  if (projectId === "rps") {
    const verdict =
      ({ win: "🎉 You win", lose: "😅 You lose", draw: "🤝 Draw" } as Record<
        string,
        string
      >)[String(out.result)] || String(out.result);
    return (
      <div className="s-try-out">
        <div>
          You: <b>{String(out.player)}</b> · CPU: <b>{String(out.cpu)}</b>
        </div>
        <div style={{ fontSize: 20, fontWeight: 700, marginTop: 4 }}>
          {verdict}
        </div>
      </div>
    );
  }
  if (projectId === "madlibs") {
    return (
      <div className="s-try-out s-try-story">
        <pre>{String(out.story)}</pre>
      </div>
    );
  }
  return <pre className="s-try-out">{JSON.stringify(out, null, 2)}</pre>;
}

// ---- Tic-Tac-Toe ----

const EMPTY_BOARD = ["", "", "", "", "", "", "", "", ""];

interface TttResponse {
  board: string[];
  status: "ongoing" | "win" | "draw";
  winner?: string;
}

function TicTacToePlay() {
  const [board, setBoard] = useState<string[]>(EMPTY_BOARD);
  const [status, setStatus] = useState<TttResponse["status"]>("ongoing");
  const [winner, setWinner] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const reset = () => {
    setBoard(EMPTY_BOARD);
    setStatus("ongoing");
    setWinner(null);
    setError(null);
  };

  const play = async (idx: number) => {
    if (board[idx] || status !== "ongoing" || loading) return;
    setError(null);
    setLoading(true);
    try {
      const res = await call<TttResponse>("tictactoe", {
        board,
        player: "X",
        move: idx,
      });
      setBoard(res.board);
      setStatus(res.status);
      setWinner(res.winner || null);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setLoading(false);
    }
  };

  const headline =
    status === "win"
      ? winner === "X"
        ? "🎉 You win"
        : "🤖 CPU wins"
      : status === "draw"
        ? "🤝 Draw"
        : "Your move (X)";

  return (
    <div className="s-try">
      <div className="s-try-h">▶ Try it live · vs the bot</div>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          marginBottom: 10,
        }}
      >
        <div style={{ fontWeight: 700 }}>{headline}</div>
        <button
          className="s-btn-sec"
          onClick={reset}
          style={{ padding: "6px 14px", fontSize: 13 }}
        >
          Reset
        </button>
      </div>
      <div className="s-ttt-grid">
        {board.map((cell, i) => (
          <button
            key={i}
            className="s-ttt-cell"
            onClick={() => play(i)}
            disabled={!!cell || status !== "ongoing" || loading}
          >
            <span data-mark={cell}>{cell}</span>
          </button>
        ))}
      </div>
      {error && <div className="s-try-error">⚠ {error}</div>}
    </div>
  );
}

// ---- Hangman ----

const ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

interface HangmanState {
  mask: string;
  wrong: string[];
  tries_left: number;
  max_tries: number;
  status: "ongoing" | "win" | "lose";
  word_length: number;
  word?: string;
}

function HangmanPlay() {
  const [seed, setSeed] = useState(() => Math.floor(Math.random() * 1e9));
  const [difficulty, setDifficulty] = useState("medium");
  const [guessed, setGuessed] = useState<string[]>([]);
  const [state, setState] = useState<HangmanState | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const refresh = async (
    nextGuessed: string[],
    nextDifficulty = difficulty,
    nextSeed = seed,
  ) => {
    setError(null);
    setLoading(true);
    try {
      const res = await call<HangmanState>("hangman", {
        word_seed: nextSeed,
        guessed: nextGuessed,
        difficulty: nextDifficulty,
      });
      setState(res);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    refresh([], difficulty, seed);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const guess = (letter: string) => {
    if (loading || !state || state.status !== "ongoing" || guessed.includes(letter))
      return;
    const next = [...guessed, letter];
    setGuessed(next);
    refresh(next);
  };

  const newWord = (nextDifficulty = difficulty) => {
    const s = Math.floor(Math.random() * 1e9);
    setSeed(s);
    setGuessed([]);
    setDifficulty(nextDifficulty);
    refresh([], nextDifficulty, s);
  };

  return (
    <div className="s-try">
      <div className="s-try-h">▶ Try it live · pick letters</div>
      <div className="s-hg-row">
        <label className="s-try-field" style={{ flex: "0 0 auto" }}>
          <span>Difficulty</span>
          <select
            value={difficulty}
            onChange={(e) => newWord(e.target.value)}
          >
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
        </label>
        <button
          className="s-btn-sec"
          onClick={() => newWord()}
          style={{ alignSelf: "end" }}
        >
          New word
        </button>
      </div>
      {state && (
        <>
          <div className="s-hg-word">
            {state.mask.split("").map((c, i) => (
              <span key={i} className="s-hg-slot">
                {c === "_" ? "·" : c}
              </span>
            ))}
          </div>
          <div className="s-hg-meta">
            <span>
              {state.tries_left} / {state.max_tries} tries left
            </span>
            <span className="s-hg-wrong">
              {state.wrong.length ? "wrong: " + state.wrong.join(" ") : ""}
            </span>
          </div>
          <div className="s-hg-keys">
            {ALPHABET.map((l) => {
              const used = guessed.includes(l);
              const hit = used && state.mask.includes(l);
              return (
                <button
                  key={l}
                  className={`s-hg-key ${used ? "used" : ""} ${
                    hit ? "hit" : used ? "miss" : ""
                  }`}
                  onClick={() => guess(l)}
                  disabled={used || state.status !== "ongoing" || loading}
                >
                  {l}
                </button>
              );
            })}
          </div>
          {state.status === "win" && (
            <div className="s-try-out">🎉 You got it!</div>
          )}
          {state.status === "lose" && (
            <div className="s-try-out">
              😅 Out of tries — the word was <b>{state.word}</b>
            </div>
          )}
        </>
      )}
      {error && <div className="s-try-error">⚠ {error}</div>}
    </div>
  );
}
