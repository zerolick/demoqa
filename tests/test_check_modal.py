import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

URL = "https://demoqa.com/modal-dialogs"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # или другой драйвер
    yield driver
    driver.quit()


def is_page_accessible(driver, url):
    try:
        driver.get(url)
        # Проверка, что страница загрузилась
        return True
    except WebDriverException:
        return False


def test_modal_dialogs(driver):
    if not is_page_accessible(driver, URL):
        pytest.skip("Страница недоступна, тест пропущен.")

    driver.get(URL)
    time.sleep(2)  # ожидание загрузки страницы

    try:
        small_button = driver.find_element(By.ID, "showSmallModal")
        large_button = driver.find_element(By.ID, "showLargeModal")
    except NoSuchElementException:
        pytest.fail("Кнопки модальных окон не найдены.")

    # Тест для Small modal
    small_button.click()
    time.sleep(1)
    small_modal = driver.find_element(By.CLASS_NAME, "modal-content")
    close_small = driver.find_element(By.ID, "closeSmallModal")
    assert small_modal.is_displayed()
    close_small.click()
    time.sleep(1)
    assert not small_modal.is_displayed()

    # Тест для Large modal
    large_button.click()
    time.sleep(1)
    large_modal = driver.find_element(By.CLASS_NAME, "modal-content")
    close_large = driver.find_element(By.ID, "closeLargeModal")
    assert large_modal.is_displayed()
    close_large.click()
    time.sleep(1)
    assert not large_modal.is_displayed()
