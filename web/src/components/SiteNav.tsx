import Link from "next/link";
import StickerLogo from "./StickerLogo";
import { REPO_URL } from "@/lib/data";

// Simple nav for project / playground pages (no bookmark state).
export default function SiteNav({
  active,
}: {
  active?: "home" | "projects" | "playground";
}) {
  return (
    <nav className="s-nav">
      <Link className="s-logo" href="/">
        <div className="s-logomark">
          <StickerLogo />
        </div>
        <div>
          <div className="s-brand-name">pyBegin</div>
          <div className="s-brand-sub">250+ projects · 1 weekend each</div>
        </div>
      </Link>
      <div className="s-navlinks">
        <Link className={active === "home" ? "active" : ""} href="/">
          Home
        </Link>
        <Link
          className={active === "projects" ? "active" : ""}
          href="/#gallery"
        >
          Projects
        </Link>
        <Link
          className={active === "playground" ? "active" : ""}
          href="/playground"
        >
          Playground
        </Link>
      </div>
      <div className="s-nav-right">
        <a className="s-cta" href={REPO_URL} target="_blank" rel="noreferrer">
          ★ Star · 2.3k
        </a>
      </div>
    </nav>
  );
}
