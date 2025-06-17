import pytest
from pages.practice_form import PracticeForm

@pytest.fixture
def page(browser):
    form = PracticeForm(browser)
    form.open()
    return form

def test_fill_state_and_city(browser, page):
    # Заполнение поля State
    page.fill_state("Москва")
    # Заполнение поля City
    page.fill_city("Москва")
    # Проверка, что поля заполнены
    assert page.get_value_state() == "Москва"
    assert page.get_value_city() == "Москва"
