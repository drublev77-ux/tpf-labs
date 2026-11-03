#!/usr/bin/env python3
# Builds EN/RU/NL/ZH pages for the TPF Labs site
import os, json

# Site languages in switcher order: (code, label). EN is served at /, others at /<code>/
LANGS = [("en","EN"),("ru","RU"),("nl","NL"),("pl","PL"),("zh","中文")]
CODES = [l for l, _ in LANGS]

# Contact address for pilot requests, used on every page and in structured data
MAIL = "orders@tpf-technology.com"  # switch to pilot@tpflabs.com once its mail forwarding works

C = {
"en": {
 "title": "CALIBER+ Blueberry Harvesting Robot | TPF Labs",
 "desc": "Autonomous blueberry harvesting robot for fresh-market farms: designed for 17 kg/h with zero loss at ≈€1.9/kg. From €26,000 per season. 2027 pilots open.",
 "nav": {"tech":"Technology","pilot":"Pilot","price":"Pricing","contact":"Contact"},
 "hero_tag": "TPF Labs · Autonomous Field Robotics",
 "h1": "<b>CALIBER+</b> blueberry harvesting robot — picks like hands, works like a machine",
 "lead": "An autonomous robot for selective harvesting of fresh-market blueberries. Two rows at once, berry by berry, designed for zero crop loss and 12–14 hours of daily autonomy.",
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
  ["Purchase","from €80,000",["Prototype and pilot series timeline 2027–2028","CE certification under EU Machinery Regulation 2023/1230","Hybrid manufacturing: EU assembly, optimized mechanics","Commercial proposal on request"]],
 ],
 "contact_h": "Bring CALIBER+ to your field",
 "contact_s": "Pilot slots for season 2027 are open. Tell us about your farm — hectares, varieties, harvest window.",
 "mail": MAIL,
 "site": "tpf-technology.com — parent company",
 "foot_l": "TPF Labs — autonomous robotics division of TPFtechnology.",
 "foot_r": "CALIBER+ is in pre-production. Photos show design concepts.",
},
"ru": {
 "title": "Робот для сбора голубики CALIBER+ — цена и пилот | TPF Labs",
 "desc": "Автономная машина для сбора голубики: цель — 17 кг/ч без потерь, ≈1,9 €/кг. Аренда от 26 000 € за сезон или покупка. Набор хозяйств на пилот 2027.",
 "nav": {"tech":"Технологии","pilot":"Пилот","price":"Цены","contact":"Контакты"},
 "hero_tag": "TPF Labs · Автономная полевая робототехника",
 "h1": "<b>CALIBER+</b> — робот для сбора голубики: собирает как руки, работает как машина",
 "lead": "Автономный робот для селективного сбора свежей голубики на продажу. Два ряда одновременно, ягоду за ягодой; проектная цель — нулевые потери и автономностью 12–14 часов в день.",
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
  ["Покупка","от 80 000 €",["Прототип и пилотная серия: 2027–2028","Сертификация CE по Регламенту ЕС 2023/1230","Гибридное производство: сборка в ЕС, оптимизированная механика","Коммерческое предложение по запросу"]],
 ],
 "contact_h": "Пригласите CALIBER+ на своё поле",
 "contact_s": "Слоты пилота на сезон 2027 открыты. Расскажите о хозяйстве: гектары, сорта, сроки уборки.",
 "mail": MAIL,
 "site": "tpf-technology.com — материнская компания",
 "foot_l": "TPF Labs — дивизион автономной робототехники TPFtechnology.",
 "foot_r": "CALIBER+ находится в стадии подготовки к производству. Изображения — дизайнерские концепты.",
},
"nl": {
 "title": "CALIBER+ oogstrobot blauwe bessen — prijs & pilot | TPF Labs",
 "desc": "Blauwe bessen machinaal oogsten voor de versmarkt: ontworpen voor 17 kg/u zonder verlies, ≈€1,9/kg. Huur vanaf €26.000 per seizoen of koop. Pilots 2027 open.",
 "nav": {"tech":"Technologie","pilot":"Pilot","price":"Prijzen","contact":"Contact"},
 "hero_tag": "TPF Labs · Autonome veldrobotica",
 "h1": "<b>CALIBER+</b> oogstrobot voor blauwe bessen — plukt als handwerk, werkt als een machine",
 "lead": "Een autonome robot voor selectieve oogst van verse blauwe bessen. Twee rijen tegelijk, bes voor bes, ontworpen voor nul verlies en 12–14 uur autonomie per dag.",
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
  ["Aankoop","vanaf €80.000",["Prototype- en pilotserie-tijdlijn 2027–2028","CE-certificering volgens EU Machinery Regulation 2023/1230","Hybride productie: EU-assemblage, geoptimaliseerde mechanica","Commercieel voorstel op aanvraag"]],
 ],
 "contact_h": "Breng CALIBER+ naar uw veld",
 "contact_s": "Pilot-slots voor seizoen 2027 zijn open. Vertel over uw bedrijf: hectaren, rassen, oogstperiode.",
 "mail": MAIL,
 "site": "tpf-technology.com — moederbedrijf",
 "foot_l": "TPF Labs — divisie autonome robotica van TPFtechnology.",
 "foot_r": "CALIBER+ is in preproductie. Foto's tonen ontwerpconcepten.",
},
"pl": {
 "title": "Robot do zbioru borówki CALIBER+ — cena i pilotaż | TPF Labs",
 "desc": "Autonomiczny kombajn do zbioru borówki na rynek świeży: projektowo 17 kg/h bez strat, ≈1,9 €/kg. Dzierżawa od 26 000 € za sezon lub zakup. Pilotaże 2027.",
 "nav": {"tech":"Technologia","pilot":"Pilotaż","price":"Ceny","contact":"Kontakt"},
 "hero_tag": "TPF Labs · Autonomiczna robotyka polowa",
 "h1": "<b>CALIBER+</b> — robot do zbioru borówki: zbiera jak ludzkie ręce, pracuje jak maszyna",
 "lead": "Autonomiczny robot do selektywnego zbioru borówki amerykańskiej na rynek świeży. Dwa rzędy jednocześnie, owoc po owocu, projektowany pod zerowe straty i autonomię 12–14 godzin dziennie.",
 "cta1": "Zgłoś się do pilotażu", "cta2": "Technologia",
 "stats": [("17 kg/h","wydajność jednej maszyny"),(">97%","trafność oceny dojrzałości"),("0%","strat (kombajny ok. 5%)"),("12–14 h","autonomii dziennie")],
 "tech_h": "Stworzony dla owoców na rynek świeży",
 "tech_s": "Cztery ramiona SCARA, wizja AI oceniająca dojrzałość i miękki chwytak hybrydowy traktują każdy owoc jak zbierany ręcznie.",
 "cards": [
  ["🦾","Cztery ramiona SCARA","Po dwa manipulatory z każdej strony na pionowych wózkach zbierają owoce z dwóch rzędów jednocześnie.","zasięg 800 mm · skok wózka 1500 mm · cykl 0,5 s"],
  ["🧠","Wizja AI oceniająca dojrzałość","Rozpoznawanie oparte na głębokim uczeniu znajduje każdy dojrzały owoc i pomija zielone — jakość na rynek świeży przy każdym przejeździe.",">97% trafności · kamery głębi + LiDAR + RTK-GPS"],
  ["🫐","Delikatny chwytak hybrydowy","Silikonowe palce ze wspomaganiem podciśnieniowym trzymają owoc z siłą poniżej 2 N. Bez odgnieceń i osypywania.","miękki chwyt ≤2 N · chłodzony zbiornik 60 l na pokładzie"],
  ["☀️","Praca przez cały dzień","Akumulatory LiFePO4 i dach solarny 600 W zapewniają pracę przez całą zmianę. Szybka wymiana baterii.","48 V LiFePO4 · podwozie gąsienicowe na miękki grunt · 450 kg"],
 ],
 "pilot_h": "Program pilotażowy: 30 / 60 / 90 dni",
 "pilot_s": "Żadnych zobowiązań finansowych do czasu umowy sezonowej. Udowodnimy liczby na Państwa plantacji, a decyzja należy do Państwa.",
 "steps": [
  ["Dni 0–30","Przegląd i mapowanie rzędów","Skanujemy rzędy, tworzymy mapę RTK kwatery i kalibrujemy system wizyjny pod Państwa odmiany."],
  ["Dni 30–60","Autonomiczny zbiór na 1 ha","CALIBER+ pracuje na kwaterze; mierzymy dojrzałość, kaliber, straty i koszt za kilogram."],
  ["Dni 60–90","Raport i umowa sezonowa","Otrzymują Państwo pełny raport z pilotażu oraz opcję zablokowania stawki RaaS lub zakupu na sezon 2027."],
 ],
 "price_h": "Prosty model współpracy",
 "price_s": "Start bez nakładów inwestycyjnych — dzierżawa na sezon lub zakup.",
 "plans": [
  ["Robot jako usługa (RaaS)","26 000 € / sezon","hot",["Serwis, oprogramowanie i aktualizacje w cenie","≈1,9 €/kg wobec ≈2,4 €/kg przy zbiorze ręcznym","Szybka wymiana baterii w stacji bazowej","Wolne terminy na sezon 2027"]],
  ["Zakup","od 80 000 €",["Prototyp i seria pilotażowa: 2027–2028","Certyfikacja CE zgodnie z rozporządzeniem UE 2023/1230 w sprawie maszyn","Produkcja hybrydowa: montaż w UE, zoptymalizowana mechanika","Oferta handlowa na zapytanie"]],
 ],
 "contact_h": "Zaproś CALIBER+ na swoją plantację",
 "contact_s": "Terminy pilotaży na sezon 2027 są otwarte. Prosimy opisać gospodarstwo: hektary, odmiany, termin zbioru.",
 "mail": MAIL,
 "site": "tpf-technology.com — firma macierzysta",
 "foot_l": "TPF Labs — dział autonomicznej robotyki TPFtechnology.",
 "foot_r": "CALIBER+ jest na etapie przygotowania do produkcji. Zdjęcia przedstawiają koncepcje projektowe.",
},
"zh": {
 "title": "CALIBER+ 蓝莓采摘机器人 — 价格与试点 | TPF Labs",
 "desc": "面向鲜果市场的自主蓝莓采摘机：设计目标每小时 17 公斤、零损耗，约 1.9 欧元/公斤。按季租赁 26,000 欧元起或购买。2027 试点名额开放。",
 "nav": {"tech":"技术","pilot":"试点","price":"价格","contact":"联系"},
 "hero_tag": "TPF Labs · 自主田间机器人",
 "h1": "<b>CALIBER+</b> 蓝莓采摘机器人：像双手一样轻采，像机器一样高效",
 "lead": "面向鲜果蓝莓市场的自主采摘机器人。同时采摘两行，逐颗识别，设计目标为零损耗、每日续航 12–14 小时。",
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
  ["购买","80,000 € 起",["原型与试产线时间表 2027–2028","按欧盟机械法规 2023/1230 进行 CE 认证","混合制造：欧盟组装，优化的机械部件","商业方案可索取"]],
 ],
 "contact_h": "把 CALIBER+ 带到你的田间",
 "contact_s": "2027 季度试点名额已开放。请介绍你的农场：面积、品种、采收期。",
 "mail": MAIL,
 "site": "tpf-technology.com — 母公司",
 "foot_l": "TPF Labs — TPFtechnology 旗下自主机器人部门。",
 "foot_r": "CALIBER+ 处于量产准备阶段。图片为设计概念图。",
},
}


