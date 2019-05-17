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
from isMe_WebAuto.business.Login_Business import LoginBusiness
import HTMLTestReportCN
import os


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
        lss = self.Login_b.Login_success()
        self.assertEqual(None, lss, msg="登录失败")
        time.sleep(2)

    # @unittest.skip("不执行这条")
    def test_login02(self):
        print(".............这是第一条case,必须使用test开头的形式01..............")
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
    # suite_path = os.path.join(os.getcwd() + "\\report" + "\\UI.html")  # 获取到当前工程路径
    suite_path = '../report/UI自动化测试结果报告.html'  # 获取到当前工程路径
    print(suite_path)
    f = open(suite_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(First_Unittest_Case("test_login02"))
    suite.addTest(First_Unittest_Case("test_login01"))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestReportCN.HTMLTestRunner(stream=f, title='UIReport', description="这是我们第一次的测试报告", verbosity=2)
    runner.run(suite)
