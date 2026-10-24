#!/usr/bin/env python3
# Builds EN/RU/NL/ZH pages for the TPF Labs site
import os, json

C = {
"en": {
 "title": "TPF Labs — CALIBER+ Autonomous Blueberry Harvester",
 "desc": "CALIBER+ by TPF Labs: autonomous selective blueberry harvester. 17 kg/h, >97% ripeness accuracy, 0% crop loss, 12–14 h autonomy. Pilot program for farms.",
 "nav": {"tech":"Technology","pilot":"Pilot","price":"Pricing","contact":"Contact"},
 "hero_tag": "TPF Labs · Autonomous Field Robotics",
 "h1": "Meet <b>CALIBER+</b> — the harvester that picks like hands, works like a machine",
 "lead": "An autonomous robot for selective harvesting of fresh-market blueberries. Two rows at once, berry by berry, with zero crop loss and 12–14 hours of daily autonomy.",
 "cta1": "Request a pilot", "cta2": "Technology",
 "stats": [("17 kg/h","picking rate per unit"),(">97%","ripeness accuracy"),("0%","crop loss (vs ~5% for harvesters)"),("12–14 h","daily autonomy")],
 "tech_h": "Engineered for fresh-market fruit",
 "tech_s": "Four SCARA arms, AI ripeness vision and a soft hybrid gripper treat every berry like a hand-picked one.",
 "cards": [
  ["🦾","Four SCARA arms","Two manipulators per side on vertical carriages pick from two rows simultaneously.","reach 800 mm · carriage stroke 1500 mm · cycle 0.5 s"],
  ["🧠","AI ripeness vision","Deep-learning detection finds every ripe berry and skips green ones — fresh-market quality, every pass.",">97% ripeness accuracy · depth cameras + LiDAR + RTK-GPS"],
  ["🫐","Gentle hybrid gripper","Silicone fingers with vacuum assist hold each berry with under 2 N of force. No bruising, no drops.","soft-touch ≤2 N · chilled 60 L hopper on board"],
  ["☀️","All-day autonomy","LiFePO4 power with a 600 W solar roof keeps the robot working through a full shift. Hot-swap batteries.","48 V LiFePO4 · tracked chassis for soft soil · 450 kg"],
 ],
 "pilot_h": "Pilot program: 30 / 60 / 90 days",
 "pilot_s": "No financial obligations until a season contract. We prove the numbers on your field, then you decide.",
 "steps": [
  ["Days 0–30","Row survey & mapping","We scan your rows, map the plot with RTK and calibrate the vision system for your varieties."],
  ["Days 30–60","Autonomous harvest on 1 ha","CALIBER+ works your plot; we measure ripeness, calibre, loss and cost per kg."],
  ["Days 60–90","Report & season contract","You get a full pilot report and an option to lock a RaaS tariff or purchase for season 2027."],
 ],
 "price_h": "Simple commercial model",
 "price_s": "Start without capital expenditure — rent for the season or buy.",
 "plans": [
  ["Robot-as-a-Service","€26,000 / season","hot",["Service, software and updates included","≈€1.9/kg vs ≈€2.4/kg manual picking","Hot-swap battery support at the base station","Season 2027 slots"]],
  ["Purchase","on request",["Prototype and pilot series timeline 2027–2028","CE certification under EU Machinery Regulation 2023/1230","Hybrid manufacturing: EU assembly, optimized mechanics","Commercial proposal on request"]],
 ],
 "contact_h": "Bring CALIBER+ to your field",
 "contact_s": "Pilot slots for season 2027 are open. Tell us about your farm — hectares, varieties, harvest window.",
 "mail": "drublev77@gmail.com",
 "site": "tpf-technology.com — parent company",
 "foot_l": "TPF Labs — autonomous robotics division of TPFtechnology.",
 "foot_r": "CALIBER+ is in pre-production. Photos show design concepts.",
},
"ru": {
 "title": "TPF Labs — автономный сборщик голубики CALIBER+",
 "desc": "CALIBER+ от TPF Labs: автономный селективный сборщик голубики. 17 кг/ч, точность спелости >97%, потери 0%, автономность 12–14 ч. Пилотная программа для хозяйств.",
 "nav": {"tech":"Технологии","pilot":"Пилот","price":"Цены","contact":"Контакты"},
 "hero_tag": "TPF Labs · Автономная полевая робототехника",
 "h1": "Знакомьтесь — <b>CALIBER+</b>: собирает как руки, работает как машина",
 "lead": "Автономный робот для селективного сбора свежей голубики на продажу. Два ряда одновременно, ягоду за ягодой, без потерь и с автономностью 12–14 часов в день.",
 "cta1": "Запросить пилот", "cta2": "Технологии",
 "stats": [("17 кг/ч","производительность машины"),(">97%","точность спелости"),("0%","потери (у комбайнов ~5%)"),("12–14 ч","автономность в день")],
 "tech_h": "Создан для ягоды свежего рынка",
 "tech_s": "Четыре SCARA-руки, ИИ-зрение спелости и мягкий гибридный захват обращаются с каждой ягодой как с ручным сбором.",
 "cards": [
  ["🦾","Четыре SCARA-руки","По два манипулятора на борт на вертикальных каретках собирают с двух рядов одновременно.","вылет 800 мм · ход каретки 1500 мм · цикл 0,5 с"],
  ["🧠","ИИ-зрение спелости","Нейросетевое распознавание находит каждую спелую ягоду и пропускает зелёную — качество свежего рынка в каждом проходе.",">97% точности · камеры глубины + лидар + RTK-GPS"],
  ["🫐","Мягкий гибридный захват","Силиконовые пальцы с вакуумной поддержкой держат ягоду с усилием менее 2 Н. Без деформации и осыпания.","мягкий захват ≤2 Н · охлаждаемый бункер 60 л"],
  ["☀️","Автономность весь день","LiFePO4 и солнечная крыша 600 Вт держат робота в работе всю смену. Горячая замена батарей.","48 В LiFePO4 · гусеничное шасси для мягких почв · 450 кг"],
 ],
 "pilot_h": "Пилотная программа: 30 / 60 / 90 дней",
 "pilot_s": "Никаких финансовых обязательств до сезонного контракта. Мы докажем цифры на твоём поле, а решение — за тобой.",
 "steps": [
  ["Дни 0–30","Обследование и картографирование","Сканируем ряды, снимаем RTK-карту участка и калибруем зрение под ваши сорта."],
  ["Дни 30–60","Автономный сбор на 1 га","CALIBER+ работает на участке; мы замеряем спелость, калибр, потери и стоимость кг."],
  ["Дни 60–90","Отчёт и сезонный контракт","Полный отчёт пилота и опция зафиксировать тариф RaaS или покупку на сезон 2027."],
 ],
 "price_h": "Простая коммерческая модель",
 "price_s": "Начните без капитальных вложений — аренда на сезон или покупка.",
 "plans": [
  ["Робот-как-Сервис (RaaS)","26 000 € / сезон","hot",["Сервис, ПО и обновления включены","≈1,9 €/кг против ≈2,4 €/кг ручного сбора","Горячая замена батарей на базовой станции","Слоты на сезон 2027"]],
  ["Покупка","по запросу",["Прототип и пилотная серия: 2027–2028","Сертификация CE по Регламенту ЕС 2023/1230","Гибридное производство: сборка в ЕС, оптимизированная механика","Коммерческое предложение по запросу"]],
 ],
 "contact_h": "Пригласите CALIBER+ на своё поле",
 "contact_s": "Слоты пилота на сезон 2027 открыты. Расскажите о хозяйстве: гектары, сорта, сроки уборки.",
 "mail": "drublev77@gmail.com",
 "site": "tpf-technology.com — материнская компания",
 "foot_l": "TPF Labs — дивизион автономной робототехники TPFtechnology.",
 "foot_r": "CALIBER+ находится в стадии подготовки к производству. Изображения — дизайнерские концепты.",
},
"nl": {
 "title": "TPF Labs — CALIBER+ autonome blauwe-bessenoogstrobot",
 "desc": "CALIBER+ van TPF Labs: autonome selectieve oogstrobot voor verse blauwe bessen. 17 kg/u, >97% nauwkeurigheid rijpheidsherkenning, 0% verlies, 12–14 uur autonomie. Pilotprogramma voor telers.",
 "nav": {"tech":"Technologie","pilot":"Pilot","price":"Prijzen","contact":"Contact"},
 "hero_tag": "TPF Labs · Autonome veldrobotica",
 "h1": "Maak kennis met <b>CALIBER+</b> — oogst zoals handmatig, werkt als een machine",
 "lead": "Een autonome robot voor selectieve oogst van verse blauwe bessen. Twee rijen tegelijk, bes voor bes, zonder verlies en 12–14 uur autonomie per dag.",
 "cta1": "Pilot aanvragen", "cta2": "Technologie",
 "stats": [("17 kg/u","oogsttempo per machine"),(">97%","nauwkeurigheid rijpheidsherkenning"),("0%","verlies (oogstmachines ~5%)"),("12–14 u","autonomie per dag")],
 "tech_h": "Gebouwd voor de versmarkt",
 "tech_s": "Vier SCARA-armen, AI-rijpheidsherkenning en een zachte hybride grijper behandelen elke bes als handgeplukt.",
 "cards": [
  ["🦾","Vier SCARA-armen","Twee manipulatoren per zijde op verticale sleden oogsten uit twee rijen tegelijk.","reikwijdte 800 mm · slede-slag 1500 mm · cyclus 0,5 s"],
  ["🧠","AI-rijpheidsherkenning","Deep learning vindt elke rijpe bes en laat groene staan — versmarktkwaliteit in elke passe.",">97% nauwkeurigheid · dieptecamera's + LiDAR + RTK-GPS"],
  ["🫐","Zachte hybride grijper","Siliconen vingers met vacuüm houden elke bes vast met minder dan 2 N. Geen beschadiging.","zachte greep ≤2 N · gekoelde 60 L hopper aan boord"],
  ["☀️","De hele dag autonomie","LiFePO4-voeding met een 600 W zonnendak houdt de robot aan het werk in een volledige shift. Hot-swap batterijen.","48 V LiFePO4 · rupschassis voor zachte grond · 450 kg"],
 ],
 "pilot_h": "Pilotprogramma: 30 / 60 / 90 dagen",
 "pilot_s": "Geen financiële verplichtingen vóór een seizoensovereenkomst. Wij bewijzen de cijfers op uw veld.",
 "steps": [
  ["Dag 0–30","Rij-scan en mapping","We scannen uw rijen, maken een RTK-kaart van het perceel en kalibreren de vision voor uw rassen."],
  ["Dag 30–60","Autonome oogst op 1 ha","CALIBER+ werkt op uw perceel; we meten rijpheid, kaliber, verlies en kosten per kg."],
  ["Dag 60–90","Rapport & seizoensovereenkomst","U ontvangt een volledig pilootrapport en de optie op een RaaS-tarief of aankoop voor seizoen 2027."],
 ],
 "price_h": "Simpel verdienmodel",
 "price_s": "Begin zonder investering — huur per seizoen of koop.",
 "plans": [
  ["Robot-as-a-Service","€26.000 / seizoen","hot",["Service, software en updates inbegrepen","≈€1,9/kg vs ≈€2,4/kg handmatig plukken","Hot-swap batterijen op het basisstation","Seizoen 2027 slots"]],
  ["Aankoop","op aanvraag",["Prototype- en pilotserie-tijdlijn 2027–2028","CE-certificering volgens EU Machinery Regulation 2023/1230","Hybride productie: EU-assemblage, geoptimaliseerde mechanica","Commercieel voorstel op aanvraag"]],
 ],
 "contact_h": "Breng CALIBER+ naar uw veld",
 "contact_s": "Pilot-slots voor seizoen 2027 zijn open. Vertel over uw bedrijf: hectaren, rassen, oogstperiode.",
 "mail": "drublev77@gmail.com",
 "site": "tpf-technology.com — moederbedrijf",
 "foot_l": "TPF Labs — divisie autonome robotica van TPFtechnology.",
 "foot_r": "CALIBER+ is in preproductie. Foto's tonen ontwerpconcepten.",
},
"zh": {
 "title": "TPF Labs — CALIBER+ 自主蓝莓采摘机器人",
 "desc": "TPF Labs 的 CALIBER+：面向鲜果市场的自主选择性蓝莓采摘机器人。17 公斤/小时，成熟度识别精度 >97%，损耗 0%，续航 12–14 小时。开放试点申请。",
 "nav": {"tech":"技术","pilot":"试点","price":"价格","contact":"联系"},
 "hero_tag": "TPF Labs · 自主田间机器人",
 "h1": "认识 <b>CALIBER+</b>：像双手一样轻采，像机器一样高效",
 "lead": "面向鲜果蓝莓市场的自主采摘机器人。同时采摘两行，逐颗识别，零损耗，每日续航 12–14 小时。",
 "cta1": "申请试点", "cta2": "技术",
 "stats": [("17 公斤/时","单机采摘速度"),(">97%","成熟度识别精度"),("0%","损耗（采收机约5%）"),("12–14 小时","每日续航")],
 "tech_h": "为鲜果市场而设计",
 "tech_s": "四条 SCARA 机械臂、AI 成熟度视觉和软性混合夹爪，像手工采摘一样对待每一颗浆果。",
 "cards": [
  ["🦾","四条 SCARA 机械臂","每侧两台机械臂安装于垂直滑座，可同时采摘两行。","臂展 800 毫米 · 滑座行程 1500 毫米 · 循环 0.5 秒"],
  ["🧠","AI 成熟度视觉","深度学习检测每一颗成熟浆果并跳过未熟的——每次作业都保持鲜果品质。",">97% 精度 · 深度相机 + 激光雷达 + RTK-GPS"],
  ["🫐","软性混合夹爪","带真空辅助的硅胶手指以小于 2 牛的力度托住每颗浆果。无损伤、无掉落。","软夹持 ≤2 牛 · 车载 60 升冷藏果箱"],
  ["☀️","全天自主作业","磷酸铁锂电池加 600 瓦太阳能顶棚，支持整班连续作业，支持热更换电池。","48 伏 LiFePO4 · 履带底盘适应松软土壤 · 450 公斤"],
 ],
 "pilot_h": "试点计划：30 / 60 / 90 天",
 "pilot_s": "在签署季节合同前无任何财务义务。我们用你田间的数据证明效果。",
 "steps": [
  ["第 0–30 天","行扫描与建图","扫描果行，用 RTK 绘制地块地图，并针对你的品种校准视觉系统。"],
  ["第 30–60 天","1 公顷自主采摘","CALIBER+ 在你的地块作业，我们测量成熟度、果径、损耗率和每公斤成本。"],
  ["第 60–90 天","报告与季节合同","获得完整试点报告，并可锁定 2027 季度的 RaaS 租赁或购买方案。"],
 ],
 "price_h": "简单的商业模式",
 "price_s": "无需设备投资即可启动——按季租赁或购买。",
 "plans": [
  ["机器人即服务（RaaS）","26,000 € / 季","hot",["含服务、软件与更新","约 1.9 €/公斤，人工约 2.4 €/公斤","基站支持电池热更换","2027 季度名额开放"]],
  ["购买","面议",["原型与试产线时间表 2027–2028","按欧盟机械法规 2023/1230 进行 CE 认证","混合制造：欧盟组装，优化的机械部件","商业方案可索取"]],
 ],
 "contact_h": "把 CALIBER+ 带到你的田间",
 "contact_s": "2027 季度试点名额已开放。请介绍你的农场：面积、品种、采收期。",
 "mail": "drublev77@gmail.com",
 "site": "tpf-technology.com — 母公司",
 "foot_l": "TPF Labs — TPFtechnology 旗下自主机器人部门。",
 "foot_r": "CALIBER+ 处于量产准备阶段。图片为设计概念图。",
},
}

TPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://tpflabs.com{suffix}">
<meta property="og:image" content="https://tpflabs.com/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="TPF Labs — CALIBER+ autonomous blueberry harvester">
<meta property="og:locale" content="{og_locale}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://tpflabs.com{suffix}">
<link rel="alternate" hreflang="en" href="https://tpflabs.com/">
<link rel="alternate" hreflang="ru" href="https://tpflabs.com/ru/">
<link rel="alternate" hreflang="nl" href="https://tpflabs.com/nl/">
<link rel="alternate" hreflang="zh" href="https://tpflabs.com/zh/">
<link rel="alternate" hreflang="x-default" href="https://tpflabs.com/">
<meta name="google-site-verification" content="Zr5OkmQBIum5PVhi6DNK-WUCK-wY8WJlHhbv-nSxepE">
<link rel="icon" href="/img/favicon-64.png" type="image/png" sizes="64x64">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header>
  <div class="wrap nav">
    <a class="logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo"> TPF<b>labs</b></a>
    <div class="links">
      <a href="#tech">{nav_tech}</a><a href="#pilot">{nav_pilot}</a><a href="#price">{nav_price}</a><a href="#contact">{nav_contact}</a>
    </div>
    <div class="langs">{langlinks}</div>
  </div>
</header>
<div class="hero">
  <div class="glow g1"></div><div class="glow g2"></div>
  <div class="wrap hero-flex"><div class="txt">
    <span class="tag">{hero_tag}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="cta-row">
      <a class="btn pri" href="mailto:{mail}?subject=CALIBER%2B%20pilot%20request">{cta1}</a>
      <a class="btn sec" href="#tech">{cta2}</a>
    </div>
  </div>
  <div class="hero-visual"><span class="c3"></span><img src="/img/hero.jpg" alt="CALIBER+ autonomous blueberry harvester concept render">
    <div class="hero-cap"><b>CALIBER+</b> · concept render · 1:2 row architecture</div>
  </div></div>
