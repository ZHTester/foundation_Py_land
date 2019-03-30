# coding=utf-8
import ddt
import unittest
"""
数据驱动

"""


@ddt.ddt  # 这个就是数据驱动的表现方式
class DataCase(unittest.TestCase):

    def setUp(self):
        print('这个是setUp')

    @ddt.data(
        [1, 2],
        [3, 4],
        [5, 6]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a + b)

    def tearDown(self):
        print('这个是tearDown')
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()

