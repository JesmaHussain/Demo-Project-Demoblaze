class Homepage:
    def __init__(self,page):
        self.page=page

        self.productadd=page.locator("//a[text()='Samsung galaxy s6']")
        self.alert=page.on("dialog", lambda dialog: (print("Show message:", dialog.message), dialog.accept()))
        self.addcart=page.locator("//a[text()='Add to cart']")
        self.homebutton=page.locator("//a[@class='nav-link']").nth(0)
        self.selectphoneoption=page.get_by_text("Phones")
        self.selectphone=page.locator("//a[text()='Nexus 6']").nth(0)
        self.selectmonitoroption=page.locator("//a[text()='Monitors']")
        self.selectmonitor=page.locator("//a[text()='Apple monitor 24']")
        self.cartbutton=page.locator("//a[@class='nav-link']").nth(3)
        self.purchasebutton=page.get_by_role("button", name="Place Order")
        self.idname=page.locator("#name")
        self.country=page.locator("#country")
        self.city=page.locator("#city")
        self.card=page.locator("#card")
        self.month=page.locator("#month")
        self.year=page.locator("#year")
        self.purchasecomplete=page.get_by_text("Purchase")
        self.purchaseclose=page.locator("//button[@class='btn btn-secondary']").nth(2)
        self.okbutton=page.locator("//button[text()='OK']")

        #Login(same as Loginpagefunction)

        #product_addd_from home page.
    def product_add_to_cart(self):

        self.productadd.click()
        return self

    def add_cart(self):

        self.alert
        self.addcart.click()
        return self

        #return to home page
    def return_to_home_page(self):
        self.homebutton.click()
        return self


        #phones->cart
    def phone_add_to_cart(self):

        self.selectphoneoption.click()
        self.selectphone.click()
        return self

        
        #monitors->cart
    def monitor_add_to_cart(self):
        self.selectmonitoroption.click()
        self.selectmonitor.click()
        return self

        
        #cart button->click

    def cart_button_select(self):

        self.cartbutton.click()
        self.purchasebutton.click()
        self.idname.fill("jesma")
        self.country.fill("India")
        self.city.fill("TVM")
        self.card.fill("1344")
        self.month.fill("August")
        self.year.fill("2026")
        self.purchasecomplete.click()
        return self

    def ok_button_click(self):
        self.okbutton.click()
        return self
    def purchase_close(self):
        self.purchaseclose.click()
        return self
