import pytest
from playwright.sync_api import Page,expect
from Utilities.excel_read import NewExcelReader
from Pages.login_page import LoginPage
from Url.link import MAINLINK

class TestHome:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_home_function(self,page:Page):
        excel = NewExcelReader()
        username = excel.read_excel_cell(2, 1)
        password = str(excel.read_excel_cell(2, 2))
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")
        #print(page.url)
        #page.wait_for_timeout(6000)
        login=LoginPage(page)
        home=(login.login_button_click().enter_username(username).enter_password(password).confirm_login_button())
        expect(page.locator("//a[@id='nameofuser']")).to_be_visible()
        home.product_add_to_cart()
        expect(page).to_have_url("https://www.demoblaze.com/prod.html?idp_=1")
        home.add_cart().return_to_home_page()
        expect(page).to_have_url("https://www.demoblaze.com/index.html")

    def test_phone_cart_view(self,page:Page):
        page.goto(MAINLINK)
        excel = NewExcelReader()
        username = excel.read_excel_cell(2, 1)
        password = str(excel.read_excel_cell(2, 2))
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")
        login = LoginPage(page)
        home = (login.login_button_click().enter_username(username).enter_password(password).confirm_login_button())
        home.phone_add_to_cart()
        expect(page).to_have_url("https://www.demoblaze.com/prod.html?idp_=3")
        home.add_cart().return_to_home_page()
        expect(page.locator("//a[@id='nameofuser']")).to_have_text("Welcome jesma")


    def test_monitor_cart_view(self,page:Page):
        page.goto(MAINLINK)
        page.goto(MAINLINK)
        excel = NewExcelReader()
        username = excel.read_excel_cell(2, 1)
        password = str(excel.read_excel_cell(2, 2))
        page.goto(MAINLINK)
        page.wait_for_load_state("domcontentloaded")
        login = LoginPage(page)
        home = (login.login_button_click().enter_username(username).enter_password(password).confirm_login_button())
        home.monitor_add_to_cart()
        expect(page).to_have_url("https://www.demoblaze.com/prod.html?idp_=10")
        home.add_cart().cart_button_select()
        expect(page).to_have_url("https://www.demoblaze.com/cart.html")
        expect(page.get_by_text("Thank you for your purchase!")).to_be_visible()
        home.ok_button_click()











