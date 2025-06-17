import pytest
from selenium.webdriver.common.by import By

def test_footer_text(driver):
    """Проверка текста в подвале страницы."""
    driver.get('https://demoqa.com/')
    footer_locator = (By.CSS_SELECTOR, 'footer')
    footer_element = driver.find_element(*footer_locator)
    footer_text = footer_element.text
    assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', \
        f"Текст в подвале не совпадает. Получено: '{footer_text}'"

def test_center_text_after_navigation(driver):
    """Проверка текста по центру после навигации."""
    driver.get('https://demoqa.com/')
    # Нажимаем кнопку или ссылку для перехода на страницу 'Elements'
    # Предположим, что есть кнопка или ссылка с текстом 'Elements'
    # Или используем конкретный локатор
    elements_button_locator = (By.CSS_SELECTOR, 'div.card-body h5')
    from selenium.webdriver.common.action_chains import ActionChains

    # Найти кнопку по тексту
    element_cards = driver.find_elements(By.CSS_SELECTOR, 'div.card')
    for card in element_cards:
        if 'Elements' in card.text:
            card.click()
            break

    # Проверка, что перешли на нужную страницу
    assert 'elements' in driver.current_url

    # Проверка текста по центру
    center_text_locator = (By.CSS_SELECTOR, 'div.main-header')
    element = driver.find_element(*center_text_locator)
    text = element.text
    assert text == 'Please select an item from left to start practice.', \
        f"Текст по центру не совпадает. Получено: '{text}'"
