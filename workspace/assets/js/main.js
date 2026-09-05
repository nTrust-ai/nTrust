/* nTrust.ai — site interactions (dependency-free, accessible) */
(function () {
  "use strict";

  // Mobile navigation toggle
  var toggle = document.querySelector(".nav__toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Current year in footer
  var yearEls = document.querySelectorAll("[data-year]");
  var year = String(new Date().getFullYear());
  yearEls.forEach(function (el) {
    el.textContent = year;
  });

  // Contact form: client-side validation only (no secrets, no network writes)
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.querySelector("[name='name']");
      var email = form.querySelector("[name='email']");
      var ok = true;
      if (!name || !name.value.trim()) ok = false;
      if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) ok = false;
      var status = document.querySelector("[data-form-status]");
      if (status) {
        status.textContent = ok
          ? "Thank you — our team will respond within one business day."
          : "Please provide a valid name and email address.";
        status.setAttribute("role", "status");
      }
    });
  }
})();
