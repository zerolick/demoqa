import pytest
import time
from pages.accordion import Accordion

@pytest.fixture
def page(browser):
    acc = Accordion(browser)
    acc.open()
    return acc

def test_visible_accordion(browser, page):
    # Первый тест: проверка скрытого содержимого после открытия
    assert page.is_section1_content_visible(), "Content секции 1 не виден при загрузке"
    page.click_section1_header()
    time.sleep(2)
    assert page.is_section1_content_not_visible(), "Content секции 1 всё ещё виден после клика"

def test_visible_accordion_default(browser, page):
    # Второй тест: проверка, что разделы по умолчанию скрыты
    # Проверка скрытости элементов
    assert not page.is_section2_content_p1_visible(), "Параграф 1 секции 2 виден по умолчанию"
    assert not page.is_section2_content_p2_visible(), "Параграф 2 секции 2 виден по умолчанию"
    assert not page.is_section3_content_visible(), "Контент секции 3 виден по умолчанию"

