from playwright.sync_api import Page,expect
from Pages.login_page import LoginPage
import pytest
from Url.link import MAINLINK


class TestLogin:


    @pytest.mark.parametrize("username,password", [("jesma","123")])
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_valid_user_password(self, page: Page,username,password):
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")
        login=LoginPage(page)

        login.login_button_click().enter_username(username).enter_password(password).confirm_login_button()

      #  expect(page.locator("//a[@id='nameofuser']")).to_be_visible()
        welcome_message=page.locator("a[id='nameofuser']")
        expect(welcome_message).to_contain_text("Welcome")


    @pytest.mark.parametrize("username1,password1",[ ("user0name", "123"), ("jesma", "pass0word"),("user0name", "pass0word")])
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_invalid_user_password(self, page: Page,username1,password1):
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")
        login = LoginPage(page)

        login.login_button_click().enter_username(username1).enter_password(password1).with_alert()









    '''def test_login_valid_user_invalid_password(self, page: Page):
        page.goto("https://www.demoblaze.com/", wait_until="domcontentloaded")
        login = LoginPage(page)
        page.wait_for_timeout(2000)
        login.login_button_click()
        page.wait_for_timeout(2000)
        login.enter_username("jesma")
        page.wait_for_timeout(2000)
        login.enter_password("pass0word")
        page.wait_for_timeout(2000)
        # alert message due invalid user and password
        login.with_alert()
        page.wait_for_timeout(6000)

    def test_login_invalid_user_invalid_password(self, page: Page):
        page.goto("https://www.demoblaze.com/", wait_until="domcontentloaded")
        login = LoginPage(page)
        page.wait_for_timeout(2000)
        login.login_button_click()
        page.wait_for_timeout(2000)
        login.enter_username("user0name")
        page.wait_for_timeout(2000)
        login.enter_password("pass0word")
        page.wait_for_timeout(2000)
        # alert message due invalid user and password
        login.with_alert()
        page.wait_for_timeout(8000)'''
