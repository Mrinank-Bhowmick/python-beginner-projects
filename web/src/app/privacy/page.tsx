import type { Metadata } from "next";
import SiteFooter from "@/components/SiteFooter";
import SiteNav from "@/components/SiteNav";

export const metadata: Metadata = {
  title: "Privacy Notice",
  description: "Privacy notice for the pyBegin educational project.",
};

export default function PrivacyPage() {
  return (
    <div className="s-shell">
      <SiteNav />
      <main className="s-readme">
        <h1>Privacy Notice</h1>
        <p>Last updated: June 3, 2026</p>

        <p>This is a personal hobby project.</p>

        <h2>Personal Information</h2>
        <p>
          I do not intentionally collect personal information through this
          repository or website.
        </p>
        <p>
          If the website includes an in-browser code playground, it is intended
          to run in your browser for learning and experimentation. Do not enter
          private, sensitive, confidential, or important information into it.
        </p>
        <p>
          Do not submit secrets, API keys, passwords, tokens, private documents,
          regulated data, or other sensitive information through repository
          issues, pull requests, discussion threads, or the playground.
        </p>

        <h2>Hosting and Platform Logs</h2>
        <p>
          This project may be hosted or distributed through third-party platforms
          such as GitHub, Cloudflare Pages, package registries, analytics-free
          static hosting, or similar services. Those providers may process
          technical information such as IP addresses, browser details, request
          metadata, logs, cookies, or security signals according to their own
          policies.
        </p>
        <p>I do not control those third-party platforms.</p>

        <h2>Third-Party Links</h2>
        <p>
          This project may link to third-party websites or tools. Their privacy
          practices are controlled by their own policies, not by this notice.
        </p>
      </main>
      <SiteFooter />
    </div>
  );
}
