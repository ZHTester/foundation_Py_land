# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/21  15:21'
"""
读取配置文件操作方法 
读取ini的文件的方法 

"""
import configparser


class ReadIni:
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = '../config/LocalElement.ini'
        if node is None:
            self.node = 'userElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf  # 返回文件ini文件对象

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    r = ReadIni()
    print(r.get_value('username'))



