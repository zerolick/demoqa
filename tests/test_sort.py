import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demoqa.com/webtables"


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


def test_table_sorting(driver):
    if not is_page_accessible(driver, URL):
        pytest.skip("Страница недоступна, тест пропущен.")

    driver.get(URL)
    headers = driver.find_elements(By.CSS_SELECTOR, ".rt-th")
    for header in headers:
        header.click()
        time.sleep(1)  # ожидание сортировки
        class_attr = header.get_attribute("class")
        assert "sort" in class_attr or "asc" in class_attr or "desc" in class_attr
