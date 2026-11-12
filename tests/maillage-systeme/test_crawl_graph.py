"""Le crawl de maillage compte les pages sources distinctes, pas les liens bruts.

Site fictif servi en local ; aucun accès réseau externe.
"""
import functools
import http.server
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'distribution' / 'skills' / 'maillage-systeme' / 'scripts' / 'crawl_graph.py'

PAGES = {
    'a.html': '<html><head><title>A</title></head><body><main><h1>Page A</h1>'
              '<p>Voir <a href="/c.html">le guide complet</a>, <a href="/c.html">la méthode détaillée</a> '
              'et <a href="/c.html">notre cas client</a>.</p></main></body></html>',
    'b.html': '<html><head><title>B</title></head><body><main><h1>Page B</h1>'
              '<p>Lire aussi <a href="/c.html">le guide</a> avant de commencer.</p></main></body></html>',
    'c.html': '<html><head><title>C</title></head><body><nav><a href="/d.html">Menu D</a></nav>'
              '<main><h1>Page C</h1><p>Retour à <a href="/a.html">la page A</a>.</p></main></body></html>',
    'd.html': '<html><head><title>D</title></head><body><main><h1>Page D</h1><p>Aucun lien dans le corps.</p></main></body></html>',
}


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class CrawlGraphTests(unittest.TestCase):
    def test_inbound_counts_distinct_source_pages(self):
        with tempfile.TemporaryDirectory() as site, tempfile.TemporaryDirectory() as out:
            for name, html in PAGES.items():
                (Path(site) / name).write_text(html, encoding='utf-8')
            handler = functools.partial(QuietHandler, directory=site)
            server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
            base = 'http://127.0.0.1:%d' % server.server_address[1]
            (Path(site) / 'sitemap.xml').write_text(
                '<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                + ''.join('<url><loc>%s/%s</loc></url>' % (base, name) for name in PAGES) + '</urlset>', encoding='utf-8')
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                done = subprocess.run([sys.executable, '-X', 'utf8', str(SCRIPT), base + '/sitemap.xml', '-o', out, '--delay', '0'],
                                      capture_output=True, text=True, encoding='utf-8', timeout=60)
            finally:
                server.shutdown()
                server.server_close()
            self.assertEqual(done.returncode, 0, done.stderr)
            index = json.loads((Path(out) / 'index.json').read_text(encoding='utf-8'))
            pages = {page['url'].rsplit('/', 1)[-1]: page for page in index['pages']}
            self.assertEqual(sorted(pages), ['a.html', 'b.html', 'c.html', 'd.html'])
            # C reçoit 3 liens de A et 1 lien de B : 2 pages sources, 4 liens.
            self.assertEqual(pages['c.html']['inbound_in_body'], 2)
            self.assertEqual(pages['c.html']['inbound_links_in_body'], 4)
            self.assertEqual((pages['a.html']['inbound_in_body'], pages['a.html']['inbound_links_in_body']), (1, 1))
            # Le lien du menu vers D ne compte pas : D reste orpheline, B aussi.
            self.assertEqual(pages['d.html']['inbound_in_body'], 0)
            self.assertEqual(sorted(url.rsplit('/', 1)[-1] for url in index['orphans']), ['b.html', 'd.html'])


if __name__ == '__main__':
    unittest.main()
