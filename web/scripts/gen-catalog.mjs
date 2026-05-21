// Catalog generator for the pyBegin site.
//
// Scans the repo's projects/ folder and emits src/lib/catalog.json — one entry
// per project (id, folder, name, blurb, runnable flag, line count).
//
// The in-browser playground for a project loads public/playground/<id>.py —
// a hand-written, annotated "tutorial" version of the project (the originals
// in projects/ are never modified). This script does NOT create those files;
// it only marks hasPlayground=true when one already exists.
//
// Run from the web/ directory:  node scripts/gen-catalog.mjs
//
// catalog.json is committed; re-run this whenever projects/ changes.

import fs from "fs";
import path from "path";

const WEB = process.cwd(); // expected: .../web
const PROJECTS_DIR = path.join(WEB, "..", "projects");
const PLAYGROUND_DIR = path.join(WEB, "public", "playground");
const OUT = path.join(WEB, "src", "lib", "catalog.json");

// The curated projects featured on the home page keep their original short
// ids / emoji / playground status so existing routes and the hand-tuned
// playground source files (public/playground/*.py) stay valid.
const CURATED = {
  "Snake Game": { id: "snake", emoji: "🐍", playground: false },
  "Tic-Tac-Toe": { id: "tictactoe", emoji: "⭕", playground: true },
  Hangman: { id: "hangman", emoji: "🪢", playground: true },
  Flappybird_game: { id: "flappy", emoji: "🐦", playground: false },
  Rock_Paper_Scissors: { id: "rps", emoji: "✊", playground: true },
  Calculator: { id: "calc", emoji: "🧮", playground: false },
  BMI_calculator: { id: "bmi", emoji: "⚖️", playground: true },
  "API Based Weather Report": { id: "weather", emoji: "☁️", playground: false },
  "QRCode-Generator": { id: "qr", emoji: "▦", playground: true },
  "YouTube Video Downloader": { id: "yt", emoji: "⬇", playground: false },
  "Madlibs Generator": { id: "madlibs", emoji: "✏️", playground: true },
};

// Contributor credit: folder -> github login. Built by gen-authors.mjs.
const AUTHORS_FILE = path.join(WEB, "src", "lib", "authors.json");
const AUTHORS = fs.existsSync(AUTHORS_FILE)
  ? JSON.parse(fs.readFileSync(AUTHORS_FILE, "utf8"))
  : {};

