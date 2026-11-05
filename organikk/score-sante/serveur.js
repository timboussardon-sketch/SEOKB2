const http = require('http'), fs = require('fs'), path = require('path');
const PORT = 4330;
http.createServer((req, res) => {
  const f = req.url === '/' || req.url.startsWith('/?') ? 'index.html' : req.url.split('?')[0].replace(/^\//, '');
  const p = path.join(__dirname, f);
  if (!p.startsWith(__dirname) || !fs.existsSync(p)) { res.writeHead(404); return res.end('non trouvé'); }
  res.writeHead(200, { 'content-type': f.endsWith('.json') ? 'application/json' : 'text/html; charset=utf-8', 'cache-control': 'no-store' });
  res.end(fs.readFileSync(p));
}).listen(PORT, () => console.log('http://localhost:' + PORT));
