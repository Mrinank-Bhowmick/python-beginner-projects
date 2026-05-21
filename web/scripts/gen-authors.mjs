// One-off: build src/lib/authors.json — a { "<project folder>": "<github-login>" }
// map crediting the contributor who first added each project.
//
// It finds the commit that first added a file under projects/<folder>/, then
// asks the GitHub API for that commit's author login (the git author name in
// the local history is not always a GitHub handle).
//
// Run from web/ with gh authenticated:  node scripts/gen-authors.mjs
// authors.json is committed; re-run only when new projects are added.

import { execSync } from "child_process";
import fs from "fs";
import path from "path";

const WEB = process.cwd();
const REPO = path.join(WEB, "..");
const OUT = path.join(WEB, "src", "lib", "authors.json");

// folder -> first-add commit SHA
const log = execSync(
  'git log --reverse --diff-filter=A --format="C|%H" --name-only -- projects/',
  { cwd: REPO, encoding: "utf8", maxBuffer: 64 * 1024 * 1024 },
);
const folderSha = {};
let sha = null;
for (const line of log.split(/\r?\n/)) {
  if (line.startsWith("C|")) {
    sha = line.slice(2);
    continue;
  }
  const m = line.match(/^projects\/([^/]+)\//);
  if (m && !folderSha[m[1]]) folderSha[m[1]] = sha;
}

const shas = [...new Set(Object.values(folderSha))];
console.log(`${Object.keys(folderSha).length} folders · ${shas.length} commits`);

// commit SHA -> github login (cached to survive interrupted runs)
const cacheFile = path.join(WEB, "scripts", "_sha-login.json");
const shaLogin = fs.existsSync(cacheFile)
  ? JSON.parse(fs.readFileSync(cacheFile, "utf8"))
  : {};

let done = 0;
for (const s of shas) {
  done++;
  if (s in shaLogin) continue;
  try {
    const login = execSync(
      `gh api repos/Mrinank-Bhowmick/python-beginner-projects/commits/${s} --jq .author.login`,
      { cwd: REPO, encoding: "utf8" },
    ).trim();
    shaLogin[s] = login || null;
  } catch {
    shaLogin[s] = null;
  }
  if (done % 20 === 0) {
    fs.writeFileSync(cacheFile, JSON.stringify(shaLogin));
    console.log(`  ${done}/${shas.length}`);
  }
}
fs.writeFileSync(cacheFile, JSON.stringify(shaLogin));

const authors = {};
for (const [folder, s] of Object.entries(folderSha)) {
  const login = shaLogin[s];
  if (login) authors[folder] = login;
}

const sorted = Object.fromEntries(
  Object.entries(authors).sort(([a], [b]) => a.localeCompare(b)),
);
fs.writeFileSync(OUT, JSON.stringify(sorted, null, 2) + "\n");
console.log(`authors.json: ${Object.keys(sorted).length} credited`);
