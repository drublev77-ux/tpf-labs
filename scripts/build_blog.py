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
LANGS = [("en", "EN"), ("ru", "RU"), ("nl", "NL"), ("pl", "PL"), ("zh", "中文")]
OG = {"en": "en_US", "ru": "ru_RU", "nl": "nl_NL", "pl": "pl_PL", "zh": "zh_CN"}
UI = {
    "en": dict(idx_title="Blog: blueberry harvesters & farm robots | TPF Labs", idx_desc="Practical articles on blueberry harvesting machines, picking robots, cost per kilogram and labour on fresh-market berry farms.", foot_l="TPF Labs — autonomous robotics division of TPFtechnology.", foot_r="CALIBER+ is in pre-production. Photos show design concepts.", blog="Blog", home="Home", back="← All articles", related="More articles", cta1="Request a pilot", cta2="Investor deck", lang_note="", og_alt="CALIBER+ autonomous blueberry harvesting robot by TPF Labs"),
    "nl": dict(idx_title="Blog: blauwe bessen oogsten & oogstrobots | TPF Labs", idx_desc="Artikelen over oogstmachines en plukrobots voor blauwe bessen, kosten per kilo en arbeid op bessenbedrijven.", foot_l="TPF Labs — divisie autonome robotica van TPFtechnology.", foot_r="CALIBER+ is in preproductie. Foto's tonen ontwerpconcepten.", blog="Blog", home="Home", back="← Alle artikelen", related="Meer artikelen", cta1="Pilot aanvragen", cta2="Investeerdersdeck", lang_note="Onze artikelen zijn voorlopig in het Engels beschikbaar.", og_alt="CALIBER+ autonome oogstrobot voor blauwe bessen van TPF Labs"),
    "ru": dict(idx_title="Блог: машины и роботы для сбора голубики | TPF Labs", idx_desc="Статьи о комбайнах и роботах для сбора голубики, стоимости уборки за килограмм и нехватке сборщиков в ягодных хозяйствах.", foot_l="TPF Labs — дивизион автономной робототехники TPFtechnology.", foot_r="CALIBER+ находится в стадии подготовки к производству. Изображения — дизайнерские концепты.", blog="Блог", home="Главная", back="← Все статьи", related="Другие статьи", cta1="Запросить пилот", cta2="Инвесторская дека", lang_note="Статьи пока доступны на английском языке.", og_alt="CALIBER+ — автономный робот для сбора голубики от TPF Labs"),
    "pl": dict(idx_title="Blog: kombajny i roboty do zbioru borówki | TPF Labs", idx_desc="Artykuły o kombajnach i robotach do zbioru borówki amerykańskiej, koszcie zbioru za kilogram i braku rąk do pracy na plantacjach.", foot_l="TPF Labs — dział autonomicznej robotyki TPFtechnology.", foot_r="CALIBER+ jest na etapie przygotowania do produkcji. Zdjęcia przedstawiają koncepcje projektowe.", blog="Blog", home="Strona główna", back="← Wszystkie artykuły", related="Więcej artykułów", cta1="Zgłoś się do pilotażu", cta2="Prezentacja dla inwestorów", lang_note="Artykuły są na razie dostępne w języku angielskim.", og_alt="CALIBER+ — autonomiczny robot do zbioru borówki od TPF Labs"),
    "zh": dict(idx_title="博客：蓝莓采摘机与农业机器人 | TPF Labs", idx_desc="关于蓝莓采摘机、采摘机器人、每公斤采收成本和浆果农场劳动力的文章。", foot_l="TPF Labs — TPFtechnology 旗下自主机器人部门。", foot_r="CALIBER+ 处于量产准备阶段。图片为设计概念图。", blog="博客", home="首页", back="← 所有文章", related="更多文章", cta1="申请试点", cta2="投资人资料", lang_note="文章暂时仅提供英文版本。", og_alt="TPF Labs 的 CALIBER+ 自主蓝莓采摘机器人"),
}
MAIL = "orders@tpf-technology.com"

