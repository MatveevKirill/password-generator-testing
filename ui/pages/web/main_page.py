from ui.pages.web.base_page import BasePage
from ui.locators.page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def generate_passwords(self, params: dict) -> None:

        # Установить значения чекбоксов.
        for element in ['usenums', 'usecaps', 'uselower', 'usesymbols']:

            if element in params:

                is_selected = self.get_selected_from_obj(locator=(self.locators.CHECKBOX_TEMPLATE[0],
                                                                  self.locators.CHECKBOX_TEMPLATE[1].format(element)))

                if params[element] != is_selected:
                    self.click(locator=(self.locators.CHECKBOX_TEMPLATE[0],
                                        self.locators.CHECKBOX_TEMPLATE[1].format(element)))

        # Установить длину пароля
        if 'len' not in params:
            self.send_keys(locator=self.locators.INPUT_VALUE, value='6')
        else:
            self.send_keys(locator=self.locators.INPUT_VALUE, value=params['len'])

        # Нажать на кнопку "Создать пароль".
        self.click(locator=self.locators.BUTTON_SUBMIT)

    def get_passwords(self):
        return [password.text for password in self.find_elements(locator=self.locators.LI_PASSWORDS, by="xpath")]
