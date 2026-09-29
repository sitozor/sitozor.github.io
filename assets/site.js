(function () {
  var text = window.SITE_TEXT || {copy: "Copy", copied: "Copied", failed: "Failed"};

  document.querySelectorAll(".tabs button").forEach(function (tab) {
    tab.addEventListener("click", function () {
      document.querySelectorAll(".tabs button").forEach(function (other) {
        other.setAttribute("aria-selected", String(other === tab));
      });
      document.querySelectorAll("[data-panel]").forEach(function (panel) {
        panel.hidden = panel.getAttribute("data-panel") !== tab.getAttribute("data-tab");
      });
    });
  });

  document.querySelectorAll(".code-wrap .copy").forEach(function (button) {
    button.addEventListener("click", function () {
      var code = button.parentElement.querySelector("pre").innerText.replace(/\s+# macOS.*$/m, "");
      function done(label) {
        button.textContent = label;
        setTimeout(function () { button.textContent = text.copy; }, 2000);
      }
      if (navigator.clipboard) {
        navigator.clipboard.writeText(code).then(function () { done(text.copied); }, function () { done(text.failed); });
      } else {
        done(text.failed);
      }
    });
  });

  // An explicit choice always wins over the automatic browser-language redirect.
  document.querySelectorAll(".lang-switch").forEach(function (link) {
    link.addEventListener("click", function () {
      try { localStorage.setItem("lang", link.getAttribute("data-lang")); } catch (e) {}
    });
  });
})();
