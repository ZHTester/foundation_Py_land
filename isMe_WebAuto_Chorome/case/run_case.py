# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/26  15:51'
"""
统一调度Unittest 中测试用例 


"""
import unittest
import os


class RunCase(unittest.TestCase):

    def test_case01(self):
        case_path = os.path.join(os.getcwd())
        suite = unittest.defaultTestLoader.discover(case_path, 'Unittest_*.py')  # 运行其他的py文件
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()


















