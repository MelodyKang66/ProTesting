#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        input_ele = self.driver.find_element_by_name("wd")
        search_ele = self.driver.find_element_by_id("su")

        input_ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(search_ele)
        action.perform()
        sleep(3)

        action.scroll_from_element(input_ele,0,10000).perform()
        sleep(3)