# тесты для автоматизации
# tests/test_webtables.py

import pytest
from pages.webtables import WebTables

@pytest.fixture
def page(browser):
    page = WebTables(browser)
    page.open()
    return page

def test_add_edit_delete_record(browser, page):
    # a. Проверка, что форма не сохраняется при пустых полях
    page.click_add()
    # Открыт диалог
    assert page.is_element_visible(page.FORM_DIALOG)
    # Попытка сохранить без заполнения
    page.submit_form()
    # Диалог остается открытым
    assert page.is_element_visible(page.FORM_DIALOG)

    # b. Заполняем все поля и добавляем
    new_data = {
        "first_name": "Петр",
        "last_name": "Петров",
        "email": "petrov@example.com",
        "age": "30",
        "salary": "50000",
        "department": "IT"
    }
    page.add_new_record(new_data)

    # c. Проверка, что запись добавилась
    rows = page.get_rows()
    found = False
    for row in rows:
        data = page.get_row_data(row)
        if data[0] == new_data["first_name"] and data[1] == new_data["last_name"]:
            found = True
            break
    assert found, "Новая запись не найдена в таблице"

    # d. Редактируем запись
    for row in rows:
        data = page.get_row_data(row)
        if data[0] == new_data["first_name"]:
            # Открываем редактирование
            page.edit_row(row, {
                "first_name": "Петр",
                "last_name": "Петров-редакт",
                "email": "petrov_new@example.com",
                "age": "31",
                "salary": "55000",
                "department": "HR"
            })
            break
    # Проверка обновления
    updated = False
    for row in page.get_rows():
        data = page.get_row_data(row)
        if data[1] == "Петров-редакт":
            updated = True
            break
    assert updated, "Редактирование не прошло успешно"

    # e. Удаляем запись
    for row in page.get_rows():
        data = page.get_row_data(row)
        if data[0] == "Петр":
            page.delete_row(row)
            break
    # Проверка удаления
    rows_after = page.get_rows()
    for row in rows_after:
        data = page.get_row_data(row)
        assert data[0] != "Петр", "Запись не удалена"

def test_pagination_controls_disabled_and_navigation(browser, page):
    # a. Проверка, что при открытии 5 строк, Next и Previous заблокированы
    # Предположим, что по умолчанию 5 строк
    rows = page.get_rows()
    assert len(rows) >= 5, f"Ожидалось минимум 5 строк, найдено {len(rows)}"

    assert page.is_previous_disabled(), "Кнопка Previous не заблокирована по умолчанию"
    assert page.is_next_disabled(), "Кнопка Next не заблокирована по умолчанию"

    # b. Добавим еще 3 записи, чтобы было 8 (предположим, что страница показывает 5)
    for i in range(3):
        data = {
            "first_name": f"Test{i}",
            "last_name": f"User{i}",
            "email": f"test{i}@example.com",
            "age": "25",
            "salary": "40000",
            "department": "QA"
        }
        page.add_new_record(data)

    # Проверка, что появилась вторая страница
    page_info = page.get_pagination_info()
    assert "2 of" in page_info, f"Нет второй страницы: {page_info}"

    # Проверка, что кнопка Next стала доступной
    assert not page.is_next_disabled(), "Кнопка Next должна быть активной"

    # Клик по Next
    page.click_next()
    # Проверка, что перешли на 2-ю страницу
    current_page = page.get_current_page_number()
    assert current_page == 2, f"Ожидалась страница 2, получена {current_page}"

    # Клик по Previous
    page.click_previous()
    current_page = page.get_current_page_number()
    assert current_page == 1, f"Ожидалась страница 1, получена {current_page}"
