# -*- coding:utf-8 -*-
import allure
import pytest
from time import sleep
from absolute.actions.general_actions import GeneralActions
from absolute.elements.home_page_elements import HomePageElements
from absolute.elements.report_page_elements import ReportPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.allure.feature('Verify active report')
@pytest.allure.story('Verify active report')
def test_active_report(setup, fixture_webdriver):
    page = GeneralActions(fixture_webdriver)
    home = HomePageElements(fixture_webdriver)
    report = ReportPageElements(fixture_webdriver)
    page.click_on_button(home.device_btn())
    # Verify report search box present
    page.check_element_on_page(report.rpt_search_box())
    # Verify report name
    page.check_text_of_element(report.activedevice_title(), 'Active Devices')
    # Verify default filter"
    page.check_text_of_element(report.default_filter(), '"Agent Status" equal to "Active"')
    # Verify device details
    # Verify filter
    sleep(3)


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.feature('Verify event store report')
@pytest.allure.story('Verify event store report')
def test_eventstore_report(setup, fixture_webdriver):
    page = GeneralActions(fixture_webdriver)
    home = HomePageElements(fixture_webdriver)
    report = ReportPageElements(fixture_webdriver)
    page.click_on_button(home.device_btn())
    # Verify report name
    page.check_text_of_element(report.activedevice_title(), 'Active Devices')
    # Nav to event store report
    page.click_on_button(report.eventstore_btn())
    page.check_text_of_element(report.eventstore_title(), '''Event Store
History of events supported by all Absolute services.
Report Options''')
    sleep(3)


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.feature('Verify nav menu')
@allure.story('Verify nav menu')
def test_navigation_menu(setup, fixture_webdriver):
    page = GeneralActions(fixture_webdriver)
    home = HomePageElements(fixture_webdriver)
    # Verify find device in navigation menu
    page.check_element_on_page(home.device_btn())
    # Verify device management in navigation menu
    page.check_element_on_page(home.device_mgn_btn())
    # Verify device protection in navigation menu
    page.check_element_on_page(home.device_protection_btn())
    # Verify find device policy in navigation menu
    page.check_element_on_page(home.device_policy_btn())
    # Verify find application persistent in navigation menu
    page.check_element_on_page(home.device_app_btn())
    # Verify find administration in navigation menu
    page.check_element_on_page(home.device_admin_btn())
    sleep(3)
