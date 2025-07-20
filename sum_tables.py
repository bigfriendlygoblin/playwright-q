from playwright.sync_api import sync_playwright
import re

SEEDS = range(55, 65)
TOTAL = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    for seed in SEEDS:
        url = f"https://ds3.orth.xyz/table?seed={seed}"
        page.goto(url)
        content = page.content()
        nums = list(map(float, re.findall(r"\d+(?:\.\d+)?", content)))
        seed_sum = sum(nums)
        print(f"Seed {seed}: {seed_sum}")
        TOTAL += seed_sum

    print(f"FINAL TOTAL SUM = {TOTAL}")
    browser.close()
