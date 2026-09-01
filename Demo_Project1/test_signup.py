from Pages.signup_page import SignUpPage
from playwright.sync_api import Page,expect
import pytest
from Utilities.excel_read import NewExcelReader
from Url.link import MAINLINK
class TestSignup:
    @pytest.mark.smoke
    def test_signup_valid(self, page: Page):
        excel=NewExcelReader()
        username=excel.read_excel_cell(3,1)
        password=str(excel.read_excel_cell(3,2))
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")



        sign = SignUpPage(page)
        sign.perform_enter()

        sign.enter_username(username)

        sign.enter_password(password)

        message=sign.perform_signup()
        assert message =="This user already exist."
        #expect(page).
        sign.perform_close()
