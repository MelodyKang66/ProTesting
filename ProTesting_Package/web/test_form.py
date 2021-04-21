#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        element = self.driver.find_element_by_css_selector('div[class*="custom-control custom-checkbox"]')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element_by_name('commit').click()
        sleep(3)