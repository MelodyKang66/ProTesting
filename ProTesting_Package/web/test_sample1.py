from time import sleep

import selenium
from selenium import webdriver

class TestTesterhome():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardoen(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("https://testerhome.com/topics")
        # sleep(3)
        self.driver.find_element_by_link_text("社团").click()
        # sleep(3)
        self.driver.find_element_by_link_text("京东").click()
        # sleep(3)
        self.driver.find_element_by_css_selector(".topic-7908 .title > a").click()