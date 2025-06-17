import pytest
import time
from pages.modal_dialogs import ModalDialogs

@pytest.fixture
def page(browser):
    modal_page = ModalDialogs(browser)
    modal_page.open()
    return modal_page

def test_modal_elements(browser, page):
    # Проверка количества кнопок
    buttons_count = page.get_buttons_count()
    assert buttons_count == 5, f"Ожидалось 5 кнопок, найдено {buttons_count}"

def test_navigation_modal(browser, page):
    # Обновляем страницу
    browser.refresh()

    # Переход на главную через иконку
    page.click_home_icon()

    # Шаг назад
    browser.back()

    # Установка размеров экрана 900x400
    browser.set_window_size(900, 400)

    # Шаг вперед
    browser.forward()

    # Проверка URL на главной странице
    current_url = browser.current_url
    assert "demoqa.com" in current_url, f"Текущий URL не содержит 'demoqa.com': {current_url}"

    # Проверка title
    title = browser.title
    assert "ToolsQA" in title, f"Заголовок страницы не содержит 'ToolsQA': {title}"

    # Восстановление размеров окна по умолчанию 1000x1000
    browser.set_window_size(1000, 1000)

