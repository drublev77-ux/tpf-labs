# TPF Labs — tpflabs.com

Static site for the **CALIBER+** autonomous blueberry harvester by TPF Labs (TPFtechnology).

## Structure
- `index.html` — English (default)
- `ru/index.html` — Русский
- `nl/index.html` — Nederlands
- `pl/index.html` — Polski
- `zh/index.html` — 中文
- `blog/` — articles, generated from `content/blog/<lang>/*.md`
- `css/style.css`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `consent.js` (GDPR-gated GA4), `img/og.png` (social card)

## Rebuild
Language pages are generated from one template:
```
python3 build.py            # language pages + sitemap.xml, written in place
python3 scripts/build_blog.py  # blog pages + sitemap-blog.xml
```

## Deploy
Push to `main` → Vercel picks it up (project: tpflabs.com).

Contact: orders@tpf-technology.com · https://tpf-technology.com
