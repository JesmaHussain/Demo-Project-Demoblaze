from playwright.sync_api import Page
import time
class TestMultipleWindow:
    def test_multiple_window(self,page:Page):
        page.goto("https://demo.guru99.com/popup.php")
        time.sleep(2)
        with page.expect_popup() as popup_info:
            page.locator("//a[text()='Click Here']").click()
        new_page=popup_info.value
        new_page.wait_for_load_state()
        print(new_page.url)
        new_page.locator("//input[@name='emailid']").fill("jesma@gmail.com")
        new_page.locator("input[value='Submit']").click()
        new_page.wait_for_load_state()
        #new_page2=popup_info1.value
        #new_page2.wait_for_load_state()
        #print(new_page2.url)
        #new_page2.locator("//a[text()='Click Here']").click()
        page.bring_to_front()
        time.sleep(2)
        print("sucessfully switched to main page")
        print(page.url)
