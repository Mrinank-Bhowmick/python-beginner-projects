import type { Metadata } from "next";
import Home from "@/components/Home";
import { PROJECTS } from "@/lib/data";

export const metadata: Metadata = {
  alternates: { canonical: "/" },
};

// JSON-LD: the site + the project collection, for rich search results.
const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      name: "pyBegin",
      url: "https://pybegin.pages.dev/",
      description:
        "250+ tiny Python beginner projects with an in-browser Python playground.",
    },
    {
      "@type": "ItemList",
      name: "Python beginner projects",
      numberOfItems: PROJECTS.length,
      itemListElement: PROJECTS.map((p, i) => ({
        "@type": "ListItem",
        position: i + 1,
        name: p.name,
        url: `https://pybegin.pages.dev/projects/${p.id}/`,
      })),
    },
  ],
};

export default function Page() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <Home />
    </>
  );
}
