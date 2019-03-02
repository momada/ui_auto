import time

from absolute.actions.general_actions import GeneralActions
from absolute.elements.login_page_elements import LoginPageElements
from simple_settings import settings


class LoginActions:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        login_elements = LoginPageElements(self.driver)
        general_action = GeneralActions(self.driver)
        general_action.open_page_by_url(settings.url)
        login_elements.email_input().send_keys(email)
        login_elements.sign_button().click()
        assert (login_elements.email_label(), email)
        login_elements.password_input().send_keys(password)
        login_elements.sign_button().click()
        time.sleep(3)

    def logout(self):
        assert (self.driver.title, 'Absolute')
        GeneralActions(self.driver).click_on_button(LoginPageElements(self.driver).user_profile())
        GeneralActions(self.driver).click_on_button(LoginPageElements(self.driver).logout_button())
        assert (self.driver.title, 'Absolute')

