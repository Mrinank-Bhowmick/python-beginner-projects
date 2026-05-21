import Link from "next/link";
import SiteNav from "@/components/SiteNav";
import SiteFooter from "@/components/SiteFooter";

export default function NotFound() {
  return (
    <div className="s-shell">
      <SiteNav />
      <div className="s-empty" style={{ marginTop: 60 }}>
        <div className="em">🫥</div>
        <h3>Page not found.</h3>
        <p>That page slithered off somewhere.</p>
        <div style={{ marginTop: 20 }}>
          <Link className="s-btn-pri" href="/">
            ← Back home
          </Link>
        </div>
      </div>
      <SiteFooter />
    </div>
  );
}
