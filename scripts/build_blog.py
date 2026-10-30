#!/usr/bin/env python3
"""Blog for the TPF Labs site: one page per finished article plus a language index.

Articles are markdown files in content/blog/<lang>/*.md with a small front matter
(title, description, date, lang, slug). The script writes

    blog/index.html                  EN index
    blog/<lang>/index.html           NL/RU/ZH indexes
    blog/<lang>/<slug>.html          one page per article
    sitemap-blog.xml                 every article + index

and keeps the same look as the rest of tpflabs.com (css/style.css).
Article pages carry Article + BreadcrumbList + FAQPage JSON-LD.
"""
from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "blog"
BASE = "https://tpflabs.com"
OG = {"en": "en_US", "ru": "ru_RU", "nl": "nl_NL", "zh": "zh_CN"}
UI = {
    "en": dict(blog="Blog", home="Home", back="← All articles", related="More articles", cta1="Request a pilot", cta2="Investor deck", lang_note=""),
    "nl": dict(blog="Blog", home="Home", back="← Alle artikelen", related="Meer artikelen", cta1="Pilot aanvragen", cta2="Investeerdersdeck", lang_note="Dit artikel is in het Engels beschikbaar."),
    "ru": dict(blog="Блог", home="Главная", back="← Все статьи", related="Другие статьи", cta1="Запросить пилот", cta2="Инвесторская дека", lang_note="Эта статья доступна на английском."),
    "zh": dict(blog="博客", home="首页", back="← 所有文章", related="更多文章", cta1="申请试点", cta2="投资人资料", lang_note="本文暂为英文版本。"),
}
MAIL = "drublev77@gmail.com"


