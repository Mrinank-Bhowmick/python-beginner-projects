import type { Metadata } from "next";
import PlaygroundNav from "@/components/PlaygroundNav";
import PlaygroundSidebar from "@/components/PlaygroundSidebar";
import Playground, { type PlaygroundProject } from "@/components/Playground";

export const metadata: Metadata = {
  title: "Python Playground — write and run Python in your browser",
  description:
    "A free in-browser Python playground. Edit Python code and run it live with a real console — no install, no signup. Powered by Pyodide (CPython in WebAssembly).",
  alternates: { canonical: "/playground/" },
  openGraph: {
    title: "Python Playground · pyBegin",
    description:
      "Edit and run Python live in your browser — real CPython, no install.",
    url: "/playground/",
  },
};

const SCRATCHPAD = `# Welcome to the pyBegin playground!
# This runs real Python in your browser. Edit the code and hit Run.

name = input("What's your name? ")
print(f"Hi {name}! Let's write some Python.")

for i in range(1, 6):
    print(f"{i} x {i} = {i * i}")
`;

const SCRATCH: PlaygroundProject = {
  id: "scratch",
  name: "Blank scratchpad",
  emoji: "✏️",
  deps: "stdlib",
  lines: SCRATCHPAD.trimEnd().split("\n").length,
  blurb: "Empty file. Write anything.",
};

export default function PlaygroundPage() {
  return (
    <div className="pg-app">
      <PlaygroundNav />
      <div className="pg-main">
        <PlaygroundSidebar activeId="scratch" />
        <Playground project={SCRATCH} initialCode={SCRATCHPAD} />
      </div>
    </div>
  );
}
