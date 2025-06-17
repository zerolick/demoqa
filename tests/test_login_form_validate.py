import pytest
from pages.practice_form import PracticeForm

@pytest.fixture
def page(browser):
    form = PracticeForm(browser)
    form.open()
    return form

def test_placeholder_and_pattern(browser, page):

    assert page.get_placeholder_first_name() == "First Name"
    assert page.get_placeholder_last_name() == "Last Name"
    assert page.get_placeholder_email() == "name@example.com"

    # Проверка атрибута pattern у email
    pattern = page.get_pattern_email()
    assert pattern is not None
    assert "@" in pattern or pattern != "", "Атрибут pattern у email пустой или отсутствует"

    # Попытка отправить пустую форму
    page.submit()

    # Проверка наличия класса "was-validated"
    assert "was-validated" in page.get_form_classes(), "Класс 'was-validated' не добавился после отправки пустой формы"