INV = {
"en": {
 "nav": "Investors",
 "cta2": "Download deck (PDF)",
 "h": "Invest in the future of fresh-market harvesting",
 "s": "CALIBER+ is raising a Seed round (€1.0–1.2M) to take the validated gripper and vision stack into the field prototype and the 2028 commercial launch. Industrial and go-to-market partners are welcome.",
 "cta": "Request the investor deck",
 "cards": [
  ["🧩","Traction today","Signed NDA and a DFM package under review with contract manufacturer WayKen (CN); third-party validation talks with AgriFoodTEF nodes ILVO and INRIA (EU); first farm interest from Poland's largest blueberry GPO.","Seed round · EU company · 2026–2027"],
  ["📈","Market window","Manual picking costs ≈€2.4/kg with a chronic labor shortage. At ≈€1.9/kg under RaaS, CALIBER+ is modelled to pay back within one season per robot.","fresh-market blueberries · EU first"],
  ["🤝","Partner with us","Pilot farms for season 2027, RaaS channel and service partners, component suppliers for the EU assembly chain.","farms · integrators · suppliers"],
  ["🚀","Roadmap","Gripper prototype: built and lab-tested. Field prototype: 2027. Commercial launch: 2028.","prototype → pilot fleet → launch"],
 ],
},
"ru": {
 "nav": "Инвесторам",
 "cta2": "Скачать деку (PDF)",
 "h": "Инвестиции в будущее уборки свежего рынка",
 "s": "CALIBER+ открывает Seed-раунд (1,0–1,2 млн €), чтобы вывести проверенные захват и ИИ-зрение в полевой прототип и к коммерческому запуску 2028 года. Мы также открыты к промышленным и партнёрским альянсам.",
 "cta": "Запросить инвесторскую презентацию",
 "cards": [
  ["🧩","Трекшн","Подписан NDA, техпакет на DFM-ревью у контрактного производителя WayKen (КНР); сторонняя валидация с нодами AgriFoodTEF ILVO и INRIA (ЕС); первый интерес от крупнейшего польского GPO по голубике.","Seed-раунд · компания в ЕС · 2026–2027"],
  ["📈","Окно рынка","Ручной сбор ≈2,4 €/кг при хронической нехватке рабочих. При RaaS ≈1,9 €/кг робот, по расчётам, окупается за один сезон.","свежая голубика · сначала ЕС"],
  ["🤝","Стать партнёром","Хозяйства-пилоты на сезон 2027, канальные и сервисные партнёры RaaS, поставщики компонентов для сборки в ЕС.","хозяйства · интеграторы · поставщики"],
  ["🚀","Дорожная карта","Прототип захвата: собран и протестирован. Полевой прототип: 2027. Коммерческий запуск: 2028.","прототип → пилотный флот → запуск"],
 ],
},
"nl": {
 "nav": "Investeerders",
 "cta2": "Deck downloaden (PDF)",
 "h": "Investeren in de toekomst van verse oogst",
 "s": "CALIBER+ opent een Seed-ronde (€1,0–1,2 mln) om de gevalideerde grijper en vision-stack naar het veldprototype en de commerciële lancering in 2028 te brengen. Industriële en go-to-market partners zijn welkom.",
 "cta": "Investeerdersdeck opvragen",
 "cards": [
  ["🧩","Tractie","Ondertekende NDA en DFM-pakket in review bij contractproducent WayKen (CN); validatiegesprekken met AgriFoodTEF-nodes ILVO en INRIA (EU); eerste belang van Polens grootste blauwe-bessen-GPO.","Seed-ronde · EU-bedrijf · 2026–2027"],
  ["📈","Marktkans","Handmatig plukken kost ≈€2,4/kg bij chronisch arbeidstekort. Bij ≈€1,9/kg RaaS verdient CALIBER+ zich volgens het model per robot in één seizoen terug.","verse blauwe bessen · eerst EU"],
  ["🤝","Partner worden","Pilotbedrijven voor seizoen 2027, RaaS-kanaal- en servicepartners, componentleveranciers voor EU-assemblage.","telers · integrators · leveranciers"],
  ["🚀","Roadmap","Grijper-prototype: gebouwd en getest. Veldprototype: 2027. Commerciële lancering: 2028.","prototype → pilotvloot → lancering"],
 ],
},
"pl": {
 "nav": "Inwestorzy",
 "cta2": "Pobierz prezentację (PDF)",
 "h": "Inwestycja w przyszłość zbioru owoców na rynek świeży",
 "s": "CALIBER+ otwiera rundę Seed (1,0–1,2 mln €), aby przenieść sprawdzony chwytak i system wizyjny do prototypu polowego i komercyjnego startu w 2028 roku. Zapraszamy partnerów przemysłowych i handlowych.",
 "cta": "Poproś o prezentację dla inwestorów",
 "cards": [
  ["🧩","Postępy","Podpisana umowa NDA i pakiet DFM w ocenie u producenta kontraktowego WayKen (Chiny); rozmowy o niezależnej walidacji z węzłami AgriFoodTEF ILVO i INRIA (UE); pierwsze zainteresowanie ze strony największej polskiej grupy zakupowej borówki.","runda Seed · firma w UE · 2026–2027"],
  ["📈","Okno rynkowe","Zbiór ręczny kosztuje ≈2,4 €/kg przy chronicznym niedoborze rąk do pracy. Przy ≈1,9 €/kg w modelu RaaS jeden robot CALIBER+ według wyliczeń zwraca się w ciągu sezonu.","borówka na rynek świeży · najpierw UE"],
  ["🤝","Zostań partnerem","Gospodarstwa pilotażowe na sezon 2027, partnerzy handlowi i serwisowi RaaS, dostawcy komponentów do montażu w UE.","plantacje · integratorzy · dostawcy"],
  ["🚀","Mapa drogowa","Prototyp chwytaka: zbudowany i przetestowany w laboratorium. Prototyp polowy: 2027. Start komercyjny: 2028.","prototyp → flota pilotażowa → start"],
 ],
},
"zh": {
 "nav": "投资人",
 "cta2": "下载资料 (PDF)",
 "h": "投资新鲜市场采摘的未来",
 "s": "CALIBER+ 正开启种子轮（100–120万欧元），将已验证的夹爪与视觉系统推进到田间原型和2028年商业化发布。同时欢迎产业与市场合作伙伴。",
 "cta": "获取投资人资料",
 "cards": [
  ["🧩","现有进展","已与合同制造商WayKen签署保密协议，DFM技术包在审；与欧盟AgriFoodTEF节点ILVO和INRIA进行第三方验证洽谈；波兰最大蓝莓GPO已表达合作意向。","种子轮 · 欧盟公司 · 2026–2027"],
  ["📈","市场窗口","人工采摘成本约2.4欧元/公斤，劳动力长期短缺。RaaS模式约1.9欧元/公斤，按测算单台机器人一个产季即可回本。","新鲜蓝莓 · 优先欧洲市场"],
  ["🤝","合作方式","2027产季试点农场、RaaS渠道与服务伙伴、欧盟组装的零部件供应商。","农场 · 集成商 · 供应商"],
  ["🚀","路线图","夹爪原型：已完成并测试。田间原型：2027年。商业化发布：2028年。","原型 → 试点车队 → 发布"],
 ],
},
}


