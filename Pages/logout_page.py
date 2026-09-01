class Logout:
    def __init__(self,page):

        self.logoutbutton=page.locator("//a[text()='Log out']")

        #Login Page
    def logout_click(self):
        self.logoutbutton.click()