# Public sources behind the sector figures. Labels are localised, URLs are shared.
SOURCE_HEAD = {
    "en": "Sources and data behind the figures",
    "ru": "Источники и данные под цифрами",
    "nl": "Bronnen en cijfers achter de cijfers",
    "pl": "Źródła i dane stojące za liczbami",
    "zh": "数据来源与依据",
}
SOURCE_NOTE = {
    "en": "Cost models in this article are TPF Labs calculations. Sector inputs come from these public sources; each cost figure is reproducible from them.",
    "ru": "Расчёты стоимости в статье — наши собственные. Отраслевые вводные взяты из этих публичных источников, и каждую цифру можно воспроизвести по ним.",
    "nl": "De kostenmodellen in dit artikel zijn berekeningen van TPF Labs. Sectorgegevens komen uit deze openbare bronnen; elk kostencijfer is daaruit te reproduceren.",
    "pl": "Modele kosztowe w tym artykule to obliczenia TPF Labs. Dane sektorowe pochodzą z tych publicznych źródeł i każdą kwotę można na ich podstawie odtworzyć.",
    "zh": "本文的成本模型为 TPF Labs 自行计算，行业数据取自以下公开来源，每一项成本均可据此复核。",
}
SOURCES = [
    ("ILVO — Institute for Agricultural, Fisheries and Food Research", "https://ilvo.vlaanderen.be/en"),
    ("AgriFoodTEF — EU test and experimentation facilities for agri-food", "https://agrifoodtef.eu/"),
    ("Eurostat — agricultural labour input and income indicators", "https://ec.europa.eu/eurostat"),
    ("FAO — agricultural labour and harvest mechanisation", "https://www.fao.org/home/en"),
]


HOME_LINKS = {
    "en": ("What the machine costs and how a pilot works:", "pricing", "pilot program"),
    "ru": ("Сколько стоит машина и как проходит пилот:", "цены", "пилотная программа"),
    "nl": ("Wat de machine kost en hoe een pilot werkt:", "prijzen", "pilotprogramma"),
    "pl": ("Ile kosztuje maszyna i jak wygląda pilotaż:", "ceny", "program pilotażowy"),
    "zh": ("机器价格与试点流程：", "价格", "试点计划"),
}



def alternates_html(pairs):
    """hreflang cluster: one link per language plus x-default on the English page."""
    if not pairs:
        return ""
    out = [f'<link rel="alternate" hreflang="{hl}" href="{url}">' for hl, url in pairs]
    default = dict(pairs).get("en") or pairs[0][1]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{default}">')
    return "\n".join(out)


GROUPS = {}

