import pytest

from Pages.logout_page import Logout
from playwright.sync_api import Page
from Utilities.excel_read import NewExcelReader
from Pages.login_page import LoginPage
from Url.link import MAINLINK
class TestLogout:
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_logout(self,page:Page):
        excel = NewExcelReader()
        username = excel.read_excel_cell(2, 1)
        password = str(excel.read_excel_cell(2, 2))
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")

        login = LoginPage(page)# (calling object from LoginPage where used in TestLogin )

        login.login_button_click().enter_username(username).enter_password(password).confirm_login_button()
        logout=Logout(page)
        logout.logout_click()

