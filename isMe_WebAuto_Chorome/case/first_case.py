# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/23  14:28'
"""
Po 模型建立 case用例集合

"""
from isMe_WebAuto.business.Login_Business import LoginBusiness
from selenium import webdriver
import time


class FirstCase:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.Login_b = LoginBusiness(self.driver)
        ti = self.driver.title
        print(ti)

    def test_login_PassWord_error(self):
        """
        登录密码错误用例
        :return:
        """
        pass

    def test_login_UserName_error(self):
        """
        登录用户名错误用例
        :return:
        """
        pass

    def test_login_Success(self):
        """
        登录成功用例
        :return:
        """
        self.Login_b.login('dstest0001', 'aeuio888')
        time.sleep(2)
        self.Login_b.Login_success()
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    f = FirstCase("http://pc.350gtv-intranet.com/#/login")
    f.test_login_Success()