</div>
<div class="wrap"><div class="stats">
  {stats_html}
</div></div>
<section id="tech">
  <div class="wrap">
    <span class="over">{over_tech}</span><br><h2>{tech_h}</h2><p class="sub">{tech_s}</p>
    <div class="grid g4">{cards_html}</div>
  </div>
</section>
<section id="pilot" class="alt">
  <div class="wrap">
    <span class="over">{over_pilot}</span><br><h2>{pilot_h}</h2><p class="sub">{pilot_s}</p>
    <div class="steps">{steps_html}</div>
  </div>
</section>
<section id="price">
  <div class="wrap">
    <span class="over">{over_price}</span><br><h2>{price_h}</h2><p class="sub">{price_s}</p>
    <div class="price">{plans_html}</div>
  </div>
</section>
<section id="contact" class="alt contact">
  <div class="wrap">
    <span class="over">{over_contact}</span><br><h2>{contact_h}</h2>
    <p class="sub" style="margin-inline:auto">{contact_s}</p>
    <a class="bigmail" href="mailto:{mail}?subject=CALIBER%2B%20pilot%20request">{mail}</a>
    <p class="note"><a href="https://tpf-technology.com" target="_blank" rel="noopener">{site}</a></p>
  </div>
</section>
<footer>
  <div class="wrap">
  <img class="foot-logo" src="/img/logo.jpg" alt="TPFtechnology">
  <div class="frow">
    <span>{foot_l}</span><span>{foot_r}</span>
  </div>
  </div>
  <div class="frow badge-row">
    <a href="https://websitelaunches.com/site/tpflabs.com" target="_blank" rel="noopener">
      <img src="https://websitelaunches.com/badge/tpflabs.com.svg" alt="Website Launches — public launch record" width="255" height="55" loading="lazy">
    </a>
  </div>
