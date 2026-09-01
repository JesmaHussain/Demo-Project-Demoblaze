from playwright.sync_api import Page
import time
class TestWebelementsCommands:
    def test_webelements(self,page:Page):
        page.goto("https://selenium.qabible.in/simple-form-demo.php")
        time.sleep(3)
        page.locator("#single-input-field").fill("hello jesma")
        time.sleep(3)
        page.get_by_role("button",name="Show Message").click()
        time.sleep(3)
        result=page.locator("div[id='message-one']")
        print(result.text_content())
        time.sleep(3)
        page.get_by_placeholder("Enter Value").first.fill("46")
        time.sleep(3)
        page.locator(".form-control").last.fill("56")
        page.get_by_role("button",name="Get Total").click()
        time.sleep(3)
        total=page.locator("//div[@id='message-two']")
        print(total.text_content())