# H1 and intro paragraph on each blog index
INTRO = {'en': ('Blueberry harvesting machines and robots: costs, types and field economics', 'Guides for fresh-market blueberry growers: what each kind of harvesting machine costs per kilogram, where selective picking robots stand today and how to test one on your own rows before you commit.'), 'ru': ('Машины и роботы для сбора голубики: цены, виды и экономика уборки', 'Материалы для хозяйств, выращивающих голубику на свежий рынок: сколько стоит машинная уборка за килограмм, чем селективный робот отличается от комбайна и как проверить его на своём поле.'), 'nl': ('Oogstmachines en plukrobots voor blauwe bessen: kosten en soorten', 'Gidsen voor telers van verse blauwe bessen: wat elk type oogstmachine per kilo kost, waar selectieve plukrobots nu staan en hoe u er een op uw eigen rijen test.'), 'pl': ('Kombajny i roboty do zbioru borówki: ceny, rodzaje i ekonomika zbioru', 'Poradniki dla plantatorów borówki amerykańskiej na rynek świeży: ile kosztuje zbiór maszynowy w przeliczeniu na kilogram, czym robot selektywny różni się od kombajnu i jak sprawdzić go na własnej plantacji.'), 'zh': ('蓝莓采摘机与采摘机器人：价格、类型与采收经济性', '面向鲜果蓝莓种植者的指南：各类采摘机每公斤成本、选择性采摘机器人的现状，以及如何在自己的果园先行测试。')}


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
    """Returns (html, faq). Questions under an H2 'FAQ' (bold line + answer) are rendered
    as visible <details> blocks and also returned for FAQPage JSON-LD."""
    out: list[str] = []
    faq: list[tuple[str, str]] = []
    para: list[str] = []
    tbl: list[list[str]] = []
    lst: list[str] = []
    lst_tag: str | None = None
    in_faq = False
    pending_q: str | None = None

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def flush_list():
        nonlocal lst, lst_tag
        if lst_tag:
            out.append(f"<{lst_tag}>" + "".join(lst) + f"</{lst_tag}>")
        lst, lst_tag = [], None

    def flush_table():
        nonlocal tbl
        if tbl:
            head_row = "".join(f"<th>{inline(c)}</th>" for c in tbl[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in tbl[1:])
            out.append(f"<table><thead><tr>{head_row}</tr></thead><tbody>{body}</tbody></table>")
            tbl = []

    def flush_all():
        flush_para(); flush_list(); flush_table()

    def add_item(tag: str, text: str):
        nonlocal lst_tag
        flush_para(); flush_table()
        if lst_tag != tag:
            flush_list()
            lst_tag = tag
        lst.append("<li>" + inline(text) + "</li>")

    faq_html: list[str] = []

    def flush_faq():
        if faq_html:
            out.append('<div class="faq">' + "".join(faq_html) + "</div>")
            faq_html.clear()

    for ln in md.splitlines():
        s = ln.rstrip()
        if s.startswith("|"):
            flush_para(); flush_list()
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                tbl.append(cells)
            continue
        flush_table()
        if s.startswith("# "):
            flush_all(); continue  # h1 comes from front matter
        if s.startswith("## "):
            flush_all(); flush_faq()
            title = s[3:].strip()
            in_faq = title.upper().startswith("FAQ")
            out.append(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")}">{inline(title)}</h2>')
            continue
        if s.startswith("### "):
            flush_all(); out.append(f"<h3>{inline(s[4:])}</h3>"); continue
        if in_faq:
            if not s:
                continue
            if s.startswith("**") and s.endswith("**"):
                pending_q = s.strip("*").strip()
                continue
            if pending_q:
                a = re.sub(r"\s+", " ", s).strip()
                faq.append((pending_q, a))
                faq_html.append(f"<details><summary>{inline(pending_q)}</summary><p>{inline(a)}</p></details>")
                pending_q = None
                continue
        m = re.match(r"^\d+\.\s+(.*)$", s)
        if m:
            add_item("ol", m.group(1)); continue
        if s.startswith("- "):
            add_item("ul", s[2:]); continue
        if not s:
            flush_para(); flush_list(); continue
        flush_list()
        para.append(s)
    flush_all(); flush_faq()
    return "\n".join(out), faq


def head(lang: str, title: str, desc: str, canon: str, extra_ld: str = "", page_type: str = "website",
         robots: str = "index,follow,max-image-preview:large,max-snippet:-1", alternates: str = "", extra_meta: str = "") -> str:
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
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(UI[lang]["og_alt"])}">
<meta property="og:site_name" content="TPF Labs">
<meta property="og:locale" content="{OG[lang]}">
{extra_meta}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="https://tpflabs.com/img/og.png">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
{alternates}
<script type="application/ld+json">{extra_ld}</script>
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/img/favicon-64.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/css/style.css">
</head>'''

NAV = '''<body>
<header>
  <div class="wrap nav">
    <a class="logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo"> TPF<b>labs</b></a>
    <div class="links">
      <a href="/{lang}/#tech">{tech}</a><a href="/{lang}/#pilot">{pilot}</a><a href="/{lang}/#price">{price}</a><a href="/blog{langpath}">{bloglabel}</a>
    </div>
    <div class="langs">{langlinks}</div>
  </div>
</header>'''

NAVLABELS = {
    "en": ("Technology", "Pilot", "Pricing"),
    "ru": ("Технологии", "Пилот", "Цены"),
    "nl": ("Technologie", "Pilot", "Prijzen"),
    "pl": ("Technologia", "Pilotaż", "Ceny"),
    "zh": ("技术", "试点", "价格"),
}

FOOT_TPL = '''<footer>
  <div class="wrap">
  <a class="logo foot-logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo" loading="lazy" decoding="async"> TPF<b>labs</b></a>
  <div class="frow"><span>{foot_l}</span><span>{foot_r}</span></div>
  </div>
</footer>
<script src="/consent.js" defer></script>
</body>
</html>'''


def foot(lang: str) -> str:
    return FOOT_TPL.replace("{foot_l}", UI[lang]["foot_l"]).replace("{foot_r}", UI[lang]["foot_r"])


def nav_html(lang: str) -> str:
    tech, pilot, price = NAVLABELS[lang]
    langpath = "/" if lang == "en" else f"/{lang}/"
    links = ""
    for l, label in LANGS:
        href = "/" if l == "en" else f"/{l}/"
        cls = ' class="on"' if l == lang else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    return (NAV.replace("/{lang}/", "/" if lang == "en" else f"/{lang}/").replace("{bloglabel}", UI[lang]["blog"])
               .replace("{tech}", tech).replace("{pilot}", pilot).replace("{price}", price)
               .replace("{langpath}", langpath).replace("{langlinks}", links))


def article_page(meta: dict, related: list[dict]) -> str:
    lang = meta["lang"]
    ui = UI[lang]
    body_html, faq = md_to_html(meta["body"])
    canon = f"{BASE}/blog/{lang}/{meta['slug']}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": meta["title"], "description": meta["description"],
         "datePublished": meta["date"], "dateModified": meta.get("updated", meta["date"]), "inLanguage": lang,
         "image": ["https://tpflabs.com/img/og.png", "https://tpflabs.com/img/hero.jpg"],
         "author": {"@type": "Organization", "@id": "https://tpflabs.com/#org", "name": "TPF Labs", "url": "https://tpflabs.com/"},
         "publisher": {"@type": "Organization", "@id": "https://tpflabs.com/#org", "name": "TPF Labs", "logo": {"@type": "ImageObject", "url": "https://tpflabs.com/apple-touch-icon.png", "width": 180, "height": 180}},
         "about": {"@id": "https://tpflabs.com/#caliber"},
         "mainEntityOfPage": {"@type": "WebPage", "@id": canon}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home"], "item": f"{BASE}/" if lang == "en" else f"{BASE}/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog/{'' if lang == 'en' else lang + '/'}"},
            {"@type": "ListItem", "position": 3, "name": meta["title"]}]},
    ]}
    if faq:
        ld["@graph"].append({"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    _onpage, _price, _pilot = HOME_LINKS[lang]
    sources_list = "".join(
        f'<li><a href="{url}" target="_blank" rel="noopener">{label}</a></li>'
        for label, url in SOURCES)
    _home = "/" if lang == "en" else f"/{lang}/"
    links_html = (f'<p class="sub" style="margin-top:28px">{_onpage} '
                  f'<a href="{_home}#price">{_price}</a> · '
                  f'<a href="{_home}#pilot">{_pilot}</a></p>')
    rel = "".join(f'<li><a href="/blog/{lang}/{r["slug"]}/">{html.escape(r["title"])}</a></li>' for r in related)
    art_meta = (f'<meta property="article:published_time" content="{meta["date"]}">\n'
                f'<meta property="article:modified_time" content="{meta.get("updated", meta["date"])}">\n'
                '<meta property="article:author" content="TPF Labs">')
    group = meta.get("group")
    siblings = GROUPS.get(group, []) if group else []
    if siblings:
        pairs = [(m["lang"], f"{BASE}/blog/{m['lang']}/{m['slug']}/") for m in sorted(siblings, key=lambda m: m["lang"])]
    else:
        pairs = [(lang, canon)]
    alt = alternates_html(pairs)
    return f'''{head(lang, meta.get("seo_title", meta["title"]), meta["description"], canon, json.dumps(ld, ensure_ascii=False), "article", alternates=alt, extra_meta=art_meta)}
{nav_html(lang)}
<main class="wrap article">
  <p class="crumb"><a href="/blog/{'' if lang == 'en' else lang + '/'}">{ui["back"]}</a></p>
  <h1>{html.escape(meta["title"])}</h1>
  <p class="meta"><time datetime="{meta["date"]}">{meta["date"]}</time> · TPF Labs</p>
  {body_html}
  <div class="sources" style="margin-top:32px">
    <h2>{SOURCE_HEAD[lang]}</h2>
    <ul>{sources_list}</ul>
    <p class="sub">{SOURCE_NOTE[lang]}</p>
  </div>
  {links_html}
  <div class="cta-row" style="margin-top:36px">
    <a class="btn pri" href="mailto:{MAIL}?subject=CALIBER%2B%20pilot%20request">{ui["cta1"]}</a>
    <a class="btn sec" href="/caliber-investor-deck.pdf" target="_blank" rel="noopener">{ui["cta2"]}</a>
  </div>
  {f'<h2>{ui["related"]}</h2><ul class="rel">{rel}</ul>' if rel else ''}
</main>
{foot(lang)}'''


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
    robots = "index,follow" if arts else "noindex,follow"
    idx_pairs = [(l, f"{BASE}/blog/{'' if l == 'en' else l + '/'}") for l, _ in LANGS]
    return f'''{head(lang, ui["idx_title"], ui["idx_desc"], canon, ld, robots=robots, alternates=alternates_html(idx_pairs))}
{nav_html(lang)}
<main class="wrap article">
  <h1>{INTRO[lang][0]}</h1>
  <p class="sub">{INTRO[lang][1]}</p>
  {note}
  <div class="grid g3">{cards}</div>
</main>
{foot(lang)}'''


def main() -> None:
    arts: dict[str, list[dict]] = {}
    for lang_dir in sorted(SRC.glob("*")):
        if not lang_dir.is_dir():
            continue
        arts[lang_dir.name] = [parse(p) for p in sorted(lang_dir.glob("*.md"))]
    all_en = arts.get("en", [])
    for lang_arts in arts.values():
        for m in lang_arts:
            if m.get("group"):
                GROUPS.setdefault(m["group"], []).append(m)
    sitemap_rows = []
    (ROOT / "blog").mkdir(exist_ok=True)
    for lang in [l for l, _ in LANGS]:
        items = arts.get(lang, [])
        outdir = ROOT / "blog" / lang
        outdir.mkdir(parents=True, exist_ok=True)
        idx = index_page(lang, items, all_en)
        (outdir / "index.html").write_text(idx, encoding="utf-8")
        if lang == "en":
            (ROOT / "blog" / "index.html").write_text(idx, encoding="utf-8")
        url = f"{BASE}/blog/{'' if lang == 'en' else lang + '/'}"
        if items:
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
