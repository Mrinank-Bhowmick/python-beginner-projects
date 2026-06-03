import { REPO_URL } from "@/lib/data";

export default function SiteFooter() {
  return (
    <footer className="s-footer">
      <div>
        Built with <span className="s-heart">♥</span> &amp; the standard library ·
        MIT licensed
      </div>
      <div className="s-footer-links">
        <a href={REPO_URL}>GitHub</a>
        <a href={`${REPO_URL}/issues`}>Issues</a>
        <a href={`${REPO_URL}/wiki`}>Wiki</a>
        <a href={`${REPO_URL}/blob/main/CODE_OF_CONDUCT.md`}>Code of Conduct</a>
        <a href="/terms">Terms</a>
        <a href="/privacy">Privacy</a>
        <a href="/disclaimer">Disclaimer</a>
      </div>
    </footer>
  );
}
