#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        clk = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        double_clk = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        right_clk = self.driver.find_element_by_xpath("/html/body/form/input[4]")

        action = ActionChains(self.driver)
        action.click(clk)
        action.double_click(double_clk)
        action.context_click(right_clk)
        sleep(3)
        action.perform()
        sleep(3)


    @pytest.mark.skip
    def test_move_mouse(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_id("s-usersetting-top")

        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[2]")

        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele,drop_ele).perform()
        # action.click_and_hold(drag_ele).release(drop_ele).perform()
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()

        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
