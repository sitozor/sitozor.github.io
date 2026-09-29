# Сайтозор — страница проекта

Страница бесплатного открытого инструмента
[web-audit-pro](https://github.com/HackToolWork/web-audit-pro) на двух языках:
`/` — русский, `/en/` — английский. Посетитель с неанглоязычным браузером
остаётся на русской версии; с другим языком браузера при первом заходе
переходит на `/en/`. Выбор в переключателе языка запоминается, поисковые роботы
не перенаправляются. Сайт не собирает персональные данные и не использует cookies.

## Как менять тексты

Страницы собираются из одного шаблона — правьте тексты в `scripts/build.py`
(словарь `CONTENT`), а не в `index.html` и `en/index.html`:

```bash
python3 scripts/build.py
```

Общие стили — `assets/style.css`, скрипты — `assets/site.js`.

Примеры отчётов (`example-report.html`, `en/example-report.html`) создаются
настоящим генератором отчётов web-audit-pro:

```bash
~/Music/web-audit-pro/.venv/bin/python scripts/make_example_report.py
```

## Публикация

Сайт публикуется GitHub Pages из ветки `main` репозитория
`sitozor/sitozor.github.io` и доступен по адресу https://sitozor.ru
(файл `CNAME`). DNS домена у REG.RU: четыре A-записи `@` на адреса GitHub Pages
185.199.108–111.153, CNAME `www` → `sitozor.github.io.`, SPF `v=spf1 -all` и
DMARC `p=reject` (домен не отправляет почту). Домен подтверждён в настройках
организации GitHub (TXT `_github-pages-challenge-sitozor`) — не удаляйте эту запись.
