from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SwagLabs(BasePage):
    def exist_icon(self):
        """Проверяет наличие элемента с логотипом"""
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True