// Pick a context-appropriate emoji from the project's name + blurb. Ordered:
// the first matching rule wins, so more specific keywords come first.
const EMOJI_RULES = [
  [/tic.?tac.?toe/, "⭕"], [/hangman/, "🪢"], [/flappy/, "🐦"],
  [/rock.?paper|paper.?scissor/, "✊"], [/madlib/, "✏️"],
  [/snake/, "🐍"], [/sudoku|2048/, "🔢"], [/minesweeper/, "💣"],
  [/battleship/, "🚢"], [/\bpong\b/, "🏓"], [/tetris/, "🟦"],
  [/\bchess\b/, "♟️"], [/\bcard\b|blackjack|poker/, "🃏"],
  [/\bdice\b|\broll\b/, "🎲"], [/coin.?(flip|toss)|flip.?coin/, "🪙"],
  [/\bquiz\b|trivia/, "❓"], [/\bmaze\b|puzzle/, "🧩"],
  [/guess|\bgame\b/, "🎮"],
  [/calculator|\bcalc\b/, "🧮"], [/\bbmi\b/, "⚖️"],
  [/cipher|encrypt|decrypt|cryptograph|caesar|\baes\b|\brsa\b|\bhash\b/, "🔐"],
  [/password|\blogin\b|\bauth\b/, "🔑"],
  [/steganograph/, "🕵️"],
  [/qr.?code|barcode/, "▦"],
  [/weather/, "⛅"], [/\bnews\b/, "📰"],
  [/stock|market|trading/, "📈"],
  [/currency|exchange rate/, "💱"],
  [/\bbank\b|\batm\b|expense|budget|finance|\bmoney\b|salary/, "💰"],
  [/\btip\b/, "💵"],
  [/email|\bmail\b|gmail/, "📧"], [/telegram/, "✈️"],
  [/discord|whatsapp|\bchat\b|\bsms\b/, "💬"], [/\bbot\b/, "🤖"],
  [/scrap|crawl|spider/, "🕷️"],
  [/translat/, "🌍"], [/morse/, "📡"],
  [/wiki/, "📚"], [/dictionary|\bword\b/, "📖"],
  [/youtube|\bvideo\b/, "🎬"],
  [/download/, "⬇️"], [/upload/, "⬆️"],
  [/\bapi\b/, "🔌"], [/url.?shorten|shorten.?url/, "🔗"],
  [/website|\bweb\b|\burl\b|browser/, "🌐"],
  [/\bsearch\b/, "🔍"],
  [/music|\bsong\b|spotify|\bmp3\b/, "🎵"],
  [/audio|\bsound\b|\bvoice\b|speech|text.?to.?speech|\btts\b/, "🔊"],
  [/camera|webcam|\bopencv\b|face.?(detect|recogn)/, "📷"],
  [/screenshot|screen.?record/, "🖥️"],
  [/neural|neuron|machine.?learning|deep.?learning|\bai\b/, "🧠"],
  [/data|analysis|\bplot\b|\bchart\b|visuali[sz]/, "📊"],
  [/image|photo|picture|\bjpg\b|\bpng\b/, "🖼️"],
  [/\bpdf\b/, "📄"], [/excel|spreadsheet/, "📊"],
  [/\bcsv\b|\bjson\b/, "🗂️"],
  [/draw|paint|sketch|turtle|\bart\b/, "🎨"],
  [/colou?r/, "🎨"],
  [/clock|stopwatch/, "🕐"], [/timer|countdown/, "⏳"],
  [/alarm|reminder/, "⏰"], [/calendar/, "📅"],
  [/pomodoro/, "🍅"],
  [/todo|to.?do|\btask\b/, "✅"], [/\bnote\b|diary|journal/, "🗒️"],
  [/typing|keyboard|\bkey\b/, "⌨️"],
  [/automat|pyautogui|\bmouse\b/, "🖱️"],
  [/\bcpu\b|\bram\b|battery|\bsystem\b|monitor/, "🖥️"],
  [/network|\bping\b|\bport\b|\bip\b|wifi/, "🌐"],
  [/\bgui\b|tkinter|\bwindow\b/, "🪟"],
  [/math|equation|fibonacci|\bprime\b|factorial|euler|matrix|\balgebra\b/, "➗"],
  [/notification|\bnotify\b/, "🔔"],
  [/recommend/, "👍"], [/summar/, "📝"], [/\breview\b/, "🔎"],
  [/jarvis|assistant/, "🤖"],
  [/internet speed|speed test/, "📶"],
  [/predict|classif|\bquality\b|recogni[sz]/, "🔮"],
  [/drowsi|sleep/, "😴"], [/othello|reversi|\bgo\b game/, "⚫"],
  [/regex|regular expression/, "🔣"],
  [/number|counter|\bcount\b/, "🔢"],
  [/random/, "🎰"],
  [/\bname\b|username/, "🏷️"],
  [/\bjoke\b/, "😂"], [/\bmeme\b/, "🤣"], [/emoji/, "😀"],
  [/story|\bpoem\b|poetry/, "📜"],
  [/recipe|\bfood\b/, "🍽️"],
  [/\bage\b|birthday/, "🎂"],
  [/shopping|\bcart\b|\bstore\b|ecommerce/, "🛒"],
  [/contact/, "📇"],
  [/\bmap\b|location|\bgps\b/, "🗺️"],
  [/planet|\bspace\b|nasa|astronom|\bsolar\b/, "🪐"],
  [/rocket|launch/, "🚀"],
  [/\bcar\b|vehicle|tesla/, "🚗"],
  [/convert|converter/, "🔄"],
  [/\bascii\b/, "🔡"], [/generator|generate/, "⚙️"],
];

function emojiFor(name, blurb) {
  const hay = `${name} ${blurb}`.toLowerCase();
  for (const [re, emoji] of EMOJI_RULES) {
    if (re.test(hay)) return emoji;
  }
  return "🐍";
}

const slugify = (s) =>
  s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "") || "project";

function findReadme(dir) {
  for (const f of fs.readdirSync(dir)) {
    if (/^readme\.md$/i.test(f)) return path.join(dir, f);
  }
  return null;
}

function findMainPy(dir, folder) {
  const top = fs.readdirSync(dir, { withFileTypes: true });
  const pys = top
    .filter((d) => d.isFile() && d.name.toLowerCase().endsWith(".py"))
    .map((d) => d.name);
  const pick = (names) => {
    const byMain = names.find((n) => n.toLowerCase() === "main.py");
    if (byMain) return byMain;
    const slug = slugify(folder);
    const byName = names.find(
      (n) => slugify(n.replace(/\.py$/i, "")) === slug,
    );
    return byName || names[0];
  };
  if (pys.length) return path.join(dir, pick(pys));
  // look one level deep for projects that nest their code in a subfolder
  for (const d of top) {
    if (!d.isDirectory()) continue;
    const sub = path.join(dir, d.name);
    const subpys = fs
      .readdirSync(sub)
      .filter((n) => n.toLowerCase().endsWith(".py"));
    if (subpys.length) {
      const byMain = subpys.find((n) => n.toLowerCase() === "main.py");
      return path.join(sub, byMain || subpys[0]);
    }
  }
  return null;
}