</footer>
<script src="/site.js" defer></script>
<script src="/consent.js" defer></script>
</body>
</html>
"""

def page(c, lang):
    suffix = "/" if lang=="en" else "/"+lang+"/"
    langlinks = ""
    for l,label in [("en","EN"),("ru","RU"),("nl","NL"),("zh","中文")]:
        href = "/" if l=="en" else "/"+l+"/"
        cls = ' class="on"' if l==lang else ""
        langlinks += f'<a href="{href}"{cls}>{label}</a>'
    stats_html = "".join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in c["stats"])
    cards_html = "".join(f'<div class="card"><div class="ic">{ic}</div><h3>{h}</h3><p>{p}</p><div class="spec">{s}</div></div>' for ic,h,p,s in c["cards"])
    steps_html = "".join(f'<div class="step"><div class="num">{d}</div><h3>{t}</h3><p>{p}</p></div>' for d,t,p in c["steps"])
    plans_html = ""
    for plan in c["plans"]:
        name, pr, feats = plan[0], plan[1], plan[3] if len(plan)>3 and plan[2]=="hot" else plan[2]
        hot = ' hot' if (len(plan)>3 and plan[2]=="hot") else ''
        ul = "".join(f"<li>{f}</li>" for f in feats)
        plans_html += f'<div class="plan{hot}"><div class="ph">{name}</div><div class="pnum">{pr}</div><ul>{ul}</ul><a class="btn sec" href="mailto:{c["mail"]}?subject=CALIBER%2B">{ ("Request" if lang=="en" else ("Запрос" if lang=="ru" else ("Aanvraag" if lang=="nl" else "咨询"))) }</a></div>'
    html = TPL.format(
        lang=lang, brand="TPF", suffix=suffix, title=c["title"], desc=c["desc"],
        over_tech=c["nav"]["tech"], over_pilot=c["nav"]["pilot"], over_price=c["nav"]["price"], over_contact=c["nav"]["contact"],
        og_locale={"en":"en_US","ru":"ru_RU","nl":"nl_NL","zh":"zh_CN"}[lang],
        nav_tech=c["nav"]["tech"], nav_pilot=c["nav"]["pilot"], nav_price=c["nav"]["price"], nav_contact=c["nav"]["contact"],
        langlinks=langlinks, hero_tag=c["hero_tag"], h1=c["h1"], lead=c["lead"],
        mail=c["mail"], cta1=c["cta1"], cta2=c["cta2"], stats_html=stats_html,
        tech_h=c["tech_h"], tech_s=c["tech_s"], cards_html=cards_html,
        pilot_h=c["pilot_h"], pilot_s=c["pilot_s"], steps_html=steps_html,
        price_h=c["price_h"], price_s=c["price_s"], plans_html=plans_html,
        contact_h=c["contact_h"], contact_s=c["contact_s"], site=c["site"],
        foot_l=c["foot_l"], foot_r=c["foot_r"])
    return html

os.makedirs("out", exist_ok=True)
for lang in ["en","ru","nl","zh"]:
    p = "out/index.html" if lang=="en" else f"out/{lang}/index.html"
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p,"w",encoding="utf-8") as f:
        f.write(page(C[lang], lang))
    print("built", p)
