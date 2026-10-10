import asyncio, re, sys
from playwright.async_api import async_playwright

URLS = ["https://www.lr-czech.com/parfemy-damske", "https://www.lr-czech.com/aloe-vera-care"]

async def main():
    out = []
    async with async_playwright() as p:
        for headless in (True, False):
            try:
                b = await p.chromium.launch(headless=headless, args=["--disable-blink-features=AutomationControlled"])
                ctx = await b.new_context(locale="cs-CZ", user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36", viewport={"width": 1366, "height": 900})
                await ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
                pg = await ctx.new_page()
                for u in URLS:
                    r = await pg.goto(u, wait_until="domcontentloaded", timeout=60000)
                    for i in range(20):
                        t = await pg.title()
                        if "Just a moment" not in t:
                            break
                        await pg.wait_for_timeout(1500)
                    html = await pg.content()
                    codes = re.findall(r"Kód\s*</?[^>]*>?\s*([\w-]+)", html)
                    out.append(f"headless={headless} {u} status={r.status if r else None} title={await pg.title()!r} len={len(html)} cards={html.count('product-card__name')} nenisklad={html.count('Není skladem')}")
                await b.close()
            except Exception as e:
                out.append(f"headless={headless} ERROR {e!r}"[:300])
    open("test/lr_vysledek.txt", "w").write("\n".join(out) + "\n")
    print("\n".join(out))

asyncio.run(main())
