class SignUpPage:
    def __init__(self,page):
        self.page=page
        self.performsignin=page.locator("#signin2")
        self.usernamefield=page.locator("input[id='sign-username']")
        self.passwordfield=page.locator("input[id='sign-password']")
        self.signbuttonfield=page.get_by_text("Sign Up").nth(1)
        self.closebuttonfield=page.get_by_text("Close").nth(1)
        #self.popupalert=page.on("dialog", lambda dialog: print(("Alert message:", dialog.message), dialog.accept()))

    def perform_enter(self):
        self.performsignin.click()


    def enter_username(self,username):
        self.usernamefield.fill(username)


    def enter_password(self,password):
        self.passwordfield.fill(password)


    def perform_signup(self):
        #self.popupalert
        with self.page.expect_event("dialog") as dialog_info:
            self.signbuttonfield.click()
            dialog=dialog_info.value
            message=dialog.message
            dialog.accept()
            return message


    def perform_close(self):
        self.closebuttonfield.click()

