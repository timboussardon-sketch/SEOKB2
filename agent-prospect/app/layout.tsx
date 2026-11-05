import type { Metadata } from "next";
import { GeistSans } from "geist/font/sans";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = { title: "Agent avocats", robots: { index: false, follow: false } };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" className={GeistSans.variable}>
      <body>
        <header className="top">
          <div className="in">
            <strong>Agent avocats</strong>
            <nav>
              <Link href="/campaigns">Campagnes</Link>
              <Link href="/prospects">Prospects</Link>
              <Link href="/review">Revue</Link>
            </nav>
          </div>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
