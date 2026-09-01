from playwright.sync_api import Page


class TestLocators:

    def test_all_locators(self, page: Page):

        page.goto("C:\Users\Jesma hussain\PycharmProjects\PlaywrightProject\Playwright_Package\demo.html")

        # get_by_label()
        page.get_by_label("Username").fill("Deepa")

        page.get_by_label("Password").fill("abc123")

        # get_by_placeholder()
        page.get_by_placeholder("Enter Username").fill("Maya")

        # click()
        page.get_by_role("checkbox", name="Remember Me").click()

        # get_by_role()
        page.get_by_role("radio", name="Male").click()

        # click button
        page.get_by_role("button", name="Login").click()

        # get_by_text()
        assert page.get_by_text(
            "Welcome to Playwright Practice Page"
        ).is_visible()

        # click link
        page.get_by_role("link", name="Forgot Password").click()
