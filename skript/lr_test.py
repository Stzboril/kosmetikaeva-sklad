"""Diagnostika: zda jde lr-czech.com stáhnout ze serverů GitHubu skutečným prohlížečem."""
import re
from playwright.sync_api import sync_playwright

URLS = ["https://www.lr-czech.com/zdravi", "https://www.lr-czech.com/parfemy"]

with sync_playwright() as p:
    for headless in (False, True):
        b = p.chromium.launch(headless=headless, args=["--disable-blink-features=AutomationControlled"])
        ctx = b.new_context(locale="cs-CZ", viewport={"width": 1366, "height": 900})
        ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
        page = ctx.new_page()
        for url in URLS:
            try:
                r = page.goto(url, wait_until="domcontentloaded", timeout=60000)
                for _ in range(20):  # až 40 s na vyřešení výzvy
                    if "Just a moment" not in page.title():
                        break
                    page.wait_for_timeout(2000)
                text = page.inner_text("body")
                print(f"[headless={headless}] {url} status={r.status if r else '-'} title={page.title()[:60]} "
                      f"pocet_Kod={text.count('Kód')}")
                i = text.find("Kód")
                if i >= 0:
                    print("  ukazka:", re.sub(r"\s+", " ", text[max(0, i - 400):i + 300]))
            except Exception as e:
                print(f"[headless={headless}] {url} chyba: {e}")
        b.close()
