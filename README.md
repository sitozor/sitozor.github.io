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

## Публикация

Сайт публикуется GitHub Pages из ветки `main` репозитория
`sitozor/sitozor.github.io` и доступен по адресу https://sitozor.ru
(файл `CNAME`). DNS домена у REG.RU: четыре A-записи `@` на адреса GitHub Pages
185.199.108–111.153, CNAME `www` → `sitozor.github.io.`, SPF `v=spf1 -all` и
DMARC `p=reject` (домен не отправляет почту). Домен подтверждён в настройках
организации GitHub (TXT `_github-pages-challenge-sitozor`) — не удаляйте эту запись.
