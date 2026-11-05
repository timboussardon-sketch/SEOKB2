import { eq } from "drizzle-orm";
import { notFound } from "next/navigation";
import type { AuditReport } from "@/core/audit";
import { getDb, schema } from "@/db/client";
import { ReportView } from "@/server/report-view";
import { SimBanner } from "@/server/ui";

export const dynamic = "force-dynamic";
export const metadata = { title: "Pré-audit", robots: { index: false, follow: false } };

/** Rapport partagé : accessible par jeton non devinable, limité dans le temps, révocable. Aucune coordonnée du prospect n'y figure. */
export default async function SharedReport({ params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  if (!/^[A-Za-z0-9_-]{20,64}$/.test(token)) notFound();
  const [audit] = await getDb().select().from(schema.audits).where(eq(schema.audits.share_token, token));
  if (!audit || audit.share_revoked || audit.share_expires_at.getTime() < Date.now()) notFound();
  const report = audit.report as AuditReport;
  return (
    <>
      <SimBanner simulation={report.simulation} />
      <h1>Pré-audit{report.firm_name ? ` : ${report.firm_name}` : ""}</h1>
      <p className="muted">Préparé par Timothée Boussardon, Organikk.</p>
      <ReportView report={report} />
    </>
  );
}
