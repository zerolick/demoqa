import pytest
from pages.text_box import TextBox

@pytest.fixture
def page(browser):
    tb = TextBox(browser)
    tb.open()
    return tb

def test_text_box_submit(browser, page):
    # Переменные с текстом
    full_name_text = "Иван Иванов"
    current_address_text = "г. Москва, ул. Ленина, д. 1"

    # Заполнение полей
    page.fill_full_name(full_name_text)
    page.fill_current_address(current_address_text)

    # Нажатие на кнопку submit
    page.submit()

    # Проверка, что снизу появились элементы с нашим текстом
    assert page.get_output_full_name() == full_name_text, "Full Name не совпадает"
    assert page.get_output_current_address() == current_address_text, "Current Address не совпадает"
