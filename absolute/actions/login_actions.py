import time

from absolute.actions.general_actions import GeneralActions
from absolute.elements.login_page_elements import LoginPageElements
from absolute.elements.main_page_elements import MainPageElements
from absolute.elements.welcome_page_elements import WelcomePageElements
from absolute.config import Param


class LoginActions:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        # main_elements = MainPageElements(self.driver)
        login_elements = LoginPageElements(self.driver)
        general_action = GeneralActions(self.driver)
        general_action.open_page_by_url(Param.url())
        login_elements.email_input().send_keys(email)
        login_elements.sign_button().click()
        assert (login_elements.email_label(), email)
        login_elements.password_input().send_keys(password)
        login_elements.sign_button().click()
        time.sleep(3)

    def logout(self):
        GeneralActions(self.driver).click_on_button(WelcomePageElements(self.driver).logout_button())
