import base64, pathlib
src = pathlib.Path('guide.src.html').read_text()
for tok, f in (('__FONT_GEIST__','geist.woff2'), ('__FONT_MONO__','geist-mono.woff2')):
    b = base64.b64encode(pathlib.Path(f).read_bytes()).decode()
    src = src.replace(tok, 'data:font/woff2;base64,'+b)
out = pathlib.Path('systeme-seo-claude-obsidian.html')
out.write_text(src)
print(out, len(src)//1024, 'Ko')