def parse(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta, body = {}, raw
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        body = m.group(2)
    meta.setdefault("slug", path.stem)
    meta.setdefault("lang", path.parent.name)
    meta.setdefault("date", date.today().isoformat())
    meta["body"] = body.strip()
    return meta


def inline(t: str) -> str:
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def md_to_html(md: str) -> tuple[str, list[tuple[str, str]]]:
    """Returns (html, faq) where faq is [(question, answer)] harvested from the last H2 'FAQ'."""
    out, para, i = [], [], 0
    faq: list[tuple[str, str]] = []
    in_faq = False
    pending_q = None
    lines = md.splitlines()

    def flush():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    tbl: list[list[str]] = []

    def flush_table():
        nonlocal tbl
        if not tbl:
            return
        rows = tbl
        head_row = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
        body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
        out.append(f"<table><thead><tr>{head_row}</tr></thead><tbody>{body}</tbody></table>")
        tbl = []

    for ln in lines:
        s = ln.rstrip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            tbl.append(cells)
            continue
        if tbl:
            flush_table()
        if s.startswith("# "):
            flush(); continue  # h1 comes from front matter
        if s.startswith("## "):
            flush()
            title = s[3:].strip()
            in_faq = title.upper().startswith("FAQ")
            out.append(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")}">{inline(title)}</h2>')
            continue
        if s.startswith("### "):
            flush(); out.append(f"<h3>{inline(s[4:])}</h3>"); continue
        if re.match(r"^\d+\.\s", s):
            flush()
            if not (out and out[-1].startswith("<ol")):
                out.append("<ol>")
            out.append("<li>" + inline(re.sub(r"^\d+\.\s+", "", s)) + "</li>")
            continue
        if s.startswith("- "):
            flush()
            if not (out and out[-1].startswith("<ul")):
                out.append("<ul>")
            out.append("<li>" + inline(s[2:]) + "</li>")
            continue
        if not s:
            flush()
            if out and out[-1] in ("<ol>", "<ul>") or (out and out[-1].startswith("<li>")):
                pass
            continue
        if in_faq and s.startswith("**") and s.endswith("**"):
            flush()
            pending_q = s.strip("*").strip()
            continue
        if in_faq and pending_q and not s.startswith("#"):
            faq.append((pending_q, re.sub(r"\s+", " ", s).strip()))
            pending_q = None
            continue
        para.append(s)
    flush()
    flush_table()
    # close lists
    fixed = []
    for chunk in out:
        if chunk == "<ol>":
            fixed.append("<ol>")
        elif chunk == "<ul>":
            fixed.append("<ul>")
        else:
            if fixed and fixed[-1].startswith("<li>") is False and fixed[-1] in ("<ol>", "<ul>"):
                pass
            fixed.append(chunk)
    # join list items properly
    res, buf, tag = [], [], None
    for chunk in fixed:
        if chunk in ("<ol>", "<ul>"):
            tag = chunk[1:3]
            buf = []
            continue
        if chunk.startswith("<li>"):
            buf.append(chunk)
            continue
        if tag:
            res.append(f"<{tag}>" + "".join(buf) + f"</{tag}>")
            tag, buf = None, []
        res.append(chunk)
    if tag:
        res.append(f"<{tag}>" + "".join(buf) + f"</{tag}>")
    return "\n".join(res), faq


def head(lang: str, title: str, desc: str, canon: str, extra_ld: str = "", page_type: str = "website") -> str:
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#070b14">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="{page_type}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://tpflabs.com/img/og.png">
<meta property="og:locale" content="{OG[lang]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{canon}">
<script type="application/ld+json">{extra_ld}</script>
<link rel="icon" href="/img/favicon-64.png" type="image/png" sizes="64x64">
<link rel="stylesheet" href="/css/style.css">
</head>'''

NAV = '''<body>
<header>
  <div class="wrap nav">
    <a class="logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo"> TPF<b>labs</b></a>
    <div class="links">
      <a href="/#{lang}/">{tech}</a><a href="/#{lang}/pilot">{pilot}</a><a href="/#{lang}/price">{price}</a><a href="/blog{langpath}">blog</a>
    </div>
    <div class="langs">{langlinks}</div>
  </div>
</header>'''

NAVLABELS = {
    "en": ("Technology", "Pilot", "Pricing"),
    "ru": ("Технологии", "Пилот", "Цены"),
    "nl": ("Technologie", "Pilot", "Prijzen"),
    "zh": ("技术", "试点", "价格"),
}

FOOT = f'''<footer>
  <div class="wrap">
  <a class="logo foot-logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo" loading="lazy" decoding="async"> TPF<b>labs</b></a>
  <div class="frow"><span>TPF Labs — autonomous robotics division of TPFtechnology.</span><span>CALIBER+ is in pre-production. Photos show design concepts.</span></div>
  </div>
</footer>
<script src="/consent.js" defer></script>
</body>
</html>'''


def nav_html(lang: str) -> str:
    tech, pilot, price = NAVLABELS[lang]
    langpath = "/" if lang == "en" else f"/{lang}/"
    links = ""
    for l, label in [("en", "EN"), ("ru", "RU"), ("nl", "NL"), ("zh", "中文")]:
        href = "/" if l == "en" else f"/{l}/"
        cls = ' class="on"' if l == lang else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    return (NAV.replace("{lang}/", "" if lang == "en" else f"{lang}/")
               .replace("{tech}", tech).replace("{pilot}", pilot).replace("{price}", price)
               .replace("{langpath}", langpath).replace("{langlinks}", links))


def article_page(meta: dict, related: list[dict]) -> str:
    lang = meta["lang"]
    ui = UI[lang]
    body_html, faq = md_to_html(meta["body"])
    canon = f"{BASE}/blog/{lang}/{meta['slug']}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": meta["title"], "description": meta["description"],
         "datePublished": meta["date"], "dateModified": meta["date"], "inLanguage": lang,
         "author": {"@type": "Organization", "name": "TPF Labs"},
         "publisher": {"@type": "Organization", "name": "TPF Labs", "logo": {"@type": "ImageObject", "url": "https://tpflabs.com/img/logo-icon.png"}},
         "mainEntityOfPage": canon},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home"], "item": f"{BASE}/" if lang == "en" else f"{BASE}/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog/{'' if lang == 'en' else lang + '/'}"},
            {"@type": "ListItem", "position": 3, "name": meta["title"]}]},
    ]}
    if faq:
        ld["@graph"].append({"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    rel = "".join(f'<li><a href="/blog/{lang}/{r["slug"]}/">{html.escape(r["title"])}</a></li>' for r in related)
    return f'''{head(lang, meta["title"], meta["description"], canon, json.dumps(ld, ensure_ascii=False), "article")}
{nav_html(lang)}
<main class="wrap article">
  <p class="crumb"><a href="/blog/{'' if lang == 'en' else lang + '/'}">{ui["back"]}</a></p>
  <h1>{html.escape(meta["title"])}</h1>
  <p class="meta"><time datetime="{meta["date"]}">{meta["date"]}</time> · TPF Labs</p>
  {body_html}
  <div class="cta-row" style="margin-top:36px">
    <a class="btn pri" href="mailto:{MAIL}?subject=CALIBER%2B%20pilot%20request">{ui["cta1"]}</a>
    <a class="btn sec" href="/caliber-investor-deck.pdf" target="_blank" rel="noopener">{ui["cta2"]}</a>
  </div>
  {f'<h2>{ui["related"]}</h2><ul class="rel">{rel}</ul>' if rel else ''}
</main>
{FOOT}'''


def index_page(lang: str, arts: list[dict], all_en: list[dict]) -> str:
    ui = UI[lang]
    canon = f"{BASE}/blog/{'' if lang == 'en' else lang + '/'}"
    items = arts or all_en
    note = "" if arts else f'<p class="sub">{ui["lang_note"]}</p>'
    cards = "".join(
        f'<div class="card"><h3><a href="/blog/{a["lang"]}/{a["slug"]}/">{html.escape(a["title"])}</a></h3>'
        f'<p>{html.escape(a["description"])}</p><div class="spec">{a["date"]}</div></div>' for a in items)
    ld = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "TPF Labs Blog",
                     "url": canon, "inLanguage": lang}, ensure_ascii=False)
    return f'''{head(lang, "Blog — TPF Labs · CALIBER+ field robotics", "Articles on blueberry harvesting machines, robotic picking, farm economics and agricultural robotics.", canon, ld)}
{nav_html(lang)}
<main class="wrap article">
  <h1>Blog</h1>
  {note}
  <div class="grid g3">{cards}</div>
</main>
{FOOT}'''


def main() -> None:
    arts: dict[str, list[dict]] = {}
    for lang_dir in sorted(SRC.glob("*")):
        if not lang_dir.is_dir():
            continue
        arts[lang_dir.name] = [parse(p) for p in sorted(lang_dir.glob("*.md"))]
    all_en = arts.get("en", [])
    sitemap_rows = []
    (ROOT / "blog").mkdir(exist_ok=True)
    for lang in ["en", "ru", "nl", "zh"]:
        items = arts.get(lang, [])
        outdir = ROOT / "blog" / lang
        outdir.mkdir(parents=True, exist_ok=True)
        idx = index_page(lang, items, all_en)
        (outdir / "index.html").write_text(idx, encoding="utf-8")
        if lang == "en":
            (ROOT / "blog" / "index.html").write_text(idx, encoding="utf-8")
        url = f"{BASE}/blog/{'' if lang == 'en' else lang + '/'}"
        sitemap_rows.append(f"  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>")
        print("built", outdir / "index.html")
        for meta in items:
            related = [a for a in items if a["slug"] != meta["slug"]][:3]
            (outdir / meta["slug"]).mkdir(parents=True, exist_ok=True)
            (outdir / meta["slug"] / "index.html").write_text(article_page(meta, related), encoding="utf-8")
            sitemap_rows.append(f"  <url><loc>{BASE}/blog/{lang}/{meta['slug']}/</loc><lastmod>{meta['date']}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>")
            print("built", outdir / meta["slug"] / "index.html")
    (ROOT / "sitemap-blog.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(sitemap_rows) + "\n</urlset>\n", encoding="utf-8")
    print("built sitemap-blog.xml")


if __name__ == "__main__":
    main()
