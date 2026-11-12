"""Read-only local dashboard for the strategy coordinator."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from paths import team_root

STATIC = Path(__file__).resolve().parent

def make_handler(root):
    root = Path(root).resolve()
    class Handler(BaseHTTPRequestHandler):
        def send(self, status, payload, content_type):
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(payload)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.end_headers()
            self.wfile.write(payload)

        def do_GET(self):
            url = urlparse(self.path)
            if url.path == '/':
                return self.send(200, (STATIC / 'index.html').read_bytes(), 'text/html; charset=utf-8')
            public = {'/style.css': 'text/css; charset=utf-8', '/app.js': 'text/javascript; charset=utf-8', '/assets/geist.woff2': 'font/woff2'}
            if url.path in public:
                return self.send(200, (STATIC / url.path.lstrip('/')).read_bytes(), public[url.path])
            if url.path == '/health':
                return self.send(200, b'{"status":"ok"}', 'application/json')
            if url.path == '/api/status':
                try:
                    from team import Team
                    result = Team(root=root).status()
                    return self.send(200, json.dumps(result, ensure_ascii=False).encode(), 'application/json; charset=utf-8')
                except Exception:
                    return self.send(503, b'{"error":"Etat du coordinateur indisponible"}', 'application/json')
            if url.path == '/artifact':
                raw = parse_qs(url.query).get('path', [''])[0]
                try:
                    path = Path(raw)
                    if not path.is_absolute():
                        path = root / path
                    path = path.resolve()
                    path.relative_to((root / 'artifacts').resolve())
                    if path.suffix not in ('.md', '.json', '.txt') or not path.is_file():
                        raise ValueError('unsupported')
                    return self.send(200, path.read_bytes(), 'text/plain; charset=utf-8')
                except (ValueError, OSError):
                    return self.send(404, b'Livrable introuvable', 'text/plain')
            self.send(404, b'Introuvable', 'text/plain')
    return Handler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9013, help='port local ; 0 choisit un port libre')
    parser.add_argument('--root', type=Path, default=None, help='dossier des données (défaut : wiki/projets/team-strategie/data du coffre)')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), make_handler(args.root or team_root()))
    print(f'Team stratégie : http://127.0.0.1:{server.server_address[1]}/', flush=True)
    server.serve_forever()
