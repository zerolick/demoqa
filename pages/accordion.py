from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Accordion(BasePage):
    URL = "https://demoqa.com/accordian"

    # Локаторы для первого раздела
    SECTION1_CONTENT = (By.CSS_SELECTOR, "#section1Content > p")
    SECTION1_HEADER = (By.CSS_SELECTOR, "#section1Heading")

    # Локаторы для второго раздела
    SECTION2_CONTENT_P1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    SECTION2_CONTENT_P2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
    SECTION2_HEADER = (By.CSS_SELECTOR, "#section2Heading")

    # Локатор для третьего раздела
    SECTION3_CONTENT = (By.CSS_SELECTOR, "#section3Content > p")
    SECTION3_HEADER = (By.CSS_SELECTOR, "#section3Heading")

    def open(self):
        self.driver.get(self.URL)

    def is_section1_content_visible(self):
        return self.is_element_visible(self.SECTION1_CONTENT)

    def is_section2_content_p1_visible(self):
        return self.is_element_visible(self.SECTION2_CONTENT_P1)

    def is_section2_content_p2_visible(self):
        return self.is_element_visible(self.SECTION2_CONTENT_P2)

    def is_section3_content_visible(self):
        return self.is_element_visible(self.SECTION3_CONTENT)

    def click_section1_header(self):
        self.click(self.SECTION1_HEADER)

    def click_section2_header(self):
        self.click(self.SECTION2_HEADER)

    def click_section3_header(self):
        self.click(self.SECTION3_HEADER)

    def is_section1_content_not_visible(self):
        return not self.is_element_visible(self.SECTION1_CONTENT)

    def is_section2_content_p1_not_visible(self):
        return not self.is_element_visible(self.SECTION2_CONTENT_P1)

    def is_section2_content_p2_not_visible(self):
        return not self.is_element_visible(self.SECTION2_CONTENT_P2)

    def is_section3_content_not_visible(self):
        return not self.is_element_visible(self.SECTION3_CONTENT)

