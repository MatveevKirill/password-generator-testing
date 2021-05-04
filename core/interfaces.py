import interface


class IBasePage(interface.Interface):

    def find_element(self, locator: tuple, timeout: float = None):
        """ Поиск элемента на странице. """
        raise NotImplementedError

    def find_elements(self, locator: tuple, by: str):
        """ Поиск нескольких элементов. """
        raise NotImplementedError

    def wait(self, timeout: float = None):
        """ Элемент WebDriverWait """
        raise NotImplementedError

    def send_keys(self, locator: tuple, value: str, timeout: float = None, autoclear: bool = True):
        """ Отправить значение в текстовое поле. """
        raise NotImplementedError

    def get_text_from_obj(self, locator: tuple, timeout: float = None):
        """ Получить текст из элемента. """
        raise NotImplementedError

    def get_selected_from_obj(self, locator: tuple, timeout: float = None):
        """ Получить значение is_selected() """
        raise NotImplementedError

    def click(self, locator: tuple, timeout: float = None):
        """ Нажать на элемент. """
        raise NotImplementedError


class IBaseTest(interface.Interface):

    def setup(self, request) -> None:
        """ Установить значения по умолчанию """
        raise NotImplementedError
