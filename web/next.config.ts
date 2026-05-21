import type { NextConfig } from "next";

// Cross-origin isolation headers — required for SharedArrayBuffer (the
// playground's blocking stdin). In production these come from public/_headers
// on Cloudflare Pages; this `headers()` block applies them during `next dev`.
const coopCoep = [
  { key: "Cross-Origin-Opener-Policy", value: "same-origin" },
  { key: "Cross-Origin-Embedder-Policy", value: "require-corp" },
];

const nextConfig: NextConfig = {
  // Static export — builds to ./out, deployed to Cloudflare Pages.
  output: "export",
  // No Next.js image optimization server in a static export.
  images: { unoptimized: true },
  // Pretty, trailing-slash URLs map cleanly to Pages' static routing.
  trailingSlash: true,
  // Applies in `next dev` only; ignored by `output: export` (Pages uses _headers).
  async headers() {
    return [{ source: "/:path*", headers: coopCoep }];
  },
};

export default nextConfig;
