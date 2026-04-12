(function () {
  var toggle = document.querySelector(".site-nav__toggle");
  var panel = document.querySelector(".site-nav__panel");
  if (!toggle || !panel) return;

  toggle.addEventListener("click", function () {
    var open = document.body.classList.toggle("site-nav-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  panel.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      document.body.classList.remove("site-nav-open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
})();

(function () {
  var targets = document.querySelectorAll(
    ".bento-card, .pub-bento-card, .post-preview"
  );
  if (!targets.length) return;

  if (!("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }

  var staggerDelay = 80;

  var observer = new IntersectionObserver(
    function (entries) {
      var visibleEntries = entries.filter(function (e) { return e.isIntersecting; });
      visibleEntries.forEach(function (entry, i) {
        entry.target.style.animationDelay = (i * staggerDelay) + "ms";
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
  );

  targets.forEach(function (el) { observer.observe(el); });
})();

(function () {
  var btn = document.getElementById("back-to-top");
  if (!btn) return;

  var shown = false;
  window.addEventListener("scroll", function () {
    var shouldShow = window.scrollY > 400;
    if (shouldShow !== shown) {
      shown = shouldShow;
      btn.classList.toggle("is-visible", shown);
    }
  }, { passive: true });

  btn.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
})();
