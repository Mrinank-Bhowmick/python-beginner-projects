import fs from "fs";
import path from "path";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { marked } from "marked";
import SiteNav from "@/components/SiteNav";
import SiteFooter from "@/components/SiteFooter";
import RunnableBadge from "@/components/RunnableBadge";
import { REPO_URL } from "@/lib/data";
import { CATALOG, getCatalogProject, catalogFolderUrl } from "@/lib/catalog";

interface Params {
  params: Promise<{ id: string }>;
}

// Read a project's README from projects/<folder>/ at build time and render it
// to HTML. The catalog lives in web/, the projects/ folder is one level up.
function readReadmeHtml(folder: string): string | null {
  const dir = path.join(process.cwd(), "..", "projects", folder);
  for (const name of ["README.md", "readme.md", "Readme.md"]) {
    const file = path.join(dir, name);
    if (fs.existsSync(file)) {
      const md = fs.readFileSync(file, "utf8");
      return marked.parse(md, { async: false }) as string;
    }
  }
  return null;
}

// Pre-render one static page per catalog project.
export function generateStaticParams() {
  return CATALOG.map((p) => ({ id: p.id }));
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { id } = await params;
  const p = getCatalogProject(id);
  if (!p) return { title: "Project not found" };
  const title = `${p.name} — Python beginner project`;
  const description = `${p.blurb} ${
    p.hasPlayground
      ? "Edit and run it live in your browser."
      : "Read the code and README on GitHub."
  }`;
  return {
    title,
    description,
    alternates: { canonical: `/projects/${p.id}/` },
    openGraph: {
      title: `${p.name} · pyBegin`,
      description,
      url: `/projects/${p.id}/`,
      type: "article",
    },
    twitter: { card: "summary", title: `${p.name} · pyBegin`, description },
  };
}

export default async function ProjectPage({ params }: Params) {
  const { id } = await params;
  const p = getCatalogProject(id);
  if (!p) notFound();

  const readmeHtml = readReadmeHtml(p.folder);
  const folderUrl = catalogFolderUrl(p);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "SoftwareSourceCode",
    name: p.name,
    description: p.blurb,
    programmingLanguage: "Python",
    codeRepository: REPO_URL,
    url: `https://pybegin.pages.dev/projects/${p.id}/`,
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <div className="s-shell">
        <SiteNav active="projects" />

        <div className="s-crumb">
          <Link href="/">pyBegin</Link> / <Link href="/#gallery">projects</Link>{" "}
          / {p.id}
        </div>

        <article className="s-proj">
          <div>
            <div className="s-proj-emoji">{p.emoji}</div>
            <h1>{p.name}</h1>
            <p className="s-proj-blurb">{p.blurb}</p>
            <div className="s-proj-meta">
              <span className="s-meta-pill">{p.lines} lines</span>
              {p.runnable ? (
                <RunnableBadge />
              ) : (
                <span className="s-meta-pill desk">🖥 Desktop only</span>
              )}
            </div>
            <div className="s-proj-actions">
              {p.hasPlayground && (
                <Link className="s-btn-pri" href={`/playground/${p.id}`}>
                  ▶ Open in playground
                </Link>
              )}
              <a
                className="s-btn-sec"
                href={folderUrl}
                target="_blank"
                rel="noreferrer"
              >
                View source folder on GitHub →
              </a>
              {p.author && (
                <a
                  className="s-proj-credit"
                  href={`https://github.com/${p.author}`}
                  target="_blank"
                  rel="noreferrer"
                >
                  <span className="s-proj-credit-by">contributed by</span>
                  <img
                    src={`https://github.com/${p.author}.png?size=48`}
                    alt=""
                    width={22}
                    height={22}
                  />
                  @{p.author}
                </a>
              )}
            </div>
          </div>

          <aside className="s-proj-side">
            <h3>Run it locally</h3>
            <div className="s-proj-code">
              <div className="c-accent">
                $ git clone python-beginner-projects.git
              </div>
              <div className="c-dim">$ cd &quot;projects/{p.folder}&quot;</div>
              <div>$ python ...</div>
            </div>
            <p
              style={{
                fontSize: 14,
                color: "rgba(29,24,48,0.7)",
                marginTop: 16,
              }}
            >
              {p.runnable
                ? "This project is pure-Python — you can also edit and run it right here in the browser playground, no install needed."
                : "This project needs a desktop Python environment. Clone the repo and follow the README below to run it."}
            </p>
          </aside>
        </article>

        {readmeHtml ? (
          <section
            className="s-readme"
            dangerouslySetInnerHTML={{ __html: readmeHtml }}
          />
        ) : (
          <section className="s-readme">
            <p>This project does not have a README yet.</p>
          </section>
        )}

        <SiteFooter />
      </div>
    </>
  );
}
