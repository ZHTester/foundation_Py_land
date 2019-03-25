# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/3/21  11:06'
"""
配置文件读取定位元素信息

"""
from selenium import webdriver
from isMe_WebAuto_Chorome.base.find_Element import FindElement


class funcitonstart:
    def __init__(self, url, ite):
        self.driver = self.get_driver(url, ite)  # 设置公共变量driver

    def get_driver(self, url, ite):
        if ite is 1:
            driver = webdriver.Edge()
        elif ite is 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        return driver

    def get_user_element(self, key):
        f = FindElement(self.driver)
        user_Element = f.get_element(key)
        return user_Element

    def user_send_key(self, key, data):
        self.get_user_element(key).send_keys(data)

    def user_click(self, key):
        self.get_user_element(key).click()

    def run_main(self):
        self.user_send_key('username', 'dstest0001')
        self.user_send_key('password', 'aeuio888')
        self.user_click('button')
        usercode = self.get_user_element('button')
        time.sleep(5)
        if usercode is None:
            print('登录成功')
        else:
            self.driver.save_screenshot('../Image/codeError.png')
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    for ite in range(4):
        fun = funcitonstart("http://pc.350gtv-intranet.com/#/login", ite)
        fun.run_main()
