# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/25  14:12'
"""
页面元素封装层

"""
from isMe_WebAuto.base.find_Element import FindElement
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.findE = FindElement(driver)

    def userName_sucess(self):
        username = self.findE.get_element("username")
        return username

    def password_success(self):
        password = self.findE.get_element('password')
        return password

    def login_button(self):
        Lbutton = self.findE.get_element('button')
        return Lbutton


if __name__ == "__main__":
    driver = webdriver.Chrome()
    lo = LoginPage(driver)
    s = lo.userName_sucess()
