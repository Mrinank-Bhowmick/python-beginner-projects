// Slim top nav for the full-bleed playground workspace.

import Link from "next/link";
import StickerLogo from "./StickerLogo";
import { REPO_URL } from "@/lib/data";

export default function PlaygroundNav() {
  return (
    <nav className="pg-nav">
      <Link className="pg-nav-left" href="/">
        <div className="pg-logomark">
          <StickerLogo />
        </div>
        <div>
          <div className="pg-brand-name">pyBegin</div>
          <div className="pg-brand-sub">250+ projects · 1 weekend each</div>
        </div>
      </Link>
      <div className="pg-nav-mid">
        <Link href="/">Home</Link>
        <Link href="/#gallery">Projects</Link>
        <Link className="active" href="/playground">
          Playground
        </Link>
        <a href={`${REPO_URL}/blob/main/CONTRIBUTING.md`}>Contribute</a>
      </div>
      <div className="pg-nav-right">
        <a className="pg-star-btn" href={REPO_URL} target="_blank" rel="noreferrer">
          ★ Star · 2.3k
        </a>
      </div>
    </nav>
  );
}
