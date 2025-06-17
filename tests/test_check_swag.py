import pytest
from pages.swag_labs import SwagLabs
from selenium.webdriver.common.by import By

@pytest.fixture
def open_page(driver):
    """Открывает страницу https://www.saucedemo.com/ и возвращает объект страницы."""
    driver.get("https://www.saucedemo.com/")
    return SwagLabs(driver)

def test_check_icon_exists(open_page):
    """Проверка наличия иконки логотипа."""
    assert open_page.exist_icon(), "Иконка логотипа не найдена"

def test_check_username_field_exists(open_page):
    """Проверка наличия поля имени пользователя."""
    try:
        element = open_page.find_element((By.ID, "user-name"))
    except:
        element = None
    assert element is not None, "Поле имени пользователя не найдено"

def test_check_password_field_exists(open_page):
    """Проверка наличия поля пароля."""
    try:
        element = open_page.find_element((By.ID, "password"))
    except:
        element = None
    assert element is not None, "Поле пароля не найдено"






