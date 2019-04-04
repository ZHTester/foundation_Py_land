# coding=utf-8
from isMe_WebAuto_Chorome.util.excel_util import ExcelUtil
from isMe_WebAuto_Chorome.util.read_ini import ReadIni

__author__ = 'landing'
__data__ = '2019/3/22  14:58'
"""
封装页面元素 - 通过配置文件的形式进行

"""


class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        global by, value
        handle_excel = ExcelUtil('../config/wordkey.xls')
        case_lines = handle_excel.get_lines()  # 拿到行数
        if case_lines:
            for i in range(1, case_lines):
                node = handle_excel.get_col_value(i, 10)
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
                elif by == 'linktext':
                    return self.driver.find_element_by_link_text(value)
                else:
                    return self.driver.find_element_by_class_name(value)
            except:
                    pass
        return None


if __name__ == "__name__":
    pass
