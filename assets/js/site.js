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
