class LoginPage:
    def __init__(self,page):
        self.page=page
        self.loginbutton=page.locator("#login2")
        self.usernamefield=page.locator("input[id='loginusername']")
        self.passwordfield=page.locator("input[id='loginpassword']")
        self.loginbutton2=page.get_by_text("Log in").nth(1)
        self.closebutton=page.get_by_text("Close").nth(2)
        self.popup=page.on("dialog", lambda dialog: print(("Alert message:", dialog.message), dialog.accept()))
        self.logoutbutton=page.locator("//a[text()='Log out']")
    def login_button_click(self):
        self.loginbutton.click()
        return self

    def enter_username(self,username):
        self.usernamefield.fill(username)
        return self

    def enter_password(self,password):
        self.passwordfield.fill(password)
        return self

    def with_alert(self):
        self.popup
        self.loginbutton2.click()
        self.closebutton.click()
        return self

    def confirm_login_button(self):

        self.loginbutton2.click()
        from Pages.home_page import Homepage
        return Homepage(self.page)



