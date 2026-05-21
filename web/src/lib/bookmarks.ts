// Bookmark persistence (localStorage). SSR-safe: every access guards `window`.

const KEY = "pbp_bookmarks_v1";

export function getBookmarks(): string[] {
  if (typeof window === "undefined") return [];
  try {
    return (JSON.parse(localStorage.getItem(KEY) || "[]") as string[]) || [];
  } catch {
    return [];
  }
}

function setBookmarks(arr: string[]): void {
  if (typeof window === "undefined") return;
  localStorage.setItem(KEY, JSON.stringify(arr));
}

/** Toggle a project id and return the new bookmark list. */
export function toggleBookmark(id: string): string[] {
  const arr = getBookmarks();
  const i = arr.indexOf(id);
  if (i >= 0) arr.splice(i, 1);
  else arr.push(id);
  setBookmarks(arr);
  return arr;
}
