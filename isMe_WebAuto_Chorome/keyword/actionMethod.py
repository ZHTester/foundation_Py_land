# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/2  9:35'
"""
关键字驱动 = 关键字操作方法操作层

"""
from selenium import webdriver
from isMe_WebAuto_Chorome.base.find_Element import FindElement
import time


class ActionMethod:

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 放大窗口
    def windowsMax(self):
        self.driver.maximize_window()

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 截图
    def click_screenshot(self, name):
        self.driver.save_screenshot('../Image/{}.png'.format(name))

    # 判断是否封装投注方法
    def betFunction(self, key):
        if self.get_element(key) is self.driver.find_element_by_link_text('封盘中'):
            time.sleep(240)
        else:
            "未封盘"

    # 等待
    def sleep_time(self, times):
        time.sleep(times)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        title = self.driver.title
        return title



































