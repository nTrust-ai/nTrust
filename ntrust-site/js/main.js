/* nTrust.ai — main.js (vanilla, dependency-free) */
(function () {
  "use strict";

  /* Mobile navigation toggle */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
    });
  }

  /* Auto-update footer year */
  var yearEl = document.querySelector("[data-year]");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* Contact form — client-side validation + mailto fallback (no backend dependency) */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var data = new FormData(form);
      var name = (data.get("name") || "").trim();
      var email = (data.get("email") || "").trim();
      var org = (data.get("org") || "").trim();
      var msg = (data.get("message") || "").trim();
      var subject = encodeURIComponent("Website inquiry from " + name + (org ? " (" + org + ")" : ""));
      var body = encodeURIComponent("Name: " + name + "\nEmail: " + email + "\nCompany: " + org + "\n\n" + msg);
      window.location.href = "mailto:hello@ntrust.ai?subject=" + subject + "&body=" + body;
      if (status) status.textContent = "Thanks, " + name + " — your email app should open to send your message.";
    });
  }
})();
