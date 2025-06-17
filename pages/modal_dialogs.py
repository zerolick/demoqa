from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ModalDialogs(BasePage):
    URL = "https://demoqa.com/modal-dialogs"

    # Локатор для всех кнопок подменю
    BUTTONS = (By.CSS_SELECTOR, ".btn.btn-primary")

    # Локатор для иконки (например, для перехода на главную)
    HOME_ICON = (By.CSS_SELECTOR, "a[href='https://demoqa.com/']")

    def open(self):
        self.driver.get(self.URL)

    def get_buttons_count(self):
        return len(self.driver.find_elements(*self.BUTTONS))

    def click_home_icon(self):
        self.click(self.HOME_ICON)
