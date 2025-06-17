from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        """Переход на страницу по базовому URL"""
        self.driver.get(self.base_url)

    def find_element(self, locator):
        """Поиск элемента по локатору."""
        return self.driver.find_element(*locator)
