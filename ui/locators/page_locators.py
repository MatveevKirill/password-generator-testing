from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CHECKBOX_TEMPLATE = (By.NAME, '{}')
    INPUT_VALUE = (By.NAME, 'value')
    BUTTON_SUBMIT = (By.XPATH, '//input[@value = "Создать пароль" and @type = "submit"]')
    LI_PASSWORDS = (By.XPATH, "//ul[@class='pas']/li")
