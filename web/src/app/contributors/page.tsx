import type { Metadata } from "next";
import SiteNav from "@/components/SiteNav";
import SiteFooter from "@/components/SiteFooter";
import { REPO_URL } from "@/lib/data";
import type { RepoContributor } from "@/types";
import contributors from "@/lib/contributors.json";

// The full contributor roll, scraped from the README by scripts/gen-contributors.mjs.
const CONTRIBUTORS = contributors as RepoContributor[];

export const metadata: Metadata = {
  title: "Contributors — pyBegin",
  description: `The ${CONTRIBUTORS.length} people who built the pyBegin beginner-project collection.`,
};

export default function ContributorsPage() {
  return (
    <div className="s-shell">
      <SiteNav />

      <header className="s-crew-head">
        <h1 className="s-crew-title">
          Made by <em>{CONTRIBUTORS.length}</em> humans.
        </h1>
        <p className="s-crew-sub">
          Everyone who has contributed a project or a fix to this open-source
          collection. Your face could be here next —{" "}
          <a href={`${REPO_URL}/blob/main/CONTRIBUTING.md`}>
            start with the contributing guide
          </a>
          .
        </p>
      </header>

      <div className="s-crew-grid">
        {CONTRIBUTORS.map((c) => (
          <a
            key={c.handle}
            className="s-crew-card"
            href={`https://github.com/${c.handle}`}
            target="_blank"
            rel="noreferrer"
            title={`${c.name} — @${c.handle}`}
          >
            <img
              className="s-crew-avatar"
              src={`${c.avatar}&s=132`}
              alt=""
              width={66}
              height={66}
              loading="lazy"
            />
            <div className="s-crew-name">{c.name}</div>
            <div className="s-crew-handle">@{c.handle}</div>
          </a>
        ))}
      </div>

      <SiteFooter />
    </div>
  );
}
