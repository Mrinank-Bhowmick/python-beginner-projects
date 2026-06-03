import type { Metadata } from "next";
import SiteFooter from "@/components/SiteFooter";
import SiteNav from "@/components/SiteNav";

export const metadata: Metadata = {
  title: "Disclaimer",
  description: "Disclaimer for the pyBegin educational project.",
};

export default function DisclaimerPage() {
  return (
    <div className="s-shell">
      <SiteNav />
      <main className="s-readme">
        <h1>Disclaimer</h1>
        <p>Last updated: June 3, 2026</p>

        <p>
          This repository and website are personal hobby projects created for
          learning, education, and portfolio demonstration.
        </p>

        <p>
          The code, examples, documentation, project descriptions, and website
          content are provided &quot;as is&quot; and &quot;as available&quot;,
          without warranties of any kind. I do not guarantee that anything in
          this project is accurate, complete, secure, error-free, maintained, or
          suitable for any particular purpose.
        </p>

        <p>
          Use, copy, modify, run, or rely on this project at your own risk. To
          the maximum extent permitted by applicable law, I am not responsible
          for any loss, damage, claim, liability, legal issue, security issue,
          data loss, business interruption, or other problem arising from or
          related to this project.
        </p>

        <p>
          Nothing in this project is professional advice, including legal,
          financial, medical, security, business, or educational certification
          advice.
        </p>

        <p>
          Some projects may include APIs, automation, scraping, bots, databases,
          media processing, encryption, networking, health or ML-style datasets,
          or other higher-risk topics. These examples are educational only. You
          are responsible for checking the code, complying with applicable laws
          and third-party terms, and using safe test environments.
        </p>

        <p>
          If Indian law applies, this disclaimer should be read subject to rights
          and liabilities that cannot legally be excluded. Nothing here is
          intended to absolutely restrict a person from approaching a competent
          court or authority.
        </p>
      </main>
      <SiteFooter />
    </div>
  );
}
