class BaseComponent:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_text(self, locator):
        """Возвращает текст элемента по локатору."""
        return str(self.find_element(locator).text)
