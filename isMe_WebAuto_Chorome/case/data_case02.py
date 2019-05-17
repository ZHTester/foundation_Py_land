# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/29  15:11'

import time
from selenium import webdriver
import HTMLTestReportCN
from isMe_WebAuto.business.Login_Business import LoginBusiness
from isMe_WebAuto.util.excel_util import opearExcel
import ddt
import unittest


@ddt.ddt  # Business
class DataCase(unittest.TestCase):

    def setUp(self):
        print('这个是setUp')
        self.excle = opearExcel()
        self.driver = webdriver.Chrome()
        self.driver.get('http://pc.350gtv-intranet.com/#/login')
        self.driver.maximize_window()
        self.Login_b = LoginBusiness(self.driver)

    # 用户名 密码
    @ddt.data(
        ['dstest0001', 'aeuio888'],
        ['dstest0002', 'aeuio88'],
        ['dstest0003', 'aeuio888'],
        ['dstest0004', 'aeuio88'],
        ['dstest0005', 'aeuio888'],
        ['dstest0006', 'aeuio888']
    )
    @ddt.unpack
    def test_add(self, username, password):
        self.Login_b.login(username, password)
        time.sleep(2)
        lss = self.Login_b.Login_success()
        self.assertEqual(None, lss, msg="登录失败")
        time.sleep(2)
        self.driver.quit()

    def tearDown(self):
        print('这个是tearDown')
        self.driver.quit()


if __name__ == "__main__":
    suite_path = '../report/数据驱动自动化测试报告.html'  # 获取到当前工程路径
    print(suite_path)
    f = open(suite_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(DataCase)  # 载入整个测试用例集合
    runner = HTMLTestReportCN.HTMLTestRunner(stream=f, title='UIReport', description="这是我们第一次的测试报告1", verbosity=2)
    runner.run(suite)