FAQ = {
"en": [
 ("How much does CALIBER+ cost?","Robot-as-a-Service starts at €26,000 per season (≈€1.9/kg of picked berries). Purchase starts at €80,000."),
 ("How fast does the robot pick?","The design target is 17 kg/h per unit with 12–14 hours of daily autonomy. It harvests two rows simultaneously, berry by berry."),
 ("Does the machine damage the berries?","No: the silicone-and-vacuum gripper holds each berry with under 2 N of force. CALIBER+ is designed for 0% crop loss versus about 5% for over-the-row harvesters."),
 ("When can a farm get a robot?","Pilot programs run in season 2027 (30/60/90 days), commercial launch is 2028. Pilot slots for 2027 are open now."),
],
"ru": [
 ("Сколько стоит CALIBER+?","Робот-как-Сервис — от 26 000 € за сезон (≈1,9 €/кг собранной ягоды). Покупка — от 80 000 €."),
 ("Как быстро робот собирает ягоду?","Проектная цель — 17 кг/ч с автономностью 12–14 часов в день. Работает с двумя рядами одновременно, ягоду за ягодой."),
 ("Повреждает ли машина ягоду?","Нет: силиконово-вакуумный захват держит ягоду с усилием менее 2 Н. Проектная цель CALIBER+ — 0% потерь против примерно 5% у комбайнов."),
 ("Когда хозяйство может получить робота?","Пилотные программы — сезон 2027 (30/60/90 дней), коммерческий запуск — 2028 год. Слоты пилота на 2027 уже открыты."),
],
"nl": [
 ("Wat kost CALIBER+?","Robot-as-a-Service vanaf €26.000 per seizoen (≈€1,9/kg geplukte bessen). Aankoop vanaf €80.000."),
 ("Hoe snel plukt de robot?","Het ontwerpdoel is 17 kg/u met 12–14 uur autonomie per dag. Hij oogst twee rijen tegelijk, bes voor bes."),
 ("Beschadigt de machine de bessen?","Nee: de siliconen-vacuümgrijper houdt elke bes vast met minder dan 2 N kracht. CALIBER+ is ontworpen voor 0% oogstverlies tegenover circa 5% bij oogstmachines."),
 ("Wanneer kan een teler een robot krijgen?","Pilotprogramma's lopen in seizoen 2027 (30/60/90 dagen), commerciële lancering in 2028. Pilotplekken voor 2027 zijn nu open."),
],
"pl": [
 ("Ile kosztuje CALIBER+?","Robot jako usługa (RaaS) od 26 000 € za sezon (≈1,9 €/kg zebranych owoców). Zakup od 80 000 €."),
 ("Jak szybko robot zbiera borówki?","Cel projektowy to 17 kg/h na maszynę przy 12–14 godzinach autonomii dziennie. Zbiera z dwóch rzędów jednocześnie, owoc po owocu."),
 ("Czy maszyna uszkadza owoce?","Nie: silikonowo-podciśnieniowy chwytak trzyma każdy owoc z siłą poniżej 2 N. CALIBER+ jest projektowany pod 0% strat wobec ok. 5% przy kombajnach okrakowych."),
 ("Kiedy gospodarstwo może otrzymać robota?","Programy pilotażowe ruszają w sezonie 2027 (30/60/90 dni), start komercyjny w 2028 roku. Terminy pilotaży na 2027 są już otwarte."),
],
"zh": [
 ("CALIBER+ 的价格是多少？","机器人即服务（RaaS）：每产季 26,000 欧元起（约 1.9 欧元/公斤）。购买：80,000 欧元起。"),
 ("机器人采摘速度有多快？","设计目标为单台每小时 17 公斤，每天自主作业 12–14 小时，可同时采摘两行，逐颗采摘。"),
 ("机器会损伤果实吗？","不会：硅胶加真空的夹爪以小于 2 牛的力夹持每颗果实。CALIBER+ 的设计目标是作物损失为 0%，而跨行采收机约为 5%。"),
 ("农场什么时候可以拿到机器人？","试点计划在 2027 产季（30/60/90 天），商业化发布于 2028 年。2027 年的试点名额现已开放。"),
],
}

TPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#070b14">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://tpflabs.com{suffix}">
<meta property="og:image" content="https://tpflabs.com/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta property="og:site_name" content="TPF Labs">
<meta property="og:locale" content="{og_locale}">
{og_locale_alt}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://tpflabs.com/img/og.png">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="https://tpflabs.com{suffix}">
{hreflang}
<meta name="google-site-verification" content="Zr5OkmQBIum5PVhi6DNK-WUCK-wY8WJlHhbv-nSxepE">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/img/favicon-64.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" as="image" href="/img/hero.webp" type="image/webp" fetchpriority="high">
<link rel="stylesheet" href="/css/style.css">
{jsonld}
</head>
<body>
<header>
  <div class="wrap nav">
    <a class="logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo"> TPF<b>labs</b></a>
    <div class="links">
      <a href="#tech">{nav_tech}</a><a href="#pilot">{nav_pilot}</a><a href="#price">{nav_price}</a><a href="#invest">{nav_inv}</a><a href="#faq">FAQ</a><a href="{blog_url}">{nav_blog}</a><a href="#contact">{nav_contact}</a>
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
  <div class="hero-visual"><span class="c3"></span><picture><source srcset="/img/hero.webp" type="image/webp"><img src="/img/hero.jpg" alt="{hero_alt}" fetchpriority="high" decoding="async" width="700" height="875"></picture>
    <div class="hero-cap"><b>CALIBER+</b> · {hero_cap}</div>
  </div></div>
