import { NextResponse, type NextRequest } from "next/server";

/**
 * Accès au tableau de bord par mot de passe (Basic auth). Les rapports partagés /r/<jeton> sont protégés par leur jeton.
 * Sans DASHBOARD_PASSWORD, l'accès est ouvert : le serveur n'écoute que sur 127.0.0.1 (npm start), donc depuis cette machine seulement.
 */
export function proxy(request: NextRequest) {
  const password = process.env.DASHBOARD_PASSWORD;
  if (!password) return NextResponse.next();
  const header = request.headers.get("authorization") ?? "";
  if (header.startsWith("Basic ")) {
    const given = atob(header.slice(6)).split(":").slice(1).join(":");
    if (given.length === password.length) {
      let diff = 0;
      for (let i = 0; i < given.length; i++) diff |= given.charCodeAt(i) ^ password.charCodeAt(i);
      if (diff === 0) return NextResponse.next();
    }
  }
  return new NextResponse("Authentification requise.", { status: 401, headers: { "WWW-Authenticate": 'Basic realm="Agent avocats"' } });
}

export const config = { matcher: ["/((?!r/|_next/|favicon.ico).*)"] };
