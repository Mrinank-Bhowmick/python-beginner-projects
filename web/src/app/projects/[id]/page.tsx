import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import SiteNav from "@/components/SiteNav";
import SiteFooter from "@/components/SiteFooter";
import TryItPanel from "@/components/TryItPanel";
import ProjectCredit from "@/components/ProjectCredit";
import { PROJECTS, REPO_URL, getProject } from "@/lib/data";

interface Params {
  params: Promise<{ id: string }>;
}

// Pre-render one static page per project.
export function generateStaticParams() {
  return PROJECTS.map((p) => ({ id: p.id }));
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { id } = await params;
  const p = getProject(id);
  if (!p) return { title: "Project not found" };
  const title = `${p.name} — Python beginner project`;
  const description = `${p.blurb} A ${p.lines}-line Python project (${p.deps}). ${
    p.playground ? "Edit and run it live in your browser." : "Read the code on GitHub."
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
  const p = getProject(id);
  if (!p) notFound();

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "SoftwareSourceCode",
    name: p.name,
    description: p.blurb,
    programmingLanguage: "Python",
    codeRepository: REPO_URL,
    url: `https://pybegin.pages.dev/projects/${p.id}/`,
    author: {
      "@type": "Person",
      name: p.author,
      url: `https://github.com/${p.author}`,
    },
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
              <span className="s-meta-pill dep">{p.deps}</span>
              <span className="s-meta-pill dep">{p.cat}</span>
              {p.playground && <span className="s-meta-pill play">▶ Playground</span>}
            </div>
            <div style={{ marginBottom: 22 }}>
              <ProjectCredit author={p.author} />
            </div>
            <div className="s-proj-actions">
              {p.playground && (
                <Link className="s-btn-pri" href={`/playground/${p.id}`}>
                  ▶ Open in playground
                </Link>
              )}
              <a
                className="s-btn-sec"
                href={REPO_URL}
                target="_blank"
                rel="noreferrer"
              >
                View on GitHub →
              </a>
            </div>
            {p.runnable && <TryItPanel project={p} />}
          </div>

          <aside className="s-proj-side">
            <h3>Run it locally</h3>
            <div className="s-proj-code">
              <div className="c-accent">$ git clone python-beginner-projects.git</div>
              <div className="c-dim">$ cd projects/{p.id}</div>
              <div>$ python {p.id}.py</div>
            </div>
            <p style={{ fontSize: 14, color: "rgba(29,24,48,0.7)", marginTop: 16 }}>
              {p.playground
                ? "This project is pure Python — you can also edit and run it right here in the browser playground, no install needed."
                : "This project needs a desktop Python environment (it uses " +
                  p.deps +
                  "). Clone the repo to run it."}
            </p>
          </aside>
        </article>

        <SiteFooter />
      </div>
    </>
  );
}
