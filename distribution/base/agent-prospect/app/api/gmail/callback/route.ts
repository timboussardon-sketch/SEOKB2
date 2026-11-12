import { NextResponse, type NextRequest } from "next/server";
import { connectGmail } from "@/engine/outreach";
import { oauthApp } from "@/net/gmail";
import { getDeps } from "@/server/context";

export async function GET(request: NextRequest) {
  const app = oauthApp();
  const url = request.nextUrl;
  const back = (msg: string) => NextResponse.redirect(new URL(`/suivi?gmail=${encodeURIComponent(msg)}`, request.url));
  if (!app) return back("GMAIL_CLIENT_ID et GMAIL_CLIENT_SECRET absents");
  if (url.searchParams.get("error")) return back(`Autorisation refusée : ${url.searchParams.get("error")}`);
  const code = url.searchParams.get("code");
  if (!code || url.searchParams.get("state") !== request.cookies.get("gmail_oauth_state")?.value) return back("Retour Google invalide, recommence");
  try {
    const email = await connectGmail(await getDeps(), app, code, new URL("/api/gmail/callback", request.url).toString());
    return back(`Connecté : ${email}`);
  } catch (err) {
    return back(err instanceof Error ? err.message : "Erreur de connexion");
  }
}
