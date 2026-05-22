"use client";

// Playground workspace — toolbar + editor window + console window.
// The console is a real xterm.js terminal: program output streams in and you
// type answers inline at the cursor. Execution runs in a Pyodide Web Worker
// (public/pyodide-worker.js); input() is bridged via a SharedArrayBuffer.
// The editor lints against Pyodide's compile() — real syntax-error squiggles.

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type CSSProperties,
} from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { linter, lintGutter, type Diagnostic } from "@codemirror/lint";
import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";
import {
  Play,
  Square,
  RotateCcw,
  BookOpen,
  PanelLeftClose,
  Check,
  Copy,
  Eraser,
  Code2,
  ArrowUpRight,
} from "lucide-react";
import { pybeginPaper } from "@/lib/cmTheme";
import ResizeHandle from "./ResizeHandle";

type Status = "idle" | "running" | "waiting" | "done" | "error";

interface LintErr {
  line: number;
  col: number;
  endLine: number;
  endCol: number;
  msg: string;
}

interface WorkerMessage {
  type:
    | "loading"
    | "ready"
    | "running"
    | "stdout"
    | "stderr"
    | "stdin"
    | "done"
    | "lint-result";
  text?: string;
  id?: number;
  errors?: LintErr[];
}

export interface PlaygroundProject {
  id: string;
  name: string;
  emoji: string;
  deps: string;
  lines: number;
  blurb: string;
  /** Contributor handle + link to the project's source folder on GitHub. */
  author?: string;
  folderUrl?: string;
}

const SAB_SIZE = 8 + 8192;

const STATUS_TEXT: Record<Status, string> = {
  idle: "Ready when you are",
  running: "Running…",
  waiting: "Waiting for your input",
  done: "Done · exited cleanly",
  error: "Error",
};

function WinDots() {
  return (
    <div className="dots" aria-hidden="true">
      <i />
      <i />
      <i />
    </div>
  );
}

const nl = (s: string) => s.replace(/\r?\n/g, "\r\n");

const clamp = (v: number, lo: number, hi: number) =>
  Math.max(lo, Math.min(hi, v));

// Stable empty-array default so the prop reference doesn't change each render.
const NO_PACKAGES: string[] = [];

