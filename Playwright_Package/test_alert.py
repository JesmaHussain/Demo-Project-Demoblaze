from playwright.sync_api import Page
import time
class TestMessageAlert:
    '''def test_message_simplealert(self,page:Page):
        page.goto("https://selenium.qabible.in/javascript-alert.php")
        page.on("dialog", lambda dialog: (print("Alert message:", dialog.message), dialog.accept()))
        page.locator("//button[text()='Click me!']").nth(0).click()
        #page.wait_for_timeout(2000)
        time.sleep(2)'''

    '''def test_message_alert_confirm(self,page:Page):
        page.goto("https://selenium.qabible.in/javascript-alert.php")
        page.on("dialog", lambda dialog: (print("Alert message:", dialog.message), dialog.accept()))
        #page.on("dialog", lambda dialog: (print("Alert message:", dialog.message), dialog.dismiss()))
        page.locator("//button[text()='Click me!']").nth(1).click()
        print(page.locator("//p[@id='confirm-demo']").text_content())
        page.wait_for_timeout(2000)'''

    def test_message_alert_prompt(self, page: Page):
        page.goto("https://selenium.qabible.in/javascript-alert.php")
        page.on("dialog", lambda dialog: (print("Alert message:", dialog.message), dialog.accept()))
        #page.on("dialog", lambda dialog: (print("Alert message:", dialog.message), dialog.dismiss()))
        page.get_by_text("Click for Prompt Box").click()
        print(page.locator("p[id='prompt-demo']").text_content())
        page.wait_for_timeout(2000)

