# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/21  11:06'
"""
配置文件读取定位元素信息

"""
from selenium import webdriver
from isMe_WebAuto_Chorome.function_selenium.find_Element import FindElement


class funcitonstart:
    def __init__(self, url):
        self.driver = self.get_driver(url)  # 设置公共变量driver

    def get_driver(self,url):
        driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    def get_user_element(self, key):
        f = FindElement(self.driver)
        user_Element = f.get_element(key)
        return user_Element

    def user_send_key(self, key, data):
        self.get_user_element(key).send_keys(data)

    def user_click(self, key):
        self.get_user_element(key).click()


if __name__ == "__main__":
    fun = funcitonstart("http://pc.350gtv-intranet.com/#/login")
    fun.user_send_key('username', 'dstest0001')
    fun.user_send_key('password', 'aeuio888')
    fun.user_click('button')











