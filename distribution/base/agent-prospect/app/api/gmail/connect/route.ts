import { randomBytes } from "node:crypto";
import { NextResponse, type NextRequest } from "next/server";
import { authUrl, oauthApp } from "@/net/gmail";

export async function GET(request: NextRequest) {
  const app = oauthApp();
  if (!app) return NextResponse.redirect(new URL("/suivi", request.url));
  const state = randomBytes(16).toString("hex");
  const res = NextResponse.redirect(authUrl(app, new URL("/api/gmail/callback", request.url).toString(), state));
  res.cookies.set("gmail_oauth_state", state, { httpOnly: true, sameSite: "lax", path: "/api/gmail", maxAge: 600 });
  return res;
}
