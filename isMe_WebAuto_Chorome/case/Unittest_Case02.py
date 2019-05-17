# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/3/26  14:57'
"""
多个case文件执行

"""
import unittest
from selenium import webdriver
from isMe_WebAuto.business.Login_Business import LoginBusiness


class First_Unittest_Case02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这个是Case整体的测试开始")

    def setUp(self):
        print('这个是Case的前置条件02')
        self.driver = webdriver.Chrome()
        self.driver.get('http://pc.350gtv-intranet.com/#/login')
        self.driver.maximize_window()
        self.Login_b = LoginBusiness(self.driver)

    def test_login01(self):
        print(".............这是第一条case,必须使用test开头的形式02..............")
        self.Login_b.login('dstest0001', 'aeuio888')
        time.sleep(2)
        lss = self.Login_b.Login_success()
        self.assertEqual(None, lss, msg="登录失败")
        time.sleep(2)

    # @unittest.skip("不执行这条")
    def test_login02(self):
        print(".............这是第一条case,必须使用test开头的形式..............")
        self.Login_b.login('dstest0002333', 'aeuio888')
        time.sleep(2)
        lss = self.Login_b.Login_success()
        self.assertEqual(None, lss, msg="登录失败")
        time.sleep(2)

    def tearDown(self):
        print('这个是Case的后置条件')
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print('这个是Case整体的测试结束')


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(First_Unittest_Case02("test_login02"))
    suite.addTest(First_Unittest_Case02("test_login01"))
    unittest.TextTestRunner().run(suite)

