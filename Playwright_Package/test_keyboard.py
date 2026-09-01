from playwright.sync_api import Page

class TestKeyboardActions:
    def test_refresh_page(self, page:Page):
        page.goto("https://selenium.qabible.in/simple-form-demo.php")
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
        page.wait_for_timeout(300)

    def test_press_enter(self, page: Page):
        page.goto("https://selenium.qabible.in/simple-form-demo.php")
        msg = page.get_by_placeholder("Message")
        msg.fill("Hello World")
        page.wait_for_timeout(3000)
        msg.press("Enter")
        page.wait_for_timeout(3000)

    def test_tab_key(self, page:Page):
        page.goto("https://selenium.qabible.in/simple-form-demo.php")
        msg = page.get_by_placeholder("Message")
        msg.fill("Hello World")
        page.wait_for_timeout(3000)
        msg.press("Tab")
        page.wait_for_timeout(3000)

    def test_tab_enter(self, page:Page):
        page.goto("https://selenium.qabible.in/simple-form-demo.php")
        msg = page.get_by_placeholder("Message")
        msg.fill("Hello World")
        page.wait_for_timeout(3000)
        msg.press("Tab")
        page.wait_for_timeout(3000)
        msg.press("Enter")
        page.wait_for_timeout(3000)

    def test_backspace(self,page:Page):
        pass


    def test_combination(self,page:Page):
        page.goto("https://selenium.qabible.in/simple-form-demo.php")
        msg = page.get_by_placeholder("Message")
        msg.fill("Hello World")
        page.wait_for_timeout(3000)
        msg.press("Control+A")
        page.wait_for_timeout(4000)
        msg.press("Backspace")
        page.wait_for_timeout(3000)