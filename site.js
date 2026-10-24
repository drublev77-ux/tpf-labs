// TPF Labs site: scroll-reveal (progressive enhancement)
document.addEventListener("DOMContentLoaded", function () {
  document.body.classList.add("js");
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var els = document.querySelectorAll(
    ".stat, .card, .step, .plan, .hero-visual, .hero .txt > *, section .wrap > h2, section .sub, .bigmail"
  );
  var i = 0;
  els.forEach(function (el) {
    el.classList.add("rev");
    el.style.transitionDelay = (i++ % 4) * 70 + "ms";
  });
  if (!("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  els.forEach(function (el) { io.observe(el); });
});
