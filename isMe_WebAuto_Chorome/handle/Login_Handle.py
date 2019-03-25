# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/23  14:44'

from isMe_WebAuto_Chorome.page.Login_page import LoginPage
"""
1 操作层的意思就是说获取对应的元素的一个操作层

"""


class LoginHandle:
    def __init__(self, driver):
        self.driver = driver
        self.page_p = LoginPage(self.driver)

    def Login_password(self, password):
        self.page_p.password_success().send_keys(password)

    def Login_useName(self, username):
        self.page_p.userName_sucess().send_keys(username)

    def Login_button(self):
        self.page_p.login_button().click()


if __name__ == "__main__":
    pass



























