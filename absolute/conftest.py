import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from absolute.actions.login_actions import LoginActions
from simple_settings import settings


@pytest.yield_fixture(scope="function", autouse=True)
def fixture_webdriver() -> webdriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture()
def setup(fixture_webdriver):
    LoginActions(fixture_webdriver).login(settings.user, settings.password)
