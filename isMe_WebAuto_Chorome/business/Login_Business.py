# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/3/23  15:08'
"""
login-business层 用例组合层 也就是操作Handle层的关系  业务层

"""

from isMe_WebAuto_Chorome.handle.Login_Handle import LoginHandle
from isMe_WebAuto_Chorome.page.Login_page import LoginPage


class LoginBusiness:
    def __init__(self, driver):
        self.login_h = LoginHandle(driver)
        self.login_p = LoginPage(driver)

    # 操作层
    def login(self, username, password):
        self.login_h.Login_useName(username)
        self.login_h.Login_password(password)
        self.login_h.Login_button()

    def Login_success(self):
        ls = self.login_p.userName_sucess()
        return ls