</div>
<div class="wrap"><div class="stats">
  {stats_html}
</div><p class="stats-note">{stats_note}</p></div>
<section id="film" class="film">
  <div class="wrap">
    <span class="over">{film_over}</span><br><h2>{film_h}</h2>
    <p class="sub">{film_s}</p>
    <div class="film-frame">
      <video class="film-video" title="{film_h}" controls playsinline preload="metadata" poster="/img/film-poster.jpg" width="1920" height="1080">
        <source src="/video/caliber-plus-film-en-16x9.mp4" type="video/mp4">
        Your browser does not support the video tag. <a href="/video/caliber-plus-film-en-16x9.mp4">Download the film</a>.
      </video>
    </div>
  </div>
</section>
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
<section id="invest" class="alt">
  <div class="wrap">
    <span class="over">{over_inv}</span><br><h2>{inv_h}</h2><p class="sub">{inv_s}</p>
    <div class="grid g4">{inv_cards}</div>
    <div class="cta-row" style="justify-content:center;margin-top:28px">
      <a class="btn pri" href="mailto:{mail}?subject=CALIBER%2B%20investors">{inv_cta}</a>
      <a class="btn sec" href="/caliber-investor-deck.pdf" target="_blank" rel="noopener">{inv_cta2}</a>
    </div>
  </div>
</section>
<section id="faq">
  <div class="wrap">
    <span class="over">FAQ</span><br><h2>{faq_h}</h2>
    <div class="faq">{faq_html}</div>
  </div>
</section>
<section id="about" class="about">
  <div class="wrap">
    <span class="over">{about_over}</span><br><h2>{about_h}</h2>
    {about_html}
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
  <a class="logo foot-logo" href="/"><img src="/img/logo-icon.png" alt="TPF Labs logo" loading="lazy" decoding="async"> TPF<b>labs</b></a>
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

FILM = {
 "en": {"over":"CALIBER+ film","h":"See how CALIBER+ works","s":"70 seconds on the machine: four SCARA arms, AI ripeness vision, a chilled 60 L hopper and 12-14 hours of autonomous work."},
 "ru": {"over":"\u0424\u0438\u043b\u044c\u043c \u043e CALIBER+","h":"\u041a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 CALIBER+","s":"70 \u0441\u0435\u043a\u0443\u043d\u0434 \u043e \u043c\u0430\u0448\u0438\u043d\u0435: \u0447\u0435\u0442\u044b\u0440\u0435 SCARA-\u043c\u0430\u043d\u0438\u043f\u0443\u043b\u044f\u0442\u043e\u0440\u0430, \u0418\u0418-\u0437\u0440\u0435\u043d\u0438\u0435 \u0441\u043f\u0435\u043b\u043e\u0441\u0442\u0438, \u043e\u0445\u043b\u0430\u0436\u0434\u0430\u0435\u043c\u044b\u0439 \u0431\u0443\u043d\u043a\u0435\u0440 60 \u043b \u0438 12-14 \u0447\u0430\u0441\u043e\u0432 \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b."},
 "nl": {"over":"CALIBER+ film","h":"Zo werkt CALIBER+","s":"70 seconden over de machine: vier SCARA-armen, AI-rijpheidsvisie, een gekoelde bunker van 60 liter en 12-14 uur autonoom werk."},
 "pl": {"over":"Film o CALIBER+","h":"Zobacz, jak działa CALIBER+","s":"70 sekund o maszynie: cztery ramiona SCARA, wizja AI oceniająca dojrzałość, chłodzony zbiornik 60 l i 12–14 godzin autonomicznej pracy."},
 "zh": {"over":"CALIBER+ \u5f71\u7247","h":"\u4e86\u89e3 CALIBER+ \u5982\u4f55\u5de5\u4f5c","s":"70 \u79d2\u770b\u61c2\u8fd9\u53f0\u673a\u5668\uff1a\u56db\u6761 SCARA \u673a\u68b0\u81c2\u3001AI \u6210\u719f\u5ea6\u8bc6\u522b\u300160 \u5347\u51b7\u85cf\u679c\u7bb1\uff0c12-14 \u5c0f\u65f6\u81ea\u4e3b\u4f5c\u4e1a\u3002"},
}

