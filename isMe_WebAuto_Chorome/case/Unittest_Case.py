# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/3/26  13:28'
"""
1 Unittest 单元测试框架
2 case执行的顺序和字母和数字的升序排列 还有就是suite中可以顺序控制
3 跳过 @unittest.skip("不执行这条")

"""
import unittest
from selenium import webdriver
from isMe_WebAuto_Chorome.business.Login_Business import LoginBusiness


class First_Unittest_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这个是Case整体的测试开始")

    def setUp(self):
        print('这个是Case的前置条件')
        self.driver = webdriver.Chrome()
        self.driver.get('http://pc.350gtv-intranet.com/#/login')
        self.driver.maximize_window()
        self.Login_b = LoginBusiness(self.driver)

    def test_login01(self):
        print(".............这是第一条case,必须使用test开头的形式01..............")
        self.Login_b.login('dstest0001', 'aeuio888')
        time.sleep(2)
        self.Login_b.Login_success()
        time.sleep(2)

    # @unittest.skip("不执行这条")
    def test_login02(self):
        print(".............这是第一条case,必须使用test开头的形式01..............")
        self.Login_b.login('dstest0002333', 'aeuio888')
        time.sleep(2)
        self.Login_b.Login_success()
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
    suite.addTest(First_Unittest_Case("test_login02"))
    suite.addTest(First_Unittest_Case("test_login01"))
    unittest.TextTestRunner().run(suite)
