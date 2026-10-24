/* Google Analytics only with the visitor's consent (GDPR). Until "Accept" is pressed nothing is loaded from
   Google and no cookie is set; the choice is kept in this browser (localStorage "tpflabs_consent").
   Measurement ID: G-M27Z9KY530 (TPF Labs, tpflabs.com). */
(function () {
  var ID = 'G-M27Z9KY530', KEY = 'tpflabs_consent';
  var T = {
    ru: { text: 'Мы хотим подключить Google Analytics, чтобы понимать, как посетители пользуются сайтом. Он ставит cookie — только если вы согласны.', ok: 'Принять', no: 'Отклонить' },
    en: { text: 'We would like to use Google Analytics to understand how visitors use the site. It sets cookies — only if you agree.', ok: 'Accept', no: 'Reject' },
    nl: { text: 'Wij willen Google Analytics gebruiken om te begrijpen hoe bezoekers de site gebruiken. Het plaatst cookies — alleen als u akkoord gaat.', ok: 'Accepteren', no: 'Weigeren' },
    zh: { text: '我们希望使用 Google Analytics 来了解访客如何使用本网站。它会设置 Cookie——仅在您同意后。', ok: '接受', no: '拒绝' }
  };
  function lang() { var l = (document.documentElement.lang || 'en').slice(0, 2); return T[l] ? l : 'en'; }
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function load() {
    if (window.__tpfGa) return; window.__tpfGa = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ID);
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
    document.head.appendChild(s);
  }
  function forget() {
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (/^_ga/.test(name)) ['', '; domain=.' + location.hostname.replace(/^www\./, '')].forEach(function (d) {
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d; });
    });
  }
  function close() { var b = document.getElementById('tpf-consent'); if (b) b.remove(); }
  function open() {
    close();
    var t = T[lang()], box = document.createElement('div');
    box.id = 'tpf-consent'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-label', 'Cookie');
    box.style.cssText = 'position:fixed;left:16px;right:16px;bottom:16px;z-index:50;max-width:720px;margin:0 auto;padding:18px 20px;' +
      'background:#0e1626;border:1px solid #1b2740;border-radius:14px;color:#e8eefc;font:15px/1.5 inherit;' +
      'box-shadow:0 10px 40px rgba(0,0,0,.5);display:flex;flex-wrap:wrap;gap:12px 16px;align-items:center';
    var p = document.createElement('p'); p.style.cssText = 'margin:0;flex:1 1 320px;color:#93a3c4';
    p.textContent = t.text;
    function button(label, value) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = label;
      b.style.cssText = 'height:42px;padding:0 20px;border-radius:999px;font-weight:600;font-size:15px;font-family:inherit;cursor:pointer;border:1px solid #4ADEDE;' +
        (value === 'granted' ? 'background:#4ADEDE;color:#03181a' : 'background:transparent;color:#e8eefc');
      b.onclick = function () {
        var before = get(); set(value); close();
        if (value === 'granted') load(); else if (before === 'granted') { forget(); location.reload(); }
      };
      return b;
    }
    var row = document.createElement('div'); row.style.cssText = 'display:flex;gap:10px';
    row.append(button(t.no, 'denied'), button(t.ok, 'granted'));
    box.append(p, row); document.body.appendChild(box);
  }
  window.tpfConsent = { open: open };
  if (navigator.webdriver) return;
  var choice = get();
  if (choice === 'granted') load();
  else if (choice !== 'denied') { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', open); else open(); }
})();
