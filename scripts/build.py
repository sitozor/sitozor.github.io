"""Build the Russian and English pages from one template.

    python3 scripts/build.py

Writes index.html (Russian, the default for sitozor.ru) and en/index.html.
Edit texts in CONTENT below, not in the generated files.
"""

from html import escape
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://sitozor.ru"
GITHUB = "https://github.com/HackToolWork/web-audit-pro"
TELEGRAM = "https://t.me/xxx_5d"

ICONS = {
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.4 8.4 8 9 4.6-.6 8-4 8-9V6z"/>',
    "code": '<path d="M14 7 10 17"/><path d="m7 9-4 3 4 3"/><path d="m17 9 4 3-4 3"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="m10.8 12.2 8.2-8.2"/><path d="m16 7 2 2"/>'
    '<path d="m18 5 2 2"/>',
}
SHIELD_LOGO = (
    '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 2 4 7v8c0 7.5 5.1 13.4 12 15 '
    '6.9-1.6 12-7.5 12-15V7z" fill="currentColor" style="color:var(--accent)"/><path '
    'd="m10.5 16 4 4 7-8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)

CONTENT = {
    "ru": {
        "path": "/",
        "title": "Сайтозор — бесплатная проверка безопасности сайта",
        "description": "Открытый инструмент: проверяет SSL-сертификат, защиту почты, настройки "
        "безопасности и плагины WordPress и выдаёт понятный отчёт на русском языке.",
        "nav": ["Возможности", "Установка", "Мониторинг", "Вопросы"],
        "switch_label": "English",
        "h1": "Бесплатная проверка безопасности сайта — с понятным отчётом",
        "lead": "Открытый инструмент: проверяет SSL-сертификат, защиту почты от подделки, "
        "настройки безопасности и плагины WordPress — и объясняет на русском языке, что не так "
        "и что именно сделать.",
        "cta_install": "Установить бесплатно",
        "cta_example": "Пример отчёта",
        "hero_note": "Открытый инструмент <a href=\"$github\" target=\"_blank\" rel=\"noopener\">"
        "web-audit-pro</a> под лицензией Apache-2.0 · звезда на GitHub помогает проекту",
        "mock_status": "Требуются срочные действия",
        "mock_sub": "shop.example · пример отчёта",
        "mock_items": [
            ("red", "Срочно", "SSL-сертификат истекает через 9 дней"),
            ("red", "Срочно", "Плагин «elementor» содержит известные уязвимости"),
            ("yellow", "Важно", "Почта домена не защищена от подделки"),
            ("green", "Исправлено", "Сайт больше нельзя встроить в чужую страницу"),
        ],
        "checks_h2": "Что проверяем",
        "checks_sub": "Самые частые причины, по которым небольшие сайты теряют клиентов, "
        "попадают в спам или оказываются взломаны.",
        "checks": [
            ("lock", "SSL-сертификат", "Действует ли сертификат и когда истекает. Истёкший "
             "сертификат — это предупреждение «сайт небезопасен» у каждого посетителя."),
            ("mail", "Защита почты", "Записи SPF и DMARC. Без них мошенники могут рассылать письма "
             "от имени вашего домена, а ваши письма чаще попадают в спам."),
            ("shield", "Настройки безопасности", "Защитные заголовки, cookies, перенаправления — "
             "то, что закрывает сайт от распространённых атак через браузер."),
            ("code", "WordPress и плагины", "Версия WordPress, список плагинов и тем, сверка "
             "версий с базой известных уязвимостей."),
            ("key", "Утечки ключей", "Ключи доступа к платным сервисам, случайно оставленные в коде, "
             "который видят посетители."),
        ],
        "report_h2": "Отчёт, понятный не только программистам",
        "report_sub": "Кроме технических отчётов (HTML, JSON, SARIF) инструмент создаёт отдельный "
        "отчёт для владельца сайта.",
        "report_points": [
            "Светофор: всё хорошо, есть замечания или нужны срочные действия",
            "Для каждой проблемы — что это значит и что сделать",
            "Что изменилось с прошлой проверки; исправления подтверждаются повторной проверкой",
            "Ваш логотип и название — удобно для веб-студий",
            "Один HTML-файл, сохраняется в PDF через печать",
        ],
        "report_cta": "Открыть пример отчёта",
        "changes_title": "Изменения с прошлой проверки",
        "changes_items": [
            ("green", "Исправлено", "SPF разрешал отправлять почту от вашего имени кому угодно"),
            ("green", "Исправлено", "Сайт можно было встроить в чужую страницу"),
            ("red", "Новое", "SSL-сертификат скоро истечёт"),
        ],
        "install_h2": "Установка",
        "install_sub": "Инструмент Сайтозора распространяется на GitHub под названием "
        "<code>web-audit-pro</code>. Нужен Python 3.11 или новее. Проверяйте только свои сайты "
        "или сайты, на проверку которых у вас есть разрешение.",
        "tabs": ["Linux (Kali, Debian, Ubuntu)", "Docker", "Windows / macOS"],
        "site_placeholder": "https://ваш-сайт.ru",
        "macos_comment": "# macOS: source .venv/bin/activate",
        "run_h3": "Проверка сайта",
        "run_extra": ' --company "Моя студия"',
        "run_note": "Отчёты появятся в папке <code>reports/</code>; отчёт для владельца — файл "
        "<code>owner-report-*.html</code>. Язык отчёта берётся из настроек системы. Подробности — "
        "в <a href=\"$github#readme\" target=\"_blank\" rel=\"noopener\">документации</a>.",
        "copy": "Копировать",
        "copied": "Скопировано",
        "copy_failed": "Не удалось",
        "monitoring_h2": "Не хотите ничего устанавливать?",
        "monitoring_sub": "Готовим автоматический мониторинг: сервис сам проверяет сайт и пишет, "
        "если что-то сломалось. Бесплатная версия инструмента остаётся бесплатной навсегда.",
        "free_title": "Инструмент",
        "free_price": "0 ₽ <small>навсегда</small>",
        "free_points": [
            "Все проверки и все отчёты",
            "Ваш логотип в отчётах",
            "Запуск на своём компьютере или сервере",
            "Открытый код",
        ],
        "free_cta": "Установить",
        "soon": "Скоро",
        "paid_title": "Мониторинг",
        "paid_price": "от 390 ₽ <small>/ мес · планируемая цена</small>",
        "paid_points": [
            "Ничего не нужно устанавливать — только адрес сайта",
            "Автоматическая проверка каждую неделю или каждый день",
            "Уведомления в Telegram, если истекает сертификат или найдена уязвимость",
            "История изменений и ежемесячный отчёт",
            "Для студий: сайты клиентов и отчёты с вашим логотипом",
        ],
        "paid_cta": "Узнать о запуске первым",
        "faq_h2": "Частые вопросы",
        "faq": [
            ("Это действительно бесплатно?", "Да. Инструмент распространяется с открытым кодом "
             "под лицензией Apache-2.0 — его можно использовать, в том числе в коммерческих целях. "
             "Платным будет только готовый сервис мониторинга, где не нужно ничего устанавливать."),
            ("Это не взлом? Сайту ничего не будет?", "Нет. Инструмент делает только обычные "
             "запросы — такие же, как браузер при посещении сайта, — с ограничением скорости. Он не "
             "подбирает пароли, не отправляет вредоносные данные и не нагружает сервер. Проверяйте "
             "только свои сайты или сайты, на проверку которых у вас есть разрешение."),
            ("Нужно ли быть программистом?", "Нужно уметь установить программу и запустить одну "
             "команду в терминале — инструкция выше. Если это неудобно, подождите запуска "
             "мониторинга: там будет достаточно ввести адрес сайта."),
            ("Откуда данные об уязвимостях WordPress?", "Из базы Wordfence Intelligence. Её можно "
             "бесплатно скачать командой <code>web-audit --update-wp-db</code> (нужен бесплатный "
             "API-ключ Wordfence) — дальше проверки работают без интернета."),
            ("Гарантирует ли отчёт, что сайт не взломают?", "Нет, и мы честно об этом пишем. "
             "Автоматическая проверка находит самые распространённые проблемы, но не заменяет "
             "полноценный аудит безопасности."),
            ("Как помочь проекту?", "Поставьте звезду на <a href=\"$github\" target=\"_blank\" "
             "rel=\"noopener\">GitHub</a>, расскажите коллегам, сообщайте об ошибках и предлагайте "
             "улучшения в Issues."),
        ],
        "footer_left": "© 2026 Сайтозор · инструмент web-audit-pro под лицензией Apache-2.0",
        "footer_right": "Сайт не собирает персональные данные и не использует cookies.",
    },
    "en": {
        "path": "/en/",
        "title": "Sitozor — free website security check",
        "description": "An open-source tool that checks the SSL certificate, email spoofing "
        "protection, security settings and WordPress plugins, and explains the results in plain "
        "language.",
        "nav": ["Features", "Install", "Monitoring", "FAQ"],
        "switch_label": "Русский",
        "h1": "Free website security check — with a report anyone can read",
        "lead": "An open-source tool that checks your SSL certificate, email spoofing protection, "
        "security settings and WordPress plugins — and explains in plain language what is wrong "
        "and exactly what to do.",
        "cta_install": "Install for free",
        "cta_example": "Example report",
        "hero_note": "Open-source <a href=\"$github\" target=\"_blank\" rel=\"noopener\">"
        "web-audit-pro</a> under the Apache-2.0 license · a star on GitHub helps the project",
        "mock_status": "Urgent action needed",
        "mock_sub": "shop.example · example report",
        "mock_items": [
            ("red", "Urgent", "SSL certificate expires in 9 days"),
            ("red", "Urgent", "Plugin 'elementor' has known vulnerabilities"),
            ("yellow", "Important", "Domain email is not protected from spoofing"),
            ("green", "Fixed", "The site can no longer be embedded in other pages"),
        ],
        "checks_h2": "What we check",
        "checks_sub": "The most common reasons small websites lose customers, land in spam folders "
        "or get hacked.",
        "checks": [
            ("lock", "SSL certificate", "Whether the certificate is valid and when it expires. An "
             "expired certificate means a 'not secure' warning for every visitor."),
            ("mail", "Email protection", "SPF and DMARC records. Without them, scammers can send "
             "email in your domain's name, and your own mail lands in spam more often."),
            ("shield", "Security settings", "Security headers, cookies and redirects — what "
             "protects the site from common browser-based attacks."),
            ("code", "WordPress and plugins", "The WordPress version, plugins and themes, checked "
             "against a database of known vulnerabilities."),
            ("key", "Leaked keys", "Access keys to paid services accidentally left in code that "
             "visitors can see."),
        ],
        "report_h2": "A report that is not just for programmers",
        "report_sub": "Besides technical reports (HTML, JSON, SARIF), the tool creates a separate "
        "report for the site owner.",
        "report_points": [
            "Traffic light: all good, issues found, or urgent action needed",
            "For every issue — what it means and what to do",
            "What changed since the last check; fixes are confirmed by a recheck",
            "Your logo and name — handy for web studios",
            "A single HTML file that prints nicely to PDF",
        ],
        "report_cta": "Open the example report",
        "changes_title": "Changes since the last check",
        "changes_items": [
            ("green", "Fixed", "SPF allowed anyone to send email in your name"),
            ("green", "Fixed", "The site could be embedded in other pages"),
            ("red", "New", "SSL certificate expires soon"),
        ],
        "install_h2": "Install",
        "install_sub": "Sitozor's tool is published on GitHub as <code>web-audit-pro</code>. It "
        "needs Python 3.11 or newer. Only check sites you own or are allowed to test.",
        "tabs": ["Linux (Kali, Debian, Ubuntu)", "Docker", "Windows / macOS"],
        "site_placeholder": "https://your-site.com",
        "macos_comment": "# macOS: source .venv/bin/activate",
        "run_h3": "Check a site",
        "run_extra": ' --company "My Studio"',
        "run_note": "Reports appear in the <code>reports/</code> folder; the owner report is "
        "<code>owner-report-*.html</code>. The report language follows your system settings. "
        "See the <a href=\"$github#readme\" target=\"_blank\" rel=\"noopener\">documentation</a> "
        "for details.",
        "copy": "Copy",
        "copied": "Copied",
        "copy_failed": "Failed",
        "monitoring_h2": "Don't want to install anything?",
        "monitoring_sub": "We are building automatic monitoring: the service checks your site on "
        "its own and tells you when something breaks. The free tool stays free forever.",
        "free_title": "Tool",
        "free_price": "$0 <small>forever</small>",
        "free_points": [
            "Every check and every report",
            "Your logo in reports",
            "Runs on your own computer or server",
            "Open source",
        ],
        "free_cta": "Install",
        "soon": "Coming soon",
        "paid_title": "Monitoring",
        "paid_price": "<small>Pricing will be announced</small>",
        "paid_points": [
            "Nothing to install — just your site's address",
            "Automatic weekly or daily checks",
            "Alerts when a certificate is expiring or a vulnerability is found",
            "Change history and a monthly report",
            "For studios: client sites and reports with your logo",
        ],
        "paid_cta": "Get notified at launch",
        "faq_h2": "FAQ",
        "faq": [
            ("Is it really free?", "Yes. The tool is open source under the Apache-2.0 license — "
             "you can use it, including commercially. Only the hosted monitoring service, where "
             "nothing needs to be installed, will be paid."),
            ("Is this hacking? Will it harm my site?", "No. The tool only makes ordinary requests — "
             "the same ones a browser makes when visiting a site — with rate limiting. It does not "
             "guess passwords, send malicious data or overload the server. Only check sites you "
             "own or are allowed to test."),
            ("Do I need to be a programmer?", "You need to install the program and run one command "
             "in a terminal — see the instructions above. If that is inconvenient, wait for the "
             "monitoring service: entering your site's address will be enough."),
            ("Where does the WordPress vulnerability data come from?", "From Wordfence "
             "Intelligence. You can download it for free with <code>web-audit --update-wp-db</code> "
             "(a free Wordfence API key is required); checks then work offline."),
            ("Does the report guarantee my site won't be hacked?", "No, and we say so honestly. "
             "An automated check finds the most common problems but does not replace a full "
             "security audit."),
            ("How can I help?", "Star the project on <a href=\"$github\" target=\"_blank\" "
             "rel=\"noopener\">GitHub</a>, tell your colleagues, report bugs and suggest "
             "improvements in Issues."),
        ],
        "footer_left": "© 2026 Sitozor · web-audit-pro tool under the Apache-2.0 license",
        "footer_right": "This site collects no personal data and uses no cookies.",
    },
}

# Only the Russian root page redirects, once, for visitors whose browser prefers another
# language and who have not chosen a language before. Crawlers are never redirected.
AUTO_REDIRECT = """<script>
(function () {
  var saved = null;
  try { saved = localStorage.getItem("lang"); } catch (e) {}
  if (/bot|crawl|spider|slurp|yandex|google|bing|duckduck/i.test(navigator.userAgent)) return;
  var preferred = (navigator.languages && navigator.languages[0]) || navigator.language || "";
  if (saved === "en" || (!saved && preferred && !/^ru\\b/i.test(preferred))) {
    location.replace("/en/" + location.hash);
  }
})();
</script>"""

TEMPLATE = Template("""<!doctype html>
<html lang="$lang">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$description">
<link rel="canonical" href="$site$path">
<link rel="alternate" hreflang="ru" href="$site/">
<link rel="alternate" hreflang="en" href="$site/en/">
<link rel="alternate" hreflang="x-default" href="$site/">
<meta property="og:type" content="website">
<meta property="og:url" content="$site$path">
<meta property="og:title" content="$title">
<meta property="og:description" content="$description">
<meta name="theme-color" content="#1f4fb8">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M16 2 4 7v8c0 7.5 5.1 13.4 12 15 6.9-1.6 12-7.5 12-15V7z' fill='%231f4fb8'/%3E%3Cpath d='m10.5 16 4 4 7-8' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="stylesheet" href="/assets/style.css">
$redirect
</head>
<body>

<div class="wrap">
  <header class="top">
    <a class="brand" href="$path">$logo$brand</a>
    <nav>
      <a href="#checks">$nav0</a>
      <a href="#install">$nav1</a>
      <a href="#monitoring">$nav2</a>
      <a href="#faq">$nav3</a>
      <a href="$github" target="_blank" rel="noopener">GitHub</a>
    </nav>
    <a class="lang-switch" href="$other_path" data-lang="$other_lang" hreflang="$other_lang">$switch_label</a>
  </header>

  <div class="hero">
    <div>
      <h1>$h1</h1>
      <p class="lead">$lead</p>
      <div class="actions">
        <a class="btn btn-primary" href="#install">$cta_install</a>
        <a class="btn btn-ghost" href="${path}example-report.html" target="_blank" rel="noopener">$cta_example</a>
      </div>
      <p class="note">$hero_note</p>
    </div>
    <div class="mock" aria-label="$cta_example">
      <div class="status">
        <div class="dot"></div>
        <div><strong>$mock_status</strong><span>$mock_sub</span></div>
      </div>
      <ul>$mock_items</ul>
    </div>
  </div>
</div>

<section id="checks" class="band">
  <div class="wrap">
    <h2>$checks_h2</h2>
    <p class="sub">$checks_sub</p>
    <div class="grid">$checks</div>
  </div>
</section>

<section id="report">
  <div class="wrap two">
    <div>
      <h2>$report_h2</h2>
      <p class="sub">$report_sub</p>
      <ul class="checks">$report_points</ul>
      <p><a class="btn btn-ghost" href="${path}example-report.html" target="_blank" rel="noopener">$report_cta</a></p>
    </div>
    <div class="mock">
      <strong>$changes_title</strong>
      <ul>$changes_items</ul>
    </div>
  </div>
</section>

<section id="install" class="band">
  <div class="wrap">
    <h2>$install_h2</h2>
    <p class="sub">$install_sub</p>
    <div class="tabs" role="tablist">
      <button type="button" role="tab" aria-selected="true" data-tab="linux">$tab0</button>
      <button type="button" role="tab" aria-selected="false" data-tab="docker">$tab1</button>
      <button type="button" role="tab" aria-selected="false" data-tab="python">$tab2</button>
    </div>
    <div data-panel="linux">
      <div class="code-wrap"><pre class="code">git clone $github.git
cd web-audit-pro
sudo ./install.sh</pre><button type="button" class="copy">$copy</button></div>
    </div>
    <div data-panel="docker" hidden>
      <div class="code-wrap"><pre class="code">git clone $github.git
cd web-audit-pro
docker build -t web-audit-pro:local .
mkdir -p reports
docker run --rm -u "$$(id -u):$$(id -g)" -v "$$PWD/reports:/app/reports" \\
  web-audit-pro:local $site_placeholder --yes-i-am-authorized --lang $lang</pre><button type="button" class="copy">$copy</button></div>
    </div>
    <div data-panel="python" hidden>
      <div class="code-wrap"><pre class="code">git clone $github.git
cd web-audit-pro
python -m venv .venv
.venv\\Scripts\\activate        <span class="c">$macos_comment</span>
python -m pip install .</pre><button type="button" class="copy">$copy</button></div>
    </div>
    <h3 style="margin:28px 0 10px">$run_h3</h3>
    <div class="code-wrap"><pre class="code">web-audit $site_placeholder$run_extra</pre><button type="button" class="copy">$copy</button></div>
    <p class="sub" style="margin:0">$run_note</p>
  </div>
</section>

<section id="monitoring">
  <div class="wrap">
    <h2>$monitoring_h2</h2>
    <p class="sub">$monitoring_sub</p>
    <div class="free-vs">
      <div class="card">
        <h3>$free_title</h3>
        <div class="price">$free_price</div>
        <ul>$free_points</ul>
        <a class="btn btn-ghost" href="#install">$free_cta</a>
      </div>
      <div class="card soon">
        <span class="badge-soon">$soon</span>
        <h3 style="margin-top:12px">$paid_title</h3>
        <div class="price">$paid_price</div>
        <ul>$paid_points</ul>
        <a class="btn btn-primary" href="$telegram" target="_blank" rel="noopener">$paid_cta</a>
      </div>
    </div>
  </div>
</section>

<section id="faq" class="band">
  <div class="wrap">
    <h2>$faq_h2</h2>
    $faq
  </div>
</section>

<footer>
  <div class="wrap">
    <span>$footer_left</span>
    <span>$footer_right <a href="$github" target="_blank" rel="noopener">GitHub</a> · <a href="$telegram" target="_blank" rel="noopener">Telegram</a></span>
  </div>
</footer>

<script>window.SITE_TEXT = {copy: "$copy", copied: "$copied", failed: "$copy_failed"};</script>
<script src="/assets/site.js"></script>
</body>
</html>
""")


def _pills(items):
    return "".join(
        f'\n        <li><span class="pill {color}">{escape(label)}</span> {escape(text)}</li>'
        for color, label, text in items
    )


def _list(points):
    return "".join(f"\n          <li>{escape(point)}</li>" for point in points)


def render(lang: str) -> str:
    text = CONTENT[lang]
    other = "en" if lang == "ru" else "ru"
    checks = "".join(
        f'\n      <div class="card"><div class="icon"><svg viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        f"{ICONS[icon]}</svg></div><h3>{escape(title)}</h3><p>{escape(body)}</p></div>"
        for icon, title, body in text["checks"]
    )
    faq = "".join(
        f'\n    <details class="faq"><summary>{escape(question)}</summary>'
        f"<p>{answer.replace('$github', GITHUB)}</p></details>"
        for question, answer in text["faq"]
    )
    values = {
        key: value
        for key, value in text.items()
        if isinstance(value, str) and key not in {"hero_note", "install_sub", "run_note"}
    }
    values = {key: escape(value, quote=True) for key, value in values.items()}
    # These fields intentionally contain markup and were written by us.
    for key in ("hero_note", "install_sub", "run_note", "free_price", "paid_price"):
        values[key] = text[key].replace("$github", GITHUB)
    values.update(
        lang=lang,
        site=SITE,
        github=GITHUB,
        telegram=TELEGRAM,
        logo=SHIELD_LOGO,
        brand="Сайтозор" if lang == "ru" else "Sitozor",
        other_lang=other,
        other_path=CONTENT[other]["path"],
        redirect=AUTO_REDIRECT if lang == "ru" else "",
        mock_items=_pills(text["mock_items"]),
        changes_items=_pills(text["changes_items"]),
        checks=checks,
        report_points=_list(text["report_points"]),
        free_points=_list(text["free_points"]),
        paid_points=_list(text["paid_points"]),
        faq=faq,
        **{f"nav{i}": escape(item) for i, item in enumerate(text["nav"])},
        **{f"tab{i}": escape(item) for i, item in enumerate(text["tabs"])},
    )
    return TEMPLATE.substitute(values)


def main() -> None:
    for lang, text in CONTENT.items():
        target = ROOT / text["path"].strip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(lang), encoding="utf-8")
        print(f"Wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
