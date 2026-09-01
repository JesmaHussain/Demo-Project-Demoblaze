from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    new_page=browser.new_page()
    new_page.goto("https://www.wikipedia.com")
    new_page.wait_for_timeout(4000)
    display=new_page.title()
    print(display)
    #browser.close()