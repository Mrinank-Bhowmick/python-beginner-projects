// Shared data for the pyBegin site.
// Pulled from github.com/Mrinank-Bhowmick/python-beginner-projects
//
// `playground: true` marks pure-stdlib console programs that run fully
// in-browser via Pyodide. pygame / tkinter / network projects cannot.

import type {
  Category,
  Contributor,
  LearningPath,
  Project,
  Stats,
} from "@/types";

// `author` is the GitHub handle of the contributor who first added the
// project folder (resolved from git history via the GitHub API).
// `repoPath` is that project's folder path under projects/ in the repo.
export const PROJECTS: Project[] = [
  { id: "snake", name: "Snake Game", cat: "games", blurb: "Slither, eat, grow longer. The classic.", lines: 92, deps: "pygame", emoji: "🐍", author: "EbrG786", repoPath: "Snake Game" },
  { id: "tictactoe", name: "Tic-Tac-Toe", cat: "games", blurb: "Three in a row, terminal showdown.", lines: 64, deps: "stdlib", emoji: "⭕", author: "Mrinank-Bhowmick", repoPath: "Tic-Tac-Toe", playground: true },
  { id: "hangman", name: "Hangman", cat: "games", blurb: "Guess letters before the gallows complete.", lines: 78, deps: "stdlib", emoji: "🪢", author: "Mrinank-Bhowmick", repoPath: "Hangman", playground: true },
  { id: "flappy", name: "Flappy Bird", cat: "games", blurb: "Tap to flap. Avoid the pipes. Die. Repeat.", lines: 140, deps: "pygame", emoji: "🐦", author: "Nikita0509", repoPath: "Flappybird_game" },
  { id: "rps", name: "Rock · Paper · Scissors", cat: "games", blurb: "Best of three vs the random module.", lines: 48, deps: "stdlib", emoji: "✊", author: "ZackeryRSmith", repoPath: "Rock_Paper_Scissors", playground: true },
  { id: "calc", name: "Calculator", cat: "tools", blurb: "Tkinter buttons. Operator precedence. Beep.", lines: 110, deps: "tkinter", emoji: "🧮", author: "shubham7668", repoPath: "Calculator" },
  { id: "bmi", name: "BMI Calculator", cat: "tools", blurb: "Height + weight → a single questionable number.", lines: 36, deps: "stdlib", emoji: "⚖️", author: "Mrinank-Bhowmick", repoPath: "BMI_calculator", playground: true },
  { id: "weather", name: "Weather App", cat: "web", blurb: "OpenWeather API, your city, today.", lines: 88, deps: "requests", emoji: "☁️", author: "srujan-landeri", repoPath: "API Based Weather Report" },
  { id: "qr", name: "QR Code Generator", cat: "tools", blurb: "Text in, scannable square out.", lines: 22, deps: "qrcode", emoji: "▦", author: "SubramanyaKS", repoPath: "QRCode-Generator", playground: true },
  { id: "pwd", name: "Password Generator", cat: "tools", blurb: "Random, strong, immediately forgotten.", lines: 30, deps: "secrets", emoji: "🔐", author: "jrbublitz", repoPath: "Password Projects/Password Generator", playground: true },
  { id: "yt", name: "YouTube Downloader", cat: "web", blurb: "pytube wrapper. Save the lecture.", lines: 54, deps: "pytube", emoji: "⬇", author: "vk0812", repoPath: "YouTube Video Downloader" },
  { id: "madlibs", name: "Madlibs Generator", cat: "fun", blurb: "Fill in nouns. Receive nonsense. Laugh.", lines: 40, deps: "stdlib", emoji: "✏️", author: "ZackeryRSmith", repoPath: "Madlibs Generator", playground: true },
];

export const CATEGORIES: Category[] = [
  { id: "all", name: "All", count: 12 },
  { id: "games", name: "Games", count: 5 },
  { id: "tools", name: "Tools", count: 4 },
  { id: "web", name: "Web & API", count: 2 },
  { id: "fun", name: "Just for Fun", count: 1 },
];

export const CONTRIBUTORS: Contributor[] = [
  { handle: "Mrinank-Bhowmick", name: "Mrinank Bhowmick", commits: 412, role: "maintainer" },
  { handle: "ibra-kdbra", name: "Ibra-kdbra", commits: 38 },
  { handle: "itsyashvardhan", name: "Yashvardhan Singh", commits: 27 },
  { handle: "Alby084", name: "Alby084", commits: 24 },
  { handle: "ca20110820", name: "Cedric Anover", commits: 21 },
  { handle: "kanchanraiii", name: "Kanchan Rai", commits: 18 },
  { handle: "TERNION-1121", name: "Vikrant Bhadouriya", commits: 16 },
  { handle: "Guyunjeong", name: "Chloe", commits: 14 },
  { handle: "rik-chatterjee", name: "Rik Chatterjee", commits: 12 },
  { handle: "omkarxpatel", name: "Omkar Patel", commits: 11 },
  { handle: "UffaModey", name: "Fafa Modey", commits: 10 },
  { handle: "anish2105", name: "Anish Vantagodi", commits: 9 },
  { handle: "JohnRTitor", name: "Masum Reza", commits: 9 },
  { handle: "sudipg4112001", name: "Sudip Ghosh", commits: 8 },
  { handle: "shashaaankkkkk", name: "Shashank Shekhar", commits: 8 },
  { handle: "jrbublitz", name: "Jefferson Bublitz", commits: 7 },
  { handle: "vagxrth", name: "Vagarth Pandey", commits: 7 },
  { handle: "shriyansnaik", name: "Shriyans Naik", commits: 6 },
  { handle: "xlo-u", name: "Yash Upadhyay", commits: 6 },
  { handle: "payallenka", name: "Payallenka", commits: 5 },
];

export const STATS: Stats = { projects: 250, contributors: 241, stars: 2300, forks: 903 };

export const PATHS: LearningPath[] = [
  { id: "starter", name: "First Steps", tag: "Day 1", desc: "Variables, input, print. Calculator → BMI → RPS.", items: ["bmi", "rps", "calc"], hue: 0 },
  { id: "games", name: "Make Games", tag: "Week 1", desc: "Loops, state, the random module. Tic-Tac-Toe → Hangman → Snake.", items: ["tictactoe", "hangman", "snake"], hue: 1 },
  { id: "real", name: "Real World", tag: "Week 2", desc: "HTTP, files, libraries. Weather → QR → YouTube.", items: ["weather", "qr", "yt"], hue: 2 },
];

export const REPO_URL =
  "https://github.com/Mrinank-Bhowmick/python-beginner-projects";

export function getProject(id: string): Project | undefined {
  return PROJECTS.find((p) => p.id === id);
}

/** GitHub URL of a project's source folder in the repo. */
export function projectFolderUrl(p: Project): string {
  const path = p.repoPath
    .split("/")
    .map((seg) => encodeURIComponent(seg))
    .join("/");
  return `${REPO_URL}/tree/main/projects/${path}`;
}
