// Generates src/lib/contributors.json — every contributor, scraped from the
// contrib-readme-action block in the repo's README.md (handle, display name,
// GitHub avatar URL).
//
// Run from the web/ directory:  node scripts/gen-contributors.mjs
// Re-run whenever the README's contributors list changes.

import fs from "fs";
import path from "path";

const WEB = process.cwd();
const README = path.join(WEB, "..", "README.md");
const OUT = path.join(WEB, "src", "lib", "contributors.json");

const BOTS = new Set(["lint-action", "github-actions", "dependabot"]);

const md = fs.readFileSync(README, "utf8");
const start = md.indexOf("<!-- readme: contributors -start -->");
const end = md.indexOf("<!-- readme: contributors -end -->");
if (start < 0 || end < 0) {
  throw new Error("contributors block not found in README.md");
}
const block = md.slice(start, end);

// Each entry: <a href="…/HANDLE"> <img src="AVATAR" … /> <br/> <sub><b>NAME</b></sub>
const re =
  /<a href="https:\/\/github\.com\/([^"/]+)">\s*<img src="([^"]+)"[^>]*\/>\s*<br\s*\/>\s*<sub><b>([^<]+)<\/b><\/sub>/g;

const seen = new Set();
const contributors = [];
let m;
while ((m = re.exec(block))) {
  const handle = m[1].trim();
  const key = handle.toLowerCase();
  if (seen.has(key) || BOTS.has(key) || key.endsWith("[bot]")) continue;
  seen.add(key);
  contributors.push({ handle, name: m[3].trim(), avatar: m[2].trim() });
}

fs.writeFileSync(OUT, JSON.stringify(contributors, null, 2) + "\n");
console.log(`contributors.json: ${contributors.length} contributors`);
