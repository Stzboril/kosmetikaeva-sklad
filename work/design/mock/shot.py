import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':900},device_scale_factor=1)
    for k in sys.argv[1:]:
        pg.goto(f'file:///home/claude/work/design/mock/navrh_{k}.html'); pg.wait_for_timeout(600)
        pg.screenshot(path=f'navrh_{k}.png',full_page=True)
    b.close()
