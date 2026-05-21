/* pyBegin playground — Pyodide Web Worker.
 *
 * Runs real CPython (via WebAssembly) in the browser. stdout/stderr stream to
 * the main thread; input() blocks the worker thread on a SharedArrayBuffer
 * until the main thread supplies a line typed in the terminal. Also answers
 * `lint` requests (compile() syntax check) for the editor's error squiggles.
 * Cross-origin isolation (COOP/COEP) is required — see public/_headers.
 */

/* global loadPyodide */

const PYODIDE_VERSION = "0.29.4";
importScripts(
  `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js`,
);

let pyodide = null;
let ctrl = null; // Int32Array view over the shared buffer
let data = null; // Uint8Array view for the input line bytes
let busy = false; // true while a program is running (no lint then)
const decoder = new TextDecoder();

// Called synchronously by Python on input(). Blocks the worker thread until
// the main thread writes a line into the shared buffer. The control flag is
// cleared *before* requesting input so a fast (type-ahead) reply can't be lost.
function blockingStdin() {
  if (!ctrl) return null;
  Atomics.store(ctrl, 0, 0);
  self.postMessage({ type: "stdin" });
  Atomics.wait(ctrl, 0, 0);
  const len = Atomics.load(ctrl, 1);
  if (len < 0) return null; // EOF
  return decoder.decode(data.slice(0, len));
}

async function boot() {
  self.postMessage({ type: "loading", text: "Downloading Python runtime…" });
  pyodide = await loadPyodide();
  pyodide.setStdout({
    write: (buf) => {
      self.postMessage({ type: "stdout", text: decoder.decode(buf) });
      return buf.length;
    },
  });
  pyodide.setStderr({
    write: (buf) => {
      self.postMessage({ type: "stderr", text: decoder.decode(buf) });
      return buf.length;
    },
  });
  // autoEOF:true — each input() invokes blockingStdin exactly once and treats
  // its returned newline-terminated string as one complete line.
  // (autoEOF:false makes Pyodide call stdin repeatedly until null → hangs.)
  pyodide.setStdin({ stdin: blockingStdin, autoEOF: true });

  // Syntax checker for the editor's lint squiggles.
  pyodide.runPython(`
import json as _json
def _pybegin_lint(src):
    try:
        compile(src, "<editor>", "exec")
        return "[]"
    except SyntaxError as e:
        return _json.dumps([{
            "line": e.lineno or 1,
            "col": e.offset or 1,
            "endLine": getattr(e, "end_lineno", None) or (e.lineno or 1),
            "endCol": getattr(e, "end_offset", None) or ((e.offset or 1) + 1),
            "msg": e.msg or "Syntax error",
        }])
    except Exception as e:
        return _json.dumps([{"line": 1, "col": 1, "endLine": 1, "endCol": 2,
                             "msg": type(e).__name__ + ": " + str(e)}])
`);
  self.postMessage({ type: "ready" });
}

const bootPromise = boot();

self.onmessage = async (e) => {
  const msg = e.data;

  // --- lint: compile-check the code, return diagnostics ---
  if (msg.type === "lint") {
    try {
      await bootPromise;
    } catch {
      return;
    }
    if (busy) {
      self.postMessage({ type: "lint-result", id: msg.id, errors: [] });
      return;
    }
    let errors = [];
    try {
      const fn = pyodide.globals.get("_pybegin_lint");
      errors = JSON.parse(fn(msg.code));
      fn.destroy();
    } catch {
      errors = [];
    }
    self.postMessage({ type: "lint-result", id: msg.id, errors });
    return;
  }

  if (msg.type !== "run") return;

  try {
    await bootPromise;
  } catch (err) {
    self.postMessage({ type: "stderr", text: "Failed to load Python: " + err + "\n" });
    self.postMessage({ type: "done" });
    return;
  }

  ctrl = new Int32Array(msg.sab, 0, 2);
  data = new Uint8Array(msg.sab, 8);
  busy = true;

  try {
    if (msg.packages && msg.packages.length) {
      self.postMessage({ type: "loading", text: "Installing " + msg.packages.join(", ") + "…" });
      await pyodide.loadPackage("micropip");
      const micropip = pyodide.pyimport("micropip");
      for (const p of msg.packages) await micropip.install(p);
    }
    self.postMessage({ type: "running" });
    // Fresh namespace per run so leftover variables don't leak between runs.
    const globals = pyodide.toPy({ __name__: "__main__" });
    await pyodide.runPythonAsync(msg.code, { globals });
    self.postMessage({ type: "done" });
  } catch (err) {
    const text = (err && err.message ? err.message : String(err)) + "\n";
    self.postMessage({ type: "stderr", text });
    self.postMessage({ type: "done" });
  } finally {
    busy = false;
  }
};
