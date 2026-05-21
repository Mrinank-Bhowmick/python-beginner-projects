import fs from "fs";
import path from "path";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { marked } from "marked";
import PlaygroundNav from "@/components/PlaygroundNav";
import PlaygroundSidebar from "@/components/PlaygroundSidebar";
import Playground, { type PlaygroundProject } from "@/components/Playground";
import { CATALOG, getCatalogProject, catalogFolderUrl } from "@/lib/catalog";

interface Params {
  params: Promise<{ id: string }>;
}

// micropip packages each playground project needs (most need none).
const PACKAGES: Record<string, string[]> = {
  qr: ["qrcode"],
  aes256: ["pycryptodome"],
  "pokemon-battle": ["numpy"],
};

// Read a project's playground source from public/playground at build time.
function readSource(id: string): string | null {
  try {
    return fs.readFileSync(
      path.join(process.cwd(), "public", "playground", `${id}.py`),
      "utf8",
    );
  } catch {
    return null;
  }
}

// Read and render the project's README (one level up, in projects/<folder>/).
function readReadmeHtml(folder: string): string | null {
  const dir = path.join(process.cwd(), "..", "projects", folder);
  for (const name of ["README.md", "readme.md", "Readme.md"]) {
    const file = path.join(dir, name);
    if (fs.existsSync(file)) {
      return marked.parse(fs.readFileSync(file, "utf8"), {
        async: false,
      }) as string;
    }
  }
  return null;
}

export function generateStaticParams() {
  return CATALOG.filter((p) => p.hasPlayground).map((p) => ({ id: p.id }));
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { id } = await params;
  const p = getCatalogProject(id);
  if (!p) return { title: "Playground" };
  const description = `Edit and run the ${p.name} Python project live in your browser. ${p.blurb}`;
  return {
    title: `${p.name} — Python playground`,
    description,
    alternates: { canonical: `/playground/${p.id}/` },
    openGraph: {
      title: `${p.name} playground · pyBegin`,
      description,
      url: `/playground/${p.id}/`,
    },
  };
}

export default async function ProjectPlaygroundPage({ params }: Params) {
  const { id } = await params;
  const p = getCatalogProject(id);
  if (!p || !p.hasPlayground) notFound();

  const source = readSource(id);
  if (source == null) notFound();

  const project: PlaygroundProject = {
    id: p.id,
    name: p.name,
    emoji: p.emoji,
    deps: "",
    lines: p.lines,
    blurb: p.blurb,
    author: p.author,
    folderUrl: catalogFolderUrl(p),
  };

  const readmeHtml = readReadmeHtml(p.folder);

  return (
    <div className="pg-app">
      <PlaygroundNav />
      <div className="pg-main">
        <PlaygroundSidebar activeId={id} />
        <Playground
          project={project}
          initialCode={source}
          packages={PACKAGES[id] || []}
          readmeHtml={readmeHtml}
        />
      </div>
    </div>
  );
}
