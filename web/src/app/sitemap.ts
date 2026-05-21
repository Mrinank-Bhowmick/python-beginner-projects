import type { MetadataRoute } from "next";
import { PROJECTS } from "@/lib/data";

const BASE = "https://pybegin.pages.dev";

export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();
  const entries: MetadataRoute.Sitemap = [
    { url: `${BASE}/`, lastModified: now, priority: 1 },
    { url: `${BASE}/playground/`, lastModified: now, priority: 0.8 },
  ];
  for (const p of PROJECTS) {
    entries.push({
      url: `${BASE}/projects/${p.id}/`,
      lastModified: now,
      priority: 0.7,
    });
    if (p.playground) {
      entries.push({
        url: `${BASE}/playground/${p.id}/`,
        lastModified: now,
        priority: 0.6,
      });
    }
  }
  return entries;
}
