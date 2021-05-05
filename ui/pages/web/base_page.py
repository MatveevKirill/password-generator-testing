from interface import implements
from selenium.common import exceptions as E
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


from core.interfaces import IBasePage
from core.exceptions import NotAllowedByTypeException

from utils.decoders import wait


class BasePage(implements(IBasePage)):
    driver: WebDriver = None
    configuration: dict = None

    def __init__(self, driver: WebDriver, configuration: dict) -> None:
        self.driver = driver
        self.configuration = configuration

    def wait(self, timeout: float = None):
        if timeout is None:
            timeout = self.configuration['timeout']

        return WebDriverWait(self.driver, timeout=timeout)

    def send_keys(self, locator: tuple, value: str, timeout: float = None, autoclear: bool = True):
        def _send_keys():
            element = self.find_element(locator=locator, timeout=timeout)
            if autoclear:
                element.clear()
            element.send_keys(value)

        return wait(
            _method=_send_keys,
            _error=E.TimeoutException,
            _timeout=self.configuration['timeout']
        )

    def find_element(self, locator: tuple, timeout: float = None):
        return self.wait(timeout=timeout).until(EC.presence_of_element_located(locator=locator))

    def find_elements(self, locator: tuple, by: str):
        if by == "xpath":
            return self.driver.find_elements_by_xpath(locator[1])
        else:
            raise NotAllowedByTypeException(f'By type "{by}" not allowed.')

    def get_text_from_obj(self, locator: tuple, timeout: float = None):
        def _text():
            return self.find_element(locator=locator).text

        return wait(
            _method=_text,
            _timeout=self.configuration['timeout'],
            _error=E.TimeoutException
        )

    def get_selected_from_obj(self, locator: tuple, timeout: float = None):
        def _is_selected():
            return self.find_element(locator=locator, timeout=timeout).is_selected()

        return wait(
            _method=_is_selected,
            _error=E.TimeoutException,
            _timeout=self.configuration['timeout']
        )

    def click(self, locator: tuple, timeout: float = None):
        def _click():
            self.find_element(locator=locator, timeout=timeout).click()

        return wait(
            _method=_click,
            _error=E.TimeoutException,
            _timeout=self.configuration['timeout']
        )
