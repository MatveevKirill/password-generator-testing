import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from ui.pages.web.main_page import MainPage


@pytest.fixture(scope="function")
def main_page(driver: WebDriver, configuration: dict) -> MainPage:
    return MainPage(driver=driver, configuration=configuration)


@pytest.fixture(scope="session")
def browser_options() -> webdriver.ChromeOptions:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("ignore-certificate-errors")
    return chrome_options


@pytest.fixture(scope="function")
def driver(browser_options: webdriver.ChromeOptions) -> WebDriver:
    manager = ChromeDriverManager(version="latest", log_level=0)
    driver = webdriver.Chrome(executable_path=manager.install(), options=browser_options)
    driver.get('http://www.onlinepasswordgenerator.ru/')
    yield driver
    driver.quit()
