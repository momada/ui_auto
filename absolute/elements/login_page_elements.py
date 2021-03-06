class LoginPageElements:
    def __init__(self, drive):
        self.driver = drive

    def email_input(self):
        return self.driver.find_element_by_id('txtEmailAddress')

    def password_input(self):
        return self.driver.find_element_by_id('txtPassword')

    def sign_button(self):
        return self.driver.find_element_by_id('btnSignIn')

    def login_page_title(self):
        return self.driver.find_element_by_xpath('//*[@id="data-container"]/h2')

    def user_profile(self):
        return self.driver.find_element_by_xpath('//button[contains(@id,"user-profile")]')

    def logout_button(self):
        return self.driver.find_element_by_xpath('//li[@data-automation-id="dropdown-menu-item-logout"]')

    def email_label(self):
        return self.driver.find_element_by_id('lblEmailAddress')
    #
    # def login_input(self):
    #     return self.driver.find_element_by_id('sonik-username')
    #
    # def login_button(self):
    #     return self.driver.find_element_by_id('sonik-submit')
    #
    # def account_id(self):
    #     return self.driver.find_element_by_id('sonik-account')
    #
    # def signup_button(self):
    #     return self.driver.find_element_by_class_name('sonik-action-link')
    #
    # def use_automatic_button(self):
    #     return self.driver.find_element_by_id('use-manual')
    #
    # def text_block(self):
    #     return self.driver.find_element_by_xpath('//*[@id="data-container"]/p')
