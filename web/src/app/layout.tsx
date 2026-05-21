import type { Metadata } from "next";
import { Fraunces, DM_Sans, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const display = Fraunces({
  subsets: ["latin"],
  variable: "--font-display",
  weight: ["400", "600", "900"],
  style: ["normal", "italic"],
  display: "swap",
});

const body = DM_Sans({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["400", "500", "600", "700", "800"],
  display: "swap",
});

const mono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  weight: ["400", "500", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://pybegin.pages.dev"),
  title: {
    default: "pyBegin · 250+ Python beginner projects you can run in the browser",
    template: "%s · pyBegin",
  },
  description:
    "A scrappy collection of tiny Python projects — each small enough to read in a coffee break. Browse 250+ beginner projects, then edit and run them live in an in-browser Python playground.",
  keywords: [
    "python beginner projects",
    "learn python",
    "python playground",
    "run python in browser",
    "python code editor",
    "python examples",
  ],
  authors: [{ name: "Mrinank Bhowmick" }],
  openGraph: {
    type: "website",
    siteName: "pyBegin",
    title: "pyBegin · 250+ Python beginner projects",
    description:
      "Browse 250+ tiny Python projects and run them live in an in-browser playground. No install, no setup.",
    url: "/",
  },
  twitter: {
    card: "summary_large_image",
    title: "pyBegin · 250+ Python beginner projects",
    description:
      "Browse 250+ tiny Python projects and run them live in an in-browser playground.",
  },
  alternates: { canonical: "/" },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="en"
      className={`${display.variable} ${body.variable} ${mono.variable}`}
    >
      <body>{children}</body>
    </html>
  );
}
