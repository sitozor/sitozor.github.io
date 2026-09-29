# Сайтозор — страница проекта

Статическая страница для GitHub Pages о бесплатном открытом инструменте
[web-audit-pro](https://github.com/HackToolWork/web-audit-pro):
`index.html` (возможности, установка, анонс платного мониторинга) и
`example-report.html` (пример отчёта для вымышленного сайта `shop.example`).
Сайт не собирает персональные данные; кнопка «Узнать о запуске первым» ведёт
в Telegram `@xxx_5d`.

Сменить Telegram во всех ссылках:

```bash
sed -i "s/xxx_5d/новый_ник/g" index.html
```

Планируемая цена мониторинга — в разделе `id="monitoring"` файла `index.html`.

## Пример отчёта

`example-report.html` создаётся настоящим генератором отчётов web-audit-pro.
После изменений в инструменте пересоберите его:

```bash
~/Music/web-audit-pro/.venv/bin/python scripts/make_example_report.py
```

## Публикация на GitHub Pages

Бесплатный GitHub Pages работает для публичных репозиториев:

```bash
git add -A && git commit -m "Add project page"
gh repo create HackToolWork/webaudit-landing --public --source=. --push
gh api -X POST repos/HackToolWork/webaudit-landing/pages -f "source[branch]=main" -f "source[path]=/"
```

Через 1–2 минуты страница будет доступна по адресу
`https://hacktoolwork.github.io/webaudit-landing/`.
