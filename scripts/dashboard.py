#!/usr/bin/env python3
"""Read-only local dashboard; no dependency outside Python."""
import argparse,html,json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs,quote

def serve(root,port):
 root=root.resolve()
 def allowed(rel):
  p=(root/rel).resolve()
  return p if any(p.is_relative_to((root/base).resolve()) for base in ['wiki','raw','.seokb/base']) and p.suffix=='.md' and p.is_relative_to(root) else None
 class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
   url=urlparse(self.path);qs=parse_qs(url.query);body=''
   if url.path=='/note':
    p=allowed(qs.get('path',[''])[0])
    if not p or not p.is_file():self.send_error(404);return
    body='<h2>'+html.escape(p.relative_to(root).as_posix())+'</h2><pre>'+html.escape(p.read_text(errors='replace'))+'</pre>'
   elif url.path=='/':
    query=qs.get('q',[''])[0].casefold();section=qs.get('section',['wiki'])[0]
    bases={'wiki':'wiki','sources':'raw','base':'.seokb/base/wiki','production':'wiki','recherche':'wiki'}
    base=root/bases.get(section,'wiki');paths=sorted(base.rglob('*.md')) if base.exists() else []
    if section=='production':paths=[p for p in paths if any(s in str(p) for s in ['brief','article','production','strategie'])]
    if section=='recherche':paths=[p for p in paths if any(s in str(p) for s in ['keyword','mot-cle','quer','recherche'])]
    paths=[p for p in paths if not query or query in p.name.casefold() or query in p.read_text(errors='replace').casefold()]
    state=json.loads((root/'.seokb/manifest.json').read_text())
    body='<h2>'+html.escape(root.name)+'</h2><p>SEOKB2 '+html.escape(state['version'])+' · '+str(len(paths))+' notes dans cette sélection.</p><p>Sources et productions personnelles conservées. Outils externes à connecter selon la mission. Aucun cron installé.</p>'
    body+='<form><input type="hidden" name="section" value="'+html.escape(section,quote=True)+'"><input name="q" placeholder="Rechercher dans les notes" value="'+html.escape(query,quote=True)+'"><button>Rechercher</button></form><ul>'
    for p in paths[:300]:
     rel=p.relative_to(root).as_posix();body+='<li><a href="/note?path='+quote(rel)+'">'+html.escape(rel)+'</a></li>'
    body+='</ul>'
    if len(paths)>300:body+='<p>Affichage limité à 300 notes. Préciser la recherche.</p>'
   else:self.send_error(404);return
   nav=' '.join('<a href="/?section='+k+'">'+label+'</a>' for k,label in [('wiki','Catalogue et journal'),('sources','Données et sources'),('recherche','Recherche'),('production','Production'),('base','Base SEO')])
   page='<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>SEOKB2 — Coffre</title><style>body{font:16px system-ui;color:#2b2b30;margin:0;background:#f6f7fc}header{background:linear-gradient(110deg,#2f4fe0,#7fa0ff);padding:32px;color:white}nav a{display:inline-block;color:white;margin:8px 24px 0 0}main{max-width:1100px;margin:32px auto;padding:24px;background:white;border:1px solid #dce2f5;border-radius:12px}a{color:#2444ce}li{margin:12px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px ui-monospace}input,button{padding:12px;border:1px solid #ccd4ec;border-radius:6px}input{width:60%}</style><header><h1>SEOKB2</h1><nav>'+nav+'</nav></header><main>'+body+'</main></html>'
   data=page.encode();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
 server=ThreadingHTTPServer(('127.0.0.1',port),Handler);print('http://127.0.0.1:'+str(server.server_port)+'/',flush=True);server.serve_forever()
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--target',type=Path,default=Path(__file__).resolve().parents[2]);ap.add_argument('--port',type=int,default=0);args=ap.parse_args();serve(args.target,args.port)
