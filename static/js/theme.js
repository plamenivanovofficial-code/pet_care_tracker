/*
 * Превключвател между тъмна и светла тема.
 * Изборът се пази в localStorage на браузъра, за да остане при следващо отваряне.
 */
(function () {
    var STORAGE_KEY = 'pc-theme';
    var root = document.documentElement;

    function savedTheme() {
        try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
    }

    function applyTheme(theme) {
        root.setAttribute('data-theme', theme);
        var label = document.querySelector('[data-theme-label]');
        if (label) {
            label.textContent = theme === 'dark' ? 'Светла тема' : 'Тъмна тема';
        }
    }

    // Прилага се веднага (скриптът е в <head>), за да няма премигване.
    applyTheme(savedTheme() || 'dark');

    document.addEventListener('DOMContentLoaded', function () {
        applyTheme(root.getAttribute('data-theme'));

        var button = document.querySelector('[data-theme-toggle]');
        if (!button) { return; }

        button.addEventListener('click', function () {
            var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            try { localStorage.setItem(STORAGE_KEY, next); } catch (e) { /* няма достъп до storage */ }
        });
    });
})();
