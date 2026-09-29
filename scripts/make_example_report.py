"""Regenerate example-report.html from web-audit-pro's real owner-report renderer.

The site is fictional (shop.example is reserved for examples) and vulnerability
titles are placeholders, so nothing here describes a real site or advisory.

Run from the landing repository root:
    ~/Music/web-audit-pro/.venv/bin/python scripts/make_example_report.py
"""

from datetime import UTC, datetime
from pathlib import Path

from web_audit.models import CheckResult
from web_audit.models import Finding as F
from web_audit.owner_report import build_owner_summary, render_owner_report_html
from web_audit.wordpress import Component
from web_audit.wordpress import findings as wordpress_findings

OUTPUT = Path(__file__).resolve().parent.parent / "example-report.html"

components = (
    Component("plugin", "elementor", "3.18.0", "/wp-content/plugins/elementor/assets/app.js"),
    Component("plugin", "woocommerce", "8.9.1", "/wp-content/plugins/woocommerce/assets/woo.css"),
    Component("plugin", "contact-form-7", None, "/wp-content/plugins/contact-form-7/index.js"),
    Component("theme", "astra", "4.6.4", "/wp-content/themes/astra/style.css"),
)
root = CheckResult(
    url="https://shop.example/",
    status=200,
    size=48213,
    elapsed_ms=180,
    scanned_at=datetime.now(UTC),
    findings=(
        F(
            "tls.certificate_expiring",
            "TLS certificate expires soon",
            "high",
            "tls",
            "shop.example:443: certificate expires on 2026-10-08 (9 day(s) left).",
            "Renew the certificate.",
        ),
        F(
            "wordpress.vulnerable.plugin.elementor",
            "Vulnerable WordPress plugin: elementor 3.18.0",
            "high",
            "vulnerable_component",
            "WordPress plugin elementor version 3.18.0 matches 2 known vulnerabilities; "
            "fixed in 3.18.2: Example: Stored Cross-Site Scripting; Example: Missing "
            "Authorization. Source: Wordfence Intelligence.",
            "Update elementor to 3.18.2 or later.",
            confidence="medium",
        ),
        F(
            "dns.dmarc.missing",
            "DMARC policy was not found",
            "medium",
            "email_security",
            "No v=DMARC1 TXT record was resolved at _dmarc.shop.example or its parent domain.",
            "Publish DMARC.",
        ),
        F(
            "cookies.secure",
            "Cookie without Secure",
            "medium",
            "cookies",
            "Set-Cookie: shop_session=…; HttpOnly; Path=/",
            "Add Secure.",
        ),
        F(
            "headers.csp",
            "Missing CSP",
            "low",
            "headers",
            "No Content-Security-Policy header.",
            "Add CSP.",
        ),
        F(
            "info.stack_headers",
            "Stack disclosure",
            "info",
            "information_disclosure",
            "X-Powered-By: PHP/8.1.2",
            "Hide versions.",
        ),
        F(
            "cms.detected.wordpress",
            "Possible WordPress installation detected",
            "info",
            "technology",
            "Detected WordPress version 6.5.3 (body:wp-content/; header:Link=api.w.org).",
            "Keep WordPress updated.",
        ),
        *wordpress_findings(components),
    ),
)
lifecycle = {
    "fixed": [
        {"rule_id": "dns.spf.permissive_all", "url": "u", "severity": "medium"},
        {"rule_id": "headers.clickjacking", "url": "u", "severity": "low"},
    ],
    "new": [{"rule_id": "tls.certificate_expiring", "url": "u", "severity": "high"}],
    "present": [
        {"rule_id": "headers.csp", "url": "u", "severity": "low"},
        {"rule_id": "dns.dmarc.missing", "url": "u", "severity": "medium"},
    ],
}
data = build_owner_summary(
    [root],
    coverage={"tls": "checked", "email": "checked", "cms": "checked", "js": "checked"},
    lifecycle=lifecycle,
    lang="ru",
    wp_vulns_checked_on=datetime.now(UTC).strftime("%Y-%m-%d"),
)
page = render_owner_report_html("https://shop.example", data, company="Сайтозор")
banner = (
    '<div style="background:#fff3cd;color:#5c4400;border-radius:10px;padding:10px 14px;'
    'margin-bottom:20px;font-size:14px">Это <strong>пример отчёта</strong> для вымышленного '
    "сайта shop.example. Названия уязвимостей условные. "
    '<a href="index.html" style="color:#5c4400">← Вернуться на главную</a></div>'
)
page = page.replace("<main>", "<main>" + banner, 1)
page = page.replace("<title>", '<meta name="robots" content="noindex"><title>Пример — ', 1)
OUTPUT.write_text(page, encoding="utf-8")
print(f"Wrote {OUTPUT} (status: {data['status']})")
