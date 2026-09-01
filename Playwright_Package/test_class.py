from playwright.sync_api import sync_playwright
import time

#class TestBasicCommands:

#    def test_new(self,page:Page):
#       page:Page->it tells the that variable page is an object of playwright page class
        #it is equivalent page=Page object
#       page.wait_for_timeout(2000)
#        page.goto("https://www.google.com")
#       page.wait_for_timeout(2000)
#       print(page.title())
#       page.wait_for_timeout(2000)
#       assert "Google" in page.title()
#        page.wait_for_timeout(2000)

#   def test_open_webpage(self, page: Page):
#       page.wait_for_timeout(2000)
#        page.goto("https://www.google.com")

#    def test_show_title(self, page: Page):
#        page.goto("https://www.google.com")
#        page.title()
#        assert "Google" in page.title()

#    def test_close_page(self, page: Page):
 #       page.goto("https://www.google.com")
        # page.wait_for_timeout(3000)
#       time.sleep(5)
#        page.close()

#    def test_close_browser(self, page: Page):
#       page.goto("https://www.google.com")
#        browser = page.context.browser
 #       browser.close()

#def test_url(page):
#   page.goto("https://www.wikipedia.org")

#  assert "wikipedia.org" in page.url
# print(page.url)
# 2. Verify Page Contains Specific Text

#def test_text(page):
#    page.goto("https://www.wikipedia.org")

#    text = page.locator("h1").text_content()

#    assert "Wikipedia" in text

#    print(text)

# 3. Verify Page Title of Example.com
def test_example_title(page):
    page.goto("https://www.wikipedia.org")

    assert page.title() == "Wikipedia"
    time.sleep(5)
    print(page.title())

def test_search(page):
    page.wait_for_timeout(2000)

    try:
        page.get_by_role("button",name="Accept all").click(timeout=3000)
    except:
        print("\nno popups accepted")