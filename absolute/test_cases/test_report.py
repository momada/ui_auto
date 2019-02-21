# -*- coding:utf-8 -*-
import allure
import pytest
from time import sleep
from absolute.actions.general_actions import GeneralActions
from absolute.elements.home_page_elements import HomePageElements
from absolute.elements.report_page_elements import ReportPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Verify active report')
@allure.story('Verify active report')
def test_active_report(setup, fixture_webdriver):
    page = GeneralActions(fixture_webdriver)
    home_element = HomePageElements(fixture_webdriver)
    page.click_on_button(home_element.device_btn())
    # Verify report search box present
    page.check_element_on_page(ReportPageElements(fixture_webdriver).rpt_search_box())
    # Verify report name
    page.check_text_of_element(home_element.activedevice_title(), 'Active Devices')
    # Verify default filter"
    page.check_text_of_element(home_element.default_filter(), '"Agent Status" equal to "Active"')
    # Verify device details
    # Verify filter
    sleep(10)


def test_eventstore_report(setup, fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    home_element = HomePageElements(fixture_webdriver)
    general_action.click_on_button(home_element.device_btn())
    # Verify report name
    assert (home_element.activedevice_title().text, 'Active Devices')
    # Verify default filter"
    assert (home_element.default_filter().text, '"Agent Status" equal to "Active"')
    # Verify device details
    # Verify filter
    sleep(10)


def test_navigation_menu(setup, fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    home_element = HomePageElements(fixture_webdriver)
    general_action.click_on_button(home_element.device_btn())
    # Verify report name
    assert (home_element.activedevice_title().text, 'Active Devices')
    # Verify default filter"
    assert (home_element.default_filter().text, '"Agent Status" equal to "Active"')
    # Verify device details
    # Verify filter
    sleep(10)
