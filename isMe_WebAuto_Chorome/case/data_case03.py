# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/29  17:11'
import time
from selenium import webdriver
import HTMLTestReportCN
from isMe_WebAuto_Chorome.business.Login_Business import LoginBusiness
from isMe_WebAuto_Chorome.util.excel_util import opearExcel
import ddt
import unittest

ex = opearExcel()
data = ex.get_data() # 拿到所有的数据


@ddt.ddt
class DataCase(unittest.TestCase):

    def setUp(self):
        print('这个是setUp')
        self.driver = webdriver.Chrome()
        self.driver.get('http://pc.350gtv-intranet.com/#/login')
        self.driver.maximize_window()
        self.Login_b = LoginBusiness(self.driver)

    @ddt.data(*data)
    def test_add(self, data_excl):
        username, password = data_excl
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