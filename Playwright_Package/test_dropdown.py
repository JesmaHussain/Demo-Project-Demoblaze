from playwright.sync_api import Page
import time
class TestDropdown:
    def test_dropdown(self,page: Page):
        page.goto("https://selenium.qabible.in/select-input.php")
        #using with ID
        page.select_option("#single-input-field",index=1)
        time.sleep(2)
        #using with value
        print(page.locator("div[id='message-one']").text_content())
        page.select_option("#single-input-field",value="Yellow")
        time.sleep(2)
        print(page.locator("div[id='message-one']").text_content())
        time.sleep(2)
        #using with chaining methods
        page.locator(".form-control").first.select_option(value="Green")
        print(page.locator("div[id='message-one']").text_content())
        time.sleep(2)