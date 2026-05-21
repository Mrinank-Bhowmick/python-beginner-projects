# AGENTS.md

## Repo layout

```
projects/      ~270 standalone beginner Python projects, one folder each
web/           Next.js website + in-browser Python playground
data/          static banner images
.github/       CI workflows
```

Two independent parts: the **Python projects** and the **website**. They don't
share code.

## projects/

Each project is a self-contained folder (`projects/Hangman/`, `projects/BMI_calculator/`).
No shared package, no repo-wide dependencies — a project lists its own libs in a
local `requirements.txt`/README. Folder naming is inconsistent; match the existing
folder, don't rename. Python is auto-formatted with Black in CI.

## web/ — system design

Next.js 16 (App Router, TypeScript, React 19), **statically exported** (`output: 'export'`)
and hosted on **Cloudflare Pages**. Pages are pre-rendered HTML at build time for SEO.

The **playground** runs real CPython in the browser — no server. Pyodide
(CPython → WebAssembly) loads in a **Web Worker** (`web/public/pyodide-worker.js`).
A `SharedArrayBuffer` + `Atomics` bridge lets blocking `input()` work, which is why
the playground needs cross-origin isolation (COOP/COEP headers in `web/public/_headers`).
The editor is CodeMirror 6; the terminal is xterm.js.

There is **no backend**. A Cloudflare Worker once executed code server-side — it was
removed; everything runs client-side now.

Key files:
- `web/src/app/` — routes (`/`, `/projects/[id]`, `/playground/[id]`)
- `web/src/lib/data.ts` — the project list shown on the site
- `web/public/playground/<id>.py` — code preloaded into the playground per project
- `web/src/lib/pyodide/` + `web/public/pyodide-worker.js` — the Pyodide worker

Only pure-stdlib console projects can run in the playground (`playground: true` in
`data.ts`); pygame/tkinter/network projects cannot.

Commands (inside `web/`): `corepack pnpm dev` (localhost:3000), `corepack pnpm
run build` (static export → `web/out/`, also runs the type check). The project
uses **pnpm** (pinned via `packageManager` in `package.json`); supply-chain
settings are in `web/pnpm-workspace.yaml`. Do not reintroduce `package-lock.json`.