OG_LOC = {"en":"en_US","ru":"ru_RU","nl":"nl_NL","pl":"pl_PL","zh":"zh_CN"}

# Localized SEO strings: image alt texts, captions, nav label, video metadata
SEO = {
 "en": {"og_alt":"CALIBER+ autonomous blueberry harvesting robot by TPF Labs",
        "hero_alt":"CALIBER+ autonomous blueberry harvesting robot picking two rows — concept render",
        "hero_cap":"concept render · 1:2 row architecture", "blog":"Blog",
        "video_name":"CALIBER+ autonomous blueberry harvester — how it works"},
 "ru": {"og_alt":"CALIBER+ — автономный робот для сбора голубики от TPF Labs",
        "hero_alt":"Автономный робот для сбора голубики CALIBER+ убирает два ряда — концепт-рендер",
        "hero_cap":"концепт-рендер · архитектура 1:2 ряда", "blog":"Блог",
        "video_name":"CALIBER+ — как работает автономный сборщик голубики"},
 "nl": {"og_alt":"CALIBER+ autonome oogstrobot voor blauwe bessen van TPF Labs",
        "hero_alt":"CALIBER+ autonome oogstrobot voor blauwe bessen oogst twee rijen — conceptrender",
        "hero_cap":"conceptrender · 1:2 rij-architectuur", "blog":"Blog",
        "video_name":"CALIBER+ autonome blauwe-bessenoogstrobot — zo werkt het"},
 "pl": {"og_alt":"CALIBER+ — autonomiczny robot do zbioru borówki od TPF Labs",
        "hero_alt":"Autonomiczny robot do zbioru borówki CALIBER+ zbiera z dwóch rzędów — wizualizacja koncepcyjna",
        "hero_cap":"wizualizacja koncepcyjna · architektura 1:2 rzędy", "blog":"Blog",
        "video_name":"CALIBER+ — jak działa autonomiczny kombajn do borówki"},
 "zh": {"og_alt":"TPF Labs 的 CALIBER+ 自主蓝莓采摘机器人",
        "hero_alt":"CALIBER+ 自主蓝莓采摘机器人同时采摘两行——概念渲染图",
        "hero_cap":"概念渲染图 · 1:2 行架构", "blog":"博客",
        "video_name":"CALIBER+ 自主蓝莓采摘机如何工作"},
}
# "About" block: who builds the machine and at what stage (trust signals for buyers)
ABOUT = {'en': ('About', 'Who builds CALIBER+', ['<b>TPF Labs</b> is the autonomous field robotics division of TPFtechnology, a software and AI company registered in Poland and working across the EU.', 'Where we are today: the soft gripper prototype is built and lab-tested; the field prototype goes into pilot farms in season 2027, and commercial launch is planned for 2028. Manufacturing is prepared with contract manufacturer WayKen, and independent validation is being discussed with the AgriFoodTEF network (ILVO, INRIA).', 'Images on this site are design renders, and performance figures are design targets until pilot results are published. Questions go to one address, answered by the team that builds the machine.']), 'ru': ('О компании', 'Кто делает CALIBER+', ['<b>TPF Labs</b> — подразделение автономной полевой робототехники TPFtechnology, компании в сфере ПО и ИИ, зарегистрированной в Польше и работающей по всему ЕС.', 'Где мы сейчас: прототип мягкого захвата собран и испытан в лаборатории; полевой прототип выходит в пилотные хозяйства в сезон 2027, коммерческий запуск запланирован на 2028 год. Производство готовится с контрактным производителем WayKen, независимая проверка обсуждается с сетью AgriFoodTEF (ILVO, INRIA).', 'Изображения на сайте — дизайнерские рендеры, а показатели — проектные цели до публикации результатов пилотов. На вопросы отвечает команда, которая строит машину, по одному адресу.']), 'nl': ('Over ons', 'Wie bouwt CALIBER+', ['<b>TPF Labs</b> is de divisie autonome veldrobotica van TPFtechnology, een software- en AI-bedrijf geregistreerd in Polen en actief in de hele EU.', 'Waar we nu staan: het prototype van de zachte grijper is gebouwd en in het lab getest; het veldprototype gaat in seizoen 2027 naar pilotbedrijven en de commerciële lancering is gepland voor 2028. De productie wordt voorbereid met contractproducent WayKen; onafhankelijke validatie wordt besproken met het AgriFoodTEF-netwerk (ILVO, INRIA).', 'Afbeeldingen op deze site zijn ontwerprenders en prestatiecijfers zijn ontwerpdoelen tot de pilotresultaten zijn gepubliceerd. Vragen gaan naar één adres en worden beantwoord door het team dat de machine bouwt.']), 'pl': ('O nas', 'Kto buduje CALIBER+', ['<b>TPF Labs</b> to dział autonomicznej robotyki polowej TPFtechnology — firmy z branży oprogramowania i AI zarejestrowanej w Polsce i działającej w całej UE.', 'Na jakim etapie jesteśmy: prototyp miękkiego chwytaka jest zbudowany i przetestowany w laboratorium; prototyp polowy trafi do gospodarstw pilotażowych w sezonie 2027, a start komercyjny planujemy na 2028 rok. Produkcję przygotowujemy z producentem kontraktowym WayKen, a niezależną walidację omawiamy z siecią AgriFoodTEF (ILVO, INRIA).', 'Zdjęcia na stronie to wizualizacje projektowe, a parametry to cele projektowe do czasu publikacji wyników pilotaży. Na pytania odpowiada zespół, który buduje maszynę, pod jednym adresem.']), 'zh': ('关于我们', '谁在打造 CALIBER+', ['<b>TPF Labs</b> 是 TPFtechnology 旗下的自主田间机器人部门。TPFtechnology 是一家在波兰注册、业务覆盖欧盟的软件与人工智能公司。', '目前进展：柔性夹爪原型已完成并通过实验室测试；田间原型将于 2027 产季进入试点农场，计划于 2028 年商业化发布。我们正与合同制造商 WayKen 准备生产，并与 AgriFoodTEF 网络（ILVO、INRIA）商谈第三方验证。', '本站图片为设计渲染图；在试点结果公布前，性能数据均为设计目标。所有问题由打造这台机器的团队通过同一个邮箱回复。'])}

