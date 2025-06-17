import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demoqa.com/links"


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


def test_home_link_opens_new_tab(driver):
    if not is_page_accessible(driver, URL):
        pytest.skip("Страница недоступна, тест пропущен.")

    driver.get(URL)
    link = driver.find_element(By.LINK_TEXT, "Home")
    assert link.text == "Home"
    href = link.get_attribute("href")
    assert href == "https://demoqa.com"

    original_windows = driver.window_handles
    link.click()
    time.sleep(2)
    new_windows = driver.window_handles
    assert len(new_windows) > len(original_windows)

    # Переключение на новую вкладку
    driver.switch_to.window(new_windows[-1])
    assert driver.current_url == "https://demoqa.com"
    driver.close()
    driver.switch_to.window(original_windows[0])
