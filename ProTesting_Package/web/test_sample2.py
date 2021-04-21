from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/latest")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@id="ember37"]').click()

        # sleep(3)
        def wait(x):
            return len(self.driver.find_elements(By.LINK_TEXT, '职位内推')) >= 1

        WebDriverWait(self.driver, 10).until((wait))
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, '职位内推')))

        self.driver.find_element(By.LINK_TEXT, '职位内推').click()
        # print("hello")
