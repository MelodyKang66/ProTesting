# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLogin():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_shelve(self):
        cookies = self.driver.get_cookies()
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, '.').click()


    # def test_cookies(self):
    #     cookies = self.driver.get_cookies()
    #     # print(cookies)
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
    #     sleep(3)

    # def test_login(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
    #     sleep(3)
