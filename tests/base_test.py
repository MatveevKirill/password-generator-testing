import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from interface import implements

from ui.pages.web.main_page import MainPage

from core.interfaces import IBaseTest


class BaseTestCase(implements(IBaseTest)):
    driver: WebDriver = None
    configuration: dict = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request) -> None:
        self.driver = request.getfixturevalue('driver')
        self.configuration = request.getfixturevalue('configuration')

        self.main_page: MainPage = request.getfixturevalue('main_page')
