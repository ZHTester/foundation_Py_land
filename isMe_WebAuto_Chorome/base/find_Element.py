# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/22  14:58'
"""
封装页面元素 - 通过配置文件的形式进行

"""
from isMe_WebAuto_Chorome.util.read_ini import ReadIni


class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, node=None):
        read_ini = ReadIni(node)
        data = read_ini.get_value(key)
        by = data.split('>')[0]  # 定位方式
        value = data.split('>')[1]  # 定位值
        try:
            if by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            else:
                return self.driver.find_element_by_class_name(value)
        except:
            self.driver.save_screenshot('../Image/%s.png' % value)
            return None


if __name__ == "__name__":
    pass
