import pytest
from selenium import webdriver

from absolute.elements.main_page_elements import MainPageElements


@pytest.fixture
def fixture_webdriver() -> webdriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
