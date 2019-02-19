# -*- coding:utf-8 -*-
import allure
import pytest
from time import sleep
from absolute.actions.general_actions import GeneralActions
from absolute.elements.home_page_elements import HomePageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Verify active report')
@allure.story('Verify active report')
def test_active_report(setup, fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    home_element = HomePageElements(fixture_webdriver)
    general_action.click_on_button(home_element.find_device_btn())
    sleep(20)
