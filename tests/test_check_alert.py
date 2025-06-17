import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://demoqa.com/alerts"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def is_page_accessible(driver, url):
    try:
        driver.get(url)
        return True
    except WebDriverException:
        return False


def test_timer_alert(driver):
    if not is_page_accessible(driver, URL):
        pytest.skip("Страница недоступна, тест пропущен.")

    driver.get(URL)
    button = driver.find_element(By.ID, "timerAlertButton")
    button.click()
    # Ждем до 6 секунд, чтобы убедиться, что алерт появился
    WebDriverWait(driver, 6).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text is not None
    alert.accept()
