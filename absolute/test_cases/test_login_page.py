# -*- coding:utf-8 -*-
import allure
import pytest
from time import sleep
from simple_settings import settings
from absolute.actions.general_actions import GeneralActions
from absolute.actions.login_actions import LoginActions
from absolute.elements.login_page_elements import LoginPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check login page features')
@allure.story('Check elements')
def test_login_page(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    lp_element = LoginPageElements(fixture_webdriver)
    print (settings.url)
    general_action.open_page_by_url(settings.url)
    # check login elements
    general_action.check_element_on_page(lp_element.email_input())
    general_action.check_element_on_page(lp_element.sign_button())
    sleep(3)


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check login page features')
@allure.story('Login on cc')
def test_login(fixture_webdriver):
    LoginActions(fixture_webdriver).login(settings.user, settings.password)
    LoginActions(fixture_webdriver).logout()
    sleep(5)
