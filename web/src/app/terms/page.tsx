import type { Metadata } from "next";
import SiteFooter from "@/components/SiteFooter";
import SiteNav from "@/components/SiteNav";

export const metadata: Metadata = {
  title: "Terms of Use",
  description: "Terms of use for the pyBegin educational project.",
};

export default function TermsPage() {
  return (
    <div className="s-shell">
      <SiteNav />
      <main className="s-readme">
        <h1>Terms of Use</h1>
        <p>Last updated: June 3, 2026</p>

        <p>
          This website and repository are a personal hobby project created for
          learning, education, and portfolio demonstration. They are not a
          commercial service, professional product, or managed platform.
        </p>
        <p>
          These terms are intended to reduce legal risk, not to prevent anyone
          from using rights that cannot be waived under applicable law.
        </p>

        <h2>No Professional Advice</h2>
        <p>
          The content is for general educational and demonstration purposes only.
          It is not legal, financial, medical, security, business, or other
          professional advice.
        </p>

        <h2>No Warranty</h2>
        <p>
          This project is provided &quot;as is&quot; and &quot;as available&quot;,
          without warranties of any kind. I do not guarantee that the code,
          examples, documentation, website, playground, or other materials are
          accurate, complete, secure, error-free, available, maintained, or
          suitable for any particular purpose.
        </p>

        <h2>Use at Your Own Risk</h2>
        <p>
          You are responsible for how you use this project. To the maximum extent
          permitted by applicable law, I am not responsible for any loss, damage,
          claim, liability, legal issue, security issue, data loss, business
          interruption, or other problem caused by or related to your access to,
          use of, or reliance on this project.
        </p>
        <p>
          Some projects may include examples involving APIs, automation,
          scraping, bots, databases, media processing, encryption, networking,
          health or ML-style datasets, or other higher-risk topics. These
          examples are for learning only. You are responsible for complying with
          applicable laws, third-party terms of service, licenses, platform
          rules, and safety requirements before running, modifying, or deploying
          them.
        </p>

        <h2>Code Playground</h2>
        <p>
          If this website includes an in-browser code playground, it is provided
          only for learning and experimentation. Do not enter private, sensitive,
          confidential, or important information into it. You are responsible for
          any code you run, copy, modify, or share.
        </p>
        <p>
          The playground is not designed for secrets, private data, regulated
          data, or production workloads.
        </p>

        <h2>Third Parties</h2>
        <p>
          This project may reference, link to, or depend on third-party websites,
          libraries, tools, packages, or services. I do not control third parties
          and am not responsible for their content, behavior, availability,
          security, licensing, or policies.
        </p>
        <p>
          You are responsible for reviewing and complying with third-party terms,
          licenses, API rules, robots.txt files, platform rules, and usage
          limits.
        </p>

        <h2>Acceptable Use</h2>
        <p>
          Do not use this project to break the law, harm others, violate privacy,
          attack systems, bypass security, distribute malware, infringe
          intellectual property, or misrepresent this project as professional
          advice or a guaranteed product.
        </p>
        <p>
          Do not use this project for unlawful scraping, spam, phishing,
          credential theft, unauthorized automation, harassment, surveillance, or
          any activity that violates the rights of others.
        </p>

        <h2>India</h2>
        <p>
          If Indian law applies, these terms should be read subject to rights and
          liabilities that cannot legally be excluded. Nothing here is intended
          to absolutely restrict a person from approaching a competent court or
          authority.
        </p>

        <h2>Changes</h2>
        <p>
          I may update, change, remove, or stop maintaining any part of this
          project at any time without notice.
        </p>
      </main>
      <SiteFooter />
    </div>
  );
}