VIDEO_UPLOAD = "2026-11-02"

# Shown under the stat tiles: the numbers are targets for a machine still in pre-production
STATS_NOTE = {'en': 'Design targets for the 2027 field prototype; pilot results will be published.', 'ru': 'Проектные показатели полевого прототипа 2027 года; результаты пилотов будут опубликованы.', 'nl': 'Ontwerpdoelen voor het veldprototype van 2027; pilotresultaten worden gepubliceerd.', 'pl': 'Parametry projektowe prototypu polowego 2027; wyniki pilotaży zostaną opublikowane.', 'zh': '以上为 2027 年田间原型的设计目标，试点结果将公开发布。'}


HREFLANG = "\n".join(f'<link rel="alternate" hreflang="{l}" href="https://tpflabs.com{"/" if l=="en" else "/"+l+"/"}">' for l in CODES) + '\n<link rel="alternate" hreflang="x-default" href="https://tpflabs.com/">'


def page(c, lang):
    suffix = "/" if lang=="en" else "/"+lang+"/"
    langlinks = ""
    for l,label in LANGS:
        href = "/" if l=="en" else "/"+l+"/"
        cls = ' class="on"' if l==lang else ""
        langlinks += f'<a href="{href}"{cls}>{label}</a>'
    stats_html = "".join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in c["stats"])
    cards_html = "".join(f'<div class="card"><div class="ic">{ic}</div><h3>{h}</h3><p>{p}</p><div class="spec">{s}</div></div>' for ic,h,p,s in c["cards"])
    steps_html = "".join(f'<div class="step"><div class="num">{d}</div><h3>{t}</h3><p>{p}</p></div>' for d,t,p in c["steps"])
    faq_items = FAQ[lang]
    faq_html = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq_items)
    import json as _json
    _url = "https://tpflabs.com" + suffix
    _org = {"@type":"Organization","@id":"https://tpflabs.com/#org","name":"TPF Labs","alternateName":["TPFlabs","TPF Labs CALIBER+"],"url":"https://tpflabs.com/","logo":{"@type":"ImageObject","url":"https://tpflabs.com/apple-touch-icon.png","width":180,"height":180},"image":"https://tpflabs.com/img/og.png","email":MAIL,"description":"Autonomous field robotics for fresh-market berry harvesting.","parentOrganization":{"@type":"Organization","name":"TPFtechnology","url":"https://tpf-technology.com/"},"address":{"@type":"PostalAddress","addressCountry":"PL"},"areaServed":{"@type":"Place","name":"European Union"},"knowsAbout":["blueberry harvesting","agricultural robotics","selective fruit picking","robot as a service"],"knowsLanguage":CODES,"sameAs":["https://www.youtube.com/@TPFTECHNOLOGY"]}
    _prod = {"@type":"Product","@id":"https://tpflabs.com/#caliber","name":"CALIBER+","description":"Autonomous selective harvester for fresh-market blueberries in pre-production. Design targets: 17 kg/h, >97% ripeness accuracy, 0% crop loss, 12-14 h autonomy.","image":["https://tpflabs.com/img/hero.jpg","https://tpflabs.com/img/og.png","https://tpflabs.com/img/film-poster.jpg"],"brand":{"@type":"Brand","name":"TPF Labs"},"manufacturer":{"@id":"https://tpflabs.com/#org"},"category":"Agricultural robot","subjectOf":{"@id":_url+"#film"},"offers":{"@type":"AggregateOffer","priceCurrency":"EUR","lowPrice":"80000","offerCount":1,"availability":"https://schema.org/PreOrder","url":_url+"#price","seller":{"@id":"https://tpflabs.com/#org"}},"additionalProperty":[{"@type":"PropertyValue","name":"Picking rate","value":"17 kg/h"},{"@type":"PropertyValue","name":"Ripeness accuracy","value":">97%"},{"@type":"PropertyValue","name":"Crop loss","value":"0%"},{"@type":"PropertyValue","name":"Daily autonomy","value":"12-14 h"},{"@type":"PropertyValue","name":"Weight","value":"450 kg"}]}
    _site = {"@type":"WebSite","@id":"https://tpflabs.com/#site","url":"https://tpflabs.com/","name":"TPF Labs","alternateName":"TPF Labs — CALIBER+","publisher":{"@id":"https://tpflabs.com/#org"},"inLanguage":CODES}
    _page = {"@type":"WebPage","@id":_url+"#page","url":_url,"name":c["title"],"description":c["desc"],"inLanguage":lang,"isPartOf":{"@id":"https://tpflabs.com/#site"},"about":{"@id":"https://tpflabs.com/#caliber"},"primaryImageOfPage":{"@type":"ImageObject","url":"https://tpflabs.com/img/hero.jpg","width":700,"height":875}}
    _video = {"@type":"VideoObject","@id":_url+"#film","name":SEO[lang]["video_name"],"description":FILM[lang]["s"],"thumbnailUrl":["https://tpflabs.com/img/film-poster.jpg"],"uploadDate":VIDEO_UPLOAD+"T12:00:00+00:00","duration":"PT1M11S","contentUrl":"https://tpflabs.com/video/caliber-plus-film-en-16x9.mp4","inLanguage":"en","sameAs":"https://www.youtube.com/watch?v=c4PZyR0PSz0","publisher":{"@id":"https://tpflabs.com/#org"}}
    _faq = {"@type":"FAQPage","@id":_url+"#faq","inLanguage":lang,"mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_items]}
    _ld = {"@context":"https://schema.org","@graph":[_org,_site,_page,_prod,_video,_faq]}
    jsonld = '<script type="application/ld+json">' + _json.dumps(_ld, ensure_ascii=False) + '</script>'
    inv = INV[lang]
    inv_cards = "".join(f'<div class="card"><div class="ic">{ic}</div><h3>{h}</h3><p>{p}</p><div class="spec">{s}</div></div>' for ic,h,p,s in inv["cards"])
    plans_html = ""
    for plan in c["plans"]:
        name, pr, feats = plan[0], plan[1], plan[3] if len(plan)>3 and plan[2]=="hot" else plan[2]
        hot = ' hot' if (len(plan)>3 and plan[2]=="hot") else ''
        ul = "".join(f"<li>{f}</li>" for f in feats)
        plans_html += f'<div class="plan{hot}"><div class="ph">{name}</div><div class="pnum">{pr}</div><ul>{ul}</ul><a class="btn sec" href="mailto:{c["mail"]}?subject=CALIBER%2B">{ {"en":"Request","ru":"Запрос","nl":"Aanvraag","pl":"Zapytaj","zh":"咨询"}[lang] }</a></div>'
    html = TPL.format(
        lang=lang, brand="TPF", suffix=suffix, title=c["title"], desc=c["desc"],
        over_tech=c["nav"]["tech"], over_pilot=c["nav"]["pilot"], over_price=c["nav"]["price"], over_contact=c["nav"]["contact"],
        og_locale=OG_LOC[lang],
        nav_tech=c["nav"]["tech"], nav_pilot=c["nav"]["pilot"], nav_price=c["nav"]["price"], nav_contact=c["nav"]["contact"],
        langlinks=langlinks, hero_tag=c["hero_tag"], h1=c["h1"], lead=c["lead"],
        mail=c["mail"], cta1=c["cta1"], cta2=c["cta2"], stats_html=stats_html, stats_note=STATS_NOTE[lang], about_over=ABOUT[lang][0], about_h=ABOUT[lang][1], about_html="".join(f'<p class="sub">{t}</p>' for t in ABOUT[lang][2]),
        tech_h=c["tech_h"], tech_s=c["tech_s"], cards_html=cards_html,
        pilot_h=c["pilot_h"], pilot_s=c["pilot_s"], steps_html=steps_html,
        price_h=c["price_h"], price_s=c["price_s"], plans_html=plans_html,
        contact_h=c["contact_h"], contact_s=c["contact_s"], site=c["site"],
        nav_inv=inv["nav"], over_inv=inv["nav"], inv_h=inv["h"], inv_s=inv["s"], inv_cta=inv["cta"], inv_cta2=inv["cta2"], inv_cards=inv_cards,
        faq_h={"en":"Questions from farms","ru":"Вопросы хозяйств","nl":"Vragen van telers","pl":"Pytania od plantatorów","zh":"农场常见问题"}[lang], faq_html=faq_html, jsonld=jsonld, blog_url=("/blog/" if lang=="en" else f"/blog/{lang}/"),
        film_over=FILM[lang]["over"], film_h=FILM[lang]["h"], film_s=FILM[lang]["s"],
        foot_l=c["foot_l"], foot_r=c["foot_r"],
        og_alt=SEO[lang]["og_alt"], hero_alt=SEO[lang]["hero_alt"], hero_cap=SEO[lang]["hero_cap"],
        nav_blog=SEO[lang]["blog"], hreflang=HREFLANG,
        og_locale_alt="\n".join(f'<meta property="og:locale:alternate" content="{v}">' for k,v in OG_LOC.items() if k!=lang))
    return html

# Pages are written straight into the site root that Vercel serves (no manual copy step)
ROOT = os.path.dirname(os.path.abspath(__file__))
for lang in CODES:
    p = os.path.join(ROOT, "index.html" if lang=="en" else f"{lang}/index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p,"w",encoding="utf-8") as f:
        f.write(page(C[lang], lang))
    print("built", p)

# Main sitemap: language versions with hreflang alternates, hero image and the film
import datetime as _dt
_today = _dt.date.today().isoformat()
_alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="https://tpflabs.com{"/" if l=="en" else "/"+l+"/"}"/>' for l in CODES)
_alts += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="https://tpflabs.com/"/>'
_rows = []
for lang in CODES:
    loc = "https://tpflabs.com" + ("/" if lang=="en" else f"/{lang}/")
    _rows.append(f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{_today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if lang=="en" else "0.9"}</priority>{_alts}
    <image:image><image:loc>https://tpflabs.com/img/hero.jpg</image:loc></image:image>
    <video:video>
      <video:thumbnail_loc>https://tpflabs.com/img/film-poster.jpg</video:thumbnail_loc>
      <video:title>{SEO[lang]["video_name"]}</video:title>
      <video:description>{FILM[lang]["s"]}</video:description>
      <video:content_loc>https://tpflabs.com/video/caliber-plus-film-en-16x9.mp4</video:content_loc>
      <video:duration>71</video:duration>
      <video:publication_date>{VIDEO_UPLOAD}T12:00:00+00:00</video:publication_date>
    </video:video>
  </url>''')
with open(os.path.join(ROOT, "sitemap.xml"),"w",encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" '
            'xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n' + "\n".join(_rows) + "\n</urlset>\n")
print("built sitemap.xml")
