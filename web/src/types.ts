// Shared types for the pyBegin frontend.

export type CategoryId = "all" | "games" | "tools" | "web" | "fun";

export interface Project {
  id: string;
  name: string;
  cat: Exclude<CategoryId, "all">;
  blurb: string;
  lines: number;
  deps: string;
  emoji: string;
  /** GitHub handle of the contributor who first added this project. */
  author: string;
  /** Folder path under projects/ in the repo (for the source link). */
  repoPath: string;
  /** Has a server-backed "Try it" demo via the Cloudflare Worker. */
  runnable?: boolean;
  /** Can run fully in-browser via Pyodide (pure-stdlib console programs). */
  playground?: boolean;
}

export interface Category {
  id: CategoryId;
  name: string;
  count: number;
}

export interface Contributor {
  handle: string;
  name: string;
  commits: number;
  role?: string;
}

export interface Stats {
  projects: number;
  contributors: number;
  stars: number;
  forks: number;
}

export interface LearningPath {
  id: string;
  name: string;
  tag: string;
  desc: string;
  items: string[];
  hue: number;
}
