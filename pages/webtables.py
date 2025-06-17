# класс страницы с необходимыми методами
# pages/webtables.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WebTables(BasePage):
    URL = "https://demoqa.com/webtables"

    # Локаторы
    BUTTON_ADD = (By.ID, "addNewRecordButton")
    FORM_DIALOG = (By.CSS_SELECTOR, ".modal-content")
    FORM_FIELDS = {
        "first_name": (By.ID, "firstName"),
        "last_name": (By.ID, "lastName"),
        "email": (By.ID, "userEmail"),
        "age": (By.ID, "age"),
        "salary": (By.ID, "salary"),
        "department": (By.ID, "department")
    }
    BUTTON_SUBMIT = (By.ID, "submit")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
    # Внутри строки
    ROW_EDIT_BUTTON = (By.CSS_SELECTOR, ".action-buttons span[title='Edit']")
    ROW_DELETE_BUTTON = (By.CSS_SELECTOR, ".action-buttons span[title='Delete']")
    ROW = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
    # В диалоге редактирования
    DIALOG_INPUTS = {
        "first_name": (By.ID, "firstName"),
        "last_name": (By.ID, "lastName"),
        "email": (By.ID, "userEmail"),
        "age": (By.ID, "age"),
        "salary": (By.ID, "salary"),
        "department": (By.ID, "department")
    }
    # Кнопки навигации
    BUTTON_NEXT = (By.CSS_SELECTOR, ".-next")
    BUTTON_PREVIOUS = (By.CSS_SELECTOR, ".-prev")
    PAGE_INFO = (By.CSS_SELECTOR, ".-pageSize")
    PAGE_NUMBERS = (By.CSS_SELECTOR, ".-pageSize span")
    # Проверка disabled
    def is_button_disabled(self, button_locator):
        button = self.driver.find_element(*button_locator)
        return "disabled" in button.get_attribute("class") or not button.is_enabled()

    def open(self):
        self.driver.get(self.URL)

    def click_add(self):
        self.click(self.BUTTON_ADD)

    def is_dialog_open(self):
        return self.is_element_visible(self.FORM_DIALOG)

    def fill_form(self, data):
        for key, value in data.items():
            self.driver.find_element(*self.FORM_FIELDS[key]).clear()
            self.driver.find_element(*self.FORM_FIELDS[key]).send_keys(value)

    def submit_form(self):
        self.click(self.BUTTON_SUBMIT)

    def get_rows(self):
        return self.driver.find_elements(*self.TABLE_ROWS)

    def get_row_data(self, row_element):
        return [cell.text for cell in row_element.find_elements(By.CSS_SELECTOR, ".rt-td")]

    def click_edit_on_row(self, row_element):
        row_element.find_element(*self.ROW_EDIT_BUTTON).click()

    def click_delete_on_row(self, row_element):
        row_element.find_element(*self.ROW_DELETE_BUTTON).click()

    def delete_row(self, row_element):
        self.click_delete_on_row(row_element)

    def edit_row(self, row_element, new_data):
        self.click_edit_on_row(row_element)
        # Заполняем форму
        for key, value in new_data.items():
            self.driver.find_element(*self.DIALOG_INPUTS[key]).clear()
            self.driver.find_element(*self.DIALOG_INPUTS[key]).send_keys(value)
        self.submit_form()

    def add_new_record(self, data):
        self.click_add()
        # Ждем появления диалога
        self.is_element_visible(self.FORM_DIALOG)
        self.fill_form(data)
        self.submit_form()

    def get_pagination_info(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".-pageInfo").text

    def get_current_page_number(self):
        # Можно парсить из текста, например "1 of 2"
        info = self.get_pagination_info()
        # пример: "1 of 2"
        return int(info.split()[0])

    def click_next(self):
        self.click(self.BUTTON_NEXT)

    def click_previous(self):
        self.click(self.BUTTON_PREVIOUS)

    def is_next_disabled(self):
        return self.is_button_disabled(self.BUTTON_NEXT)

    def is_previous_disabled(self):
        return self.is_button_disabled(self.BUTTON_PREVIOUS)