function parseReadme(file) {
  const lines = fs.readFileSync(file, "utf8").split(/\r?\n/);

  let name = null;
  for (const l of lines) {
    const m = l.match(/^#\s+(.+)/);
    if (m) {
      name = m[1].trim();
      break;
    }
  }

  // blurb: first plain paragraph (skip headings, images, quotes, code fences),
  // joining the wrapped lines of that paragraph back into one sentence.
  let blurb = "";
  let inCode = false;
  const para = [];
  for (const raw of lines) {
    const l = raw.trim();
    if (l.startsWith("```")) {
      inCode = !inCode;
      continue;
    }
    if (inCode) continue;
    if (!l) {
      if (para.length) break;
      continue;
    }
    if (l.startsWith("#") || l.startsWith("![") || l.startsWith(">")) {
      if (para.length) break;
      continue;
    }
    if (l.startsWith("- ") || l.startsWith("* ") || /^\d+\.\s/.test(l)) {
      if (para.length) break;
      continue;
    }
    para.push(l);
  }
  blurb = para.join(" ");
  blurb = blurb
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/[*`_]/g, "")
    .trim();
  if (blurb.length > 150) blurb = blurb.slice(0, 147).trimEnd() + "…";

  // Pyodide-runnable verdict
  let runnable = false;
  const idx = lines.findIndex((l) =>
    /^#+\s*pyodide-runnable/i.test(l.trim()),
  );
  if (idx >= 0) {
    for (let i = idx + 1; i < lines.length; i++) {
      const l = lines[i].trim();
      if (!l) continue;
      runnable = /^(yes|partly)/i.test(l);
      break;
    }
  }
  return { name, blurb, runnable };
}

const folders = fs
  .readdirSync(PROJECTS_DIR, { withFileTypes: true })
  .filter((d) => d.isDirectory())
  .map((d) => d.name)
  .sort((a, b) => a.localeCompare(b));

const usedIds = new Set();
const entries = [];

for (const folder of folders) {
  const dir = path.join(PROJECTS_DIR, folder);
  const curated = CURATED[folder];

  let id;
  if (curated) {
    id = curated.id;
  } else {
    const base = slugify(folder);
    id = base;
    let n = 2;
    while (usedIds.has(id)) id = `${base}-${n++}`;
  }
  usedIds.add(id);

  let name = folder;
  let blurb = "";
  let verdictRunnable = false;
  const readmeFile = findReadme(dir);
  if (readmeFile) {
    const parsed = parseReadme(readmeFile);
    name = parsed.name || folder;
    blurb = parsed.blurb;
    verdictRunnable = parsed.runnable;
  }

  const mainPy = findMainPy(dir, folder);
  const lines = mainPy
    ? fs.readFileSync(mainPy, "utf8").split(/\r?\n/).length
    : 0;

  const runnable = curated ? curated.playground : verdictRunnable;
  const emoji = curated ? curated.emoji : emojiFor(name, blurb);
  const author = AUTHORS[folder];

  // A project is playable iff a hand-written annotated tutorial file exists
  // at public/playground/<id>.py. The originals in projects/ are never copied.
  const pgFile = path.join(PLAYGROUND_DIR, `${id}.py`);
  const hasPlayground = fs.existsSync(pgFile);

  entries.push({
    id, folder, name, blurb, emoji, runnable, hasPlayground, lines,
    ...(author ? { author } : {}),
  });
}

// The "Password Generator" sub-project is featured on the home page under its
// own short id; surface it as a standalone catalog entry too.
if (!usedIds.has("pwd")) {
  entries.push({
    id: "pwd",
    folder: "Password Projects/Password Generator",
    name: "Password Generator",
    blurb: "Generate random, strong passwords from the command line.",
    emoji: "🔐",
    runnable: true,
    hasPlayground: fs.existsSync(path.join(PLAYGROUND_DIR, "pwd.py")),
    lines: 30,
    ...(AUTHORS["Password Projects"]
      ? { author: AUTHORS["Password Projects"] }
      : {}),
  });
}

entries.sort((a, b) => a.name.localeCompare(b.name));
fs.writeFileSync(OUT, JSON.stringify(entries, null, 2) + "\n");

const runnableCount = entries.filter((e) => e.runnable).length;
const pgCount = entries.filter((e) => e.hasPlayground).length;
console.log(
  `catalog.json: ${entries.length} projects · ${runnableCount} runnable · ${pgCount} with a playground file`,
);
