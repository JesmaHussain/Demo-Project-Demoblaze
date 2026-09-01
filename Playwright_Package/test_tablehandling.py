from playwright.sync_api import Page
import time
class Testtable:
    def test_table(self,page:Page):
        page.goto("https://selenium.qabible.in/table-pagination.php")
        time.sleep(2)
        #print(page.locator("//table[@id='dtBasicExample']/thead").text_content())
        #print(page.locator("//table[@id='dtBasicExample']/tbody").text_content())
        #print(page.locator("//table[@id='dtBasicExample']/tbody/tr[2]").text_content())
        #print(page.locator("//table[@id='dtBasicExample']/tbody/tr[5]/td[5]").text_content())
        #search=page.locator("//table[@id='dtBasicExample']/tbody/tr").nth(9)
        #print(search.text_content())
        names=page.locator("//table[@id='dtBasicExample']/tbody/tr/td[1]")
        print(names.all_text_contents())
        ages= page.locator("//table[@id='dtBasicExample']/tbody/tr/td[4]")
        print(ages.all_text_contents())

