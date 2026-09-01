from playwright.sync_api import Page
import time
class TestLogin:
    def test_page(self,page:Page):
        time.sleep(3)
        page.goto("https://www.wikipedia.org/")
        time.sleep(3)
        print(page.url)
        assert "wikipedia" in page.url
        page.locator("#searchInput").type("India")
        time.sleep(3)
        print (page.title())
        assert "Wikipedia"in page.title()
        #page.get_by_role("button",name="search").click()
        page.locator("#searchInput").press("Enter")
        time.sleep(3)
        print(page.url)
        print(page.title())
        assert "India" in page.url
        assert "India" in page.title()
        page.close()