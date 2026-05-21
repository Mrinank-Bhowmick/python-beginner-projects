import fs from "fs";
import path from "path";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import PlaygroundNav from "@/components/PlaygroundNav";
import PlaygroundSidebar from "@/components/PlaygroundSidebar";
import Playground, { type PlaygroundProject } from "@/components/Playground";
import { PROJECTS, getProject, projectFolderUrl } from "@/lib/data";

interface Params {
  params: Promise<{ id: string }>;
}

// micropip packages each playground project needs (most need none).
const PACKAGES: Record<string, string[]> = {
  qr: ["qrcode"],
};

// Read the curated source for a project from public/playground at build time.
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

export function generateStaticParams() {
  return PROJECTS.filter((p) => p.playground).map((p) => ({ id: p.id }));
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { id } = await params;
  const p = getProject(id);
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
  const p = getProject(id);
  if (!p || !p.playground) notFound();

  const source = readSource(id);
  if (source == null) notFound();

  const project: PlaygroundProject = {
    id: p.id,
    name: p.name,
    emoji: p.emoji,
    deps: p.deps,
    lines: p.lines,
    blurb: p.blurb,
    author: p.author,
    folderUrl: projectFolderUrl(p),
  };

  return (
    <div className="pg-app">
      <PlaygroundNav />
      <div className="pg-main">
        <PlaygroundSidebar activeId={id} />
        <Playground
          project={project}
          initialCode={source}
          packages={PACKAGES[id] || []}
        />
      </div>
    </div>
  );
}
