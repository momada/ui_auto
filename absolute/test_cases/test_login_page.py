import time

import allure
import pytest

from absolute.config import Param
from absolute.actions.general_actions import GeneralActions
from absolute.actions.login_actions import LoginActions
from absolute.elements.login_page_elements import LoginPageElements
from absolute.elements.main_page_elements import MainPageElements
from absolute.elements.users_page_elements import UsersPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check login page features')
@allure.story('Check elements')
def test_verify_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    lp_element = LoginPageElements(fixture_webdriver)
    general_action.open_page_by_url(Param.url())

    # check login elements
    general_action.check_element_on_page(lp_element.email_input())
    general_action.check_element_on_page(lp_element.sign_button())

#
# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Check login page features')
# @allure.story('Check Login page elements')
# def test_page_elements(fixture_webdriver):
#     general_action = GeneralActions(fixture_webdriver)
#     login_element = LoginPageElements(fixture_webdriver)
#     general_action.open_page_by_url(MainPageElements(fixture_webdriver).url() + '#login')
#     time.sleep(3)
#
#     general_action.check_element_on_page(login_element.login_page_title())
#     general_action.check_element_on_page(login_element.login_form())
#     general_action.check_element_on_page(login_element.account_id())
#     general_action.check_element_on_page(login_element.login_input())
#     general_action.check_element_on_page(login_element.login_button())
#     general_action.check_element_on_page(login_element.signup_button())
#     general_action.check_element_on_page(login_element.use_automatic_button())
#     general_action.check_element_on_page(login_element.text_block())
#
#
# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Check login page features')
# @allure.story('Login canceling')
# def test_cancel_login(fixture_webdriver):
#     LoginActions(fixture_webdriver).login_cancel('any@email.com')
#
#
@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check login page features')
@allure.story('Login on cc')
def test_login(fixture_webdriver):
    LoginActions(fixture_webdriver).login(Param.user_email(), Param.user_password())