export default function Playground({
  project,
  initialCode,
  packages = NO_PACKAGES,
  readmeHtml,
}: {
  project: PlaygroundProject;
  initialCode: string;
  packages?: string[];
  readmeHtml?: string | null;
}) {
  const [code, setCode] = useState(initialCode);
  const [status, setStatus] = useState<Status>("idle");
  const [copied, setCopied] = useState(false);
  const [readmeOpen, setReadmeOpen] = useState(true);

  // Resizable layout — README pane width (%) and editor/console height (%).
  const [readmePct, setReadmePct] = useState(38);
  const [editorPct, setEditorPct] = useState(58);
  const splitRef = useRef<HTMLDivElement | null>(null);
  const rightColRef = useRef<HTMLDivElement | null>(null);

  const workerRef = useRef<Worker | null>(null);
  const sabRef = useRef<SharedArrayBuffer | null>(null);

  const termHostRef = useRef<HTMLDivElement | null>(null);
  const termRef = useRef<Terminal | null>(null);
  const fitRef = useRef<FitAddon | null>(null);

  const runActiveRef = useRef(false); // a program is running
  const awaitingRef = useRef(false); // worker is blocked on input()
  const inputBufRef = useRef(""); // current line being typed in the terminal
  const queueRef = useRef<string[]>([]); // type-ahead lines

  const lintPending = useRef<Map<number, (e: LintErr[]) => void>>(new Map());
  const lintId = useRef(0);

  // --- push one typed line into the worker via the shared buffer ---
  const sendLine = useCallback((line: string) => {
    const sab = sabRef.current;
    if (!sab) return;
    const ctrl = new Int32Array(sab, 0, 2);
    const data = new Uint8Array(sab, 8);
    const enc = new TextEncoder().encode(line + "\n");
    const len = Math.min(enc.length, data.length);
    data.set(enc.subarray(0, len));
    Atomics.store(ctrl, 1, len);
    Atomics.store(ctrl, 0, 1);
    Atomics.notify(ctrl, 0);
  }, []);

  const handleMessage = useCallback(
    (msg: WorkerMessage) => {
      const term = termRef.current;
      // lint replies are handled any time; program output only during a run
      // (so the eager background boot doesn't write to the console).
      if (msg.type === "lint-result") {
        const resolve = lintPending.current.get(msg.id as number);
        if (resolve) {
          lintPending.current.delete(msg.id as number);
          resolve(msg.errors || []);
        }
        return;
      }
      if (!runActiveRef.current) return;
      switch (msg.type) {
        case "loading":
          setStatus("running");
          term?.writeln("\x1b[2;3m" + (msg.text || "Loading…") + "\x1b[0m");
          break;
        case "running":
          setStatus("running");
          break;
        case "stdout":
          term?.write(nl(msg.text || ""));
          break;
        case "stderr":
          setStatus("error");
          term?.write("\x1b[31m" + nl(msg.text || "") + "\x1b[0m");
          break;
        case "stdin":
          if (queueRef.current.length > 0) {
            sendLine(queueRef.current.shift() as string);
          } else {
            awaitingRef.current = true;
            setStatus("waiting");
          }
          break;
        case "done":
          runActiveRef.current = false;
          awaitingRef.current = false;
          setStatus((s) => (s === "error" ? "error" : "done"));
          term?.writeln("\x1b[2;3m\n— program finished —\x1b[0m");
          break;
      }
    },
    [sendLine],
  );

  const ensureWorker = useCallback((): Worker => {
    if (!workerRef.current) {
      const w = new Worker("/pyodide-worker.js");
      w.onmessage = (e: MessageEvent<WorkerMessage>) => handleMessage(e.data);
      workerRef.current = w;
    }
    return workerRef.current;
  }, [handleMessage]);

  // --- terminal setup ---
  useEffect(() => {
    if (!termHostRef.current) return;
    const term = new Terminal({
      fontFamily: "var(--font-mono), 'JetBrains Mono', ui-monospace, monospace",
      fontSize: 13,
      lineHeight: 1.4,
      cursorBlink: true,
      convertEol: true,
      theme: {
        background: "#fbf3e0",
        foreground: "#3b3155",
        cursor: "#ff7a59",
        cursorAccent: "#fbf3e0",
        selectionBackground: "#ff7a5940",
        black: "#3b3155",
        brightBlack: "#9c8eaf",
        red: "#c0392b",
        brightRed: "#c0392b",
        green: "#2a8c6e",
        brightGreen: "#2a8c6e",
        yellow: "#a85e1a",
        brightYellow: "#a85e1a",
        blue: "#3d6fb5",
        brightBlue: "#3d6fb5",
        magenta: "#c44a8a",
        brightMagenta: "#c44a8a",
        cyan: "#2a8c6e",
        brightCyan: "#2a8c6e",
        white: "#3b3155",
        brightWhite: "#3b3155",
      },
    });
    const fit = new FitAddon();
    term.loadAddon(fit);
    term.open(termHostRef.current);
    fit.fit();
    term.writeln(
      "\x1b[2;3m# Output appears here. Hit Run code to start.\x1b[0m",
    );

    term.onData((d) => {
      if (!runActiveRef.current) return;
      for (const ch of d) {
        if (ch === "\r") {
          term.write("\r\n");
          const line = inputBufRef.current;
          inputBufRef.current = "";
          if (awaitingRef.current) {
            awaitingRef.current = false;
            setStatus("running");
            sendLine(line);
          } else {
            queueRef.current.push(line);
          }
        } else if (ch === "\x7f") {
          if (inputBufRef.current.length) {
            inputBufRef.current = inputBufRef.current.slice(0, -1);
            term.write("\b \b");
          }
        } else if (ch >= " ") {
          inputBufRef.current += ch;
          term.write(ch);
        }
      }
    });

    termRef.current = term;
    fitRef.current = fit;

    const onResize = () => fit.fit();
    window.addEventListener("resize", onResize);
    const ro = new ResizeObserver(() => {
      try {
        fit.fit();
      } catch {
        /* not visible yet */
      }
    });
    ro.observe(termHostRef.current);

    return () => {
      window.removeEventListener("resize", onResize);
      ro.disconnect();
      term.dispose();
      termRef.current = null;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Start the worker eagerly — Pyodide loads in the background so the editor
  // can lint and the first Run is instant.
  useEffect(() => {
    ensureWorker();
    return () => {
      // Null the ref too — otherwise React StrictMode's mount/unmount/mount
      // cycle leaves a terminated worker in the ref and ensureWorker reuses it,
      // so the first Run posts to a dead worker and hangs on "Running…".
      workerRef.current?.terminate();
      workerRef.current = null;
    };
  }, [ensureWorker]);

  // --- editor lint: round-trip the source to the worker's compile() check ---
  const requestLint = useCallback(
    (src: string): Promise<LintErr[]> => {
      const worker = ensureWorker();
      return new Promise((resolve) => {
        const id = ++lintId.current;
        lintPending.current.set(id, resolve);
        worker.postMessage({ type: "lint", code: src, id });
        setTimeout(() => {
          if (lintPending.current.has(id)) {
            lintPending.current.delete(id);
            resolve([]);
          }
        }, 9000);
      });
    },
    [ensureWorker],
  );

  const cmExtensions = useMemo(() => {
    const pyLint = linter(
      async (view): Promise<Diagnostic[]> => {
        const src = view.state.doc.toString();
        const errors = await requestLint(src);
        const doc = view.state.doc;
        return errors.map((e) => {
          const ln = Math.max(1, Math.min(e.line, doc.lines));
          const lineObj = doc.line(ln);
          const from = Math.min(
            lineObj.from + Math.max(0, e.col - 1),
            lineObj.to,
          );
          const endLn = Math.max(1, Math.min(e.endLine || ln, doc.lines));
          const endObj = doc.line(endLn);
          let to = Math.min(
            endObj.from + Math.max(0, (e.endCol || e.col) - 1),
            doc.length,
          );
          if (to <= from) to = Math.min(from + 1, doc.length);
          return { from, to, severity: "error" as const, message: e.msg };
        });
      },
      { delay: 450 },
    );
    return [python(), pyLint, lintGutter()];
  }, [requestLint]);

  const run = useCallback(() => {
    if (typeof SharedArrayBuffer === "undefined" || !self.crossOriginIsolated) {
      termRef.current?.writeln(
        "\x1b[31mThis page needs cross-origin isolation. Reload it directly.\x1b[0m",
      );
      return;
    }
    const term = termRef.current;
    term?.clear();
    runActiveRef.current = true;
    awaitingRef.current = false;
    inputBufRef.current = "";
    queueRef.current = [];

    const worker = ensureWorker();
    const sab = new SharedArrayBuffer(SAB_SIZE);
    sabRef.current = sab;
    setStatus("running");
    worker.postMessage({ type: "run", code, packages, sab });
    term?.focus();
  }, [code, packages, ensureWorker]);

  const stop = useCallback(() => {
    workerRef.current?.terminate();
    workerRef.current = null;
    runActiveRef.current = false;
    awaitingRef.current = false;
    setStatus("idle");
    termRef.current?.writeln("\x1b[31m\n— stopped —\x1b[0m");
    ensureWorker(); // respawn so the editor keeps linting
  }, [ensureWorker]);

  const reset = useCallback(() => {
    stop();
    setCode(initialCode);
    termRef.current?.clear();
    setStatus("idle");
  }, [initialCode, stop]);

  const copyCode = () => {
    navigator.clipboard?.writeText(code).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 1400);
    });
  };

  // Drag the vertical bar between the README pane and the editor column —
  // px delta as a percentage of the whole workspace width.
  const resizeReadme = useCallback((dx: number) => {
    const w = splitRef.current?.clientWidth ?? 1;
    setReadmePct((p) => clamp(p + (dx / w) * 100, 18, 62));
  }, []);

  // Drag the horizontal bar between editor and console — px delta as a
  // percentage of the right column's height.
  const resizeEditor = useCallback((dy: number) => {
    const h = rightColRef.current?.clientHeight ?? 1;
    setEditorPct((p) => clamp(p + (dy / h) * 100, 20, 82));
  }, []);

  const lineCount = code.split("\n").length;
  const isRunning = status === "running" || status === "waiting";

  return (
    <main className="pg-work">
      {/* toolbar */}
      <div className="pg-toolbar">
        <div className="pg-toolbar-left">
          <div className="pg-proj-emoji">{project.emoji}</div>
          <div style={{ minWidth: 0 }}>
            <h1 className="pg-proj-name">{project.name}</h1>
            <div className="pg-proj-meta">
              <span className="pill lang">Python</span>
              {project.deps && <span className="pill">{project.deps}</span>}
              <span className="pill">{project.lines} lines</span>
              {project.blurb && (
                <span className="pg-proj-blurb">· {project.blurb}</span>
              )}
            </div>
            {project.folderUrl && (
              <a
                className="pg-credit"
                href={project.folderUrl}
                target="_blank"
                rel="noreferrer"
              >
                <Code2 size={14} strokeWidth={2.25} aria-hidden="true" />
                <span>
                  {project.author
                    ? `Original project by @${project.author} — `
                    : ""}
                  view source on GitHub
                </span>
                <ArrowUpRight size={13} strokeWidth={2.25} aria-hidden="true" />
              </a>
            )}
          </div>
        </div>
        <div className="pg-toolbar-right">
          <div className={`pg-status ${status}`}>
            <span className="d" />
            <span>{STATUS_TEXT[status]}</span>
          </div>
          {!isRunning ? (
            <button className="pg-btn run" onClick={run}>
              <Play size={15} strokeWidth={2.5} fill="currentColor" />
              Run code
            </button>
          ) : (
            <button className="pg-btn stop" onClick={stop}>
              <Square size={14} strokeWidth={2.5} fill="currentColor" />
              Stop
            </button>
          )}
          <button className="pg-btn" onClick={reset} title="Reset to original">
            <RotateCcw size={14} strokeWidth={2.5} />
            Reset
          </button>
        </div>
      </div>

      {/* workspace — README on the left, editor stacked over console */}
      <div className="pg-split row" ref={splitRef}>
        {/* README — collapsible left pane */}
        {readmeHtml &&
          (readmeOpen ? (
            <>
              <section
                className="pg-window pg-readme-pane"
                style={{ flexGrow: readmePct } as CSSProperties}
              >
                <div className="pg-winbar">
                  <WinDots />
                  <div className="filename">
                    README<span className="dim">· what to build</span>
                  </div>
                  <div className="spacer" />
                  <button
                    className="iconbtn"
                    onClick={() => setReadmeOpen(false)}
                    title="Collapse README"
                    aria-label="Collapse README"
                  >
                    <PanelLeftClose size={15} strokeWidth={2.25} />
                  </button>
                </div>
                <div
                  className="pg-readme-body s-readme"
                  dangerouslySetInnerHTML={{ __html: readmeHtml }}
                />
              </section>
              <ResizeHandle
                orientation="x"
                className="pg-resize-split"
                onResize={resizeReadme}
                ariaLabel="Resize README panel"
              />
            </>
          ) : (
            <button
              className="pg-readme-rail"
              onClick={() => setReadmeOpen(true)}
              title="Show README"
              aria-label="Show README"
            >
              <BookOpen size={16} strokeWidth={2.25} aria-hidden="true" />
              <span className="pg-readme-rail-label">README</span>
            </button>
          ))}

        {/* editor + console, stacked vertically */}
        <div
          className="pg-right-col"
          ref={rightColRef}
          style={
            {
              flexGrow: readmeHtml && readmeOpen ? 100 - readmePct : 100,
              "--pg-ed-grow": editorPct,
              "--pg-co-grow": 100 - editorPct,
            } as CSSProperties
          }
        >
          {/* editor */}
          <div className="pg-window pg-editor">
            <div className="pg-winbar">
              <WinDots />
              <div className="filename">
                {project.id}.py<span className="dim">· Python 3.x</span>
              </div>
              <div className="spacer" />
              <span className="pill">{lineCount} lines</span>
              <button className="iconbtn" onClick={copyCode} title="Copy code">
                {copied ? (
                  <Check size={15} strokeWidth={2.5} />
                ) : (
                  <Copy size={15} strokeWidth={2.25} />
                )}
              </button>
            </div>
            <div className="pg-editor-body">
              <CodeMirror
                value={code}
                height="100%"
                theme={pybeginPaper}
                extensions={cmExtensions}
                onChange={setCode}
                basicSetup={{ tabSize: 4, highlightActiveLine: true }}
              />
            </div>
          </div>

          {/* drag bar between editor and console */}
          <ResizeHandle
            orientation="y"
            className="pg-resize-vert"
            onResize={resizeEditor}
            ariaLabel="Resize editor and console"
          />

          {/* console — real terminal */}
          <div className="pg-window pg-console">
            <div className="pg-winbar">
              <WinDots />
              <div className="filename">
                Console<span className="dim">· terminal</span>
              </div>
              <div className="spacer" />
              <button
                className="iconbtn"
                onClick={() => termRef.current?.clear()}
                title="Clear console"
              >
                <Eraser size={15} strokeWidth={2.25} />
              </button>
            </div>
            <div className="pg-console-body">
              <div className="pg-term" ref={termHostRef} />
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
