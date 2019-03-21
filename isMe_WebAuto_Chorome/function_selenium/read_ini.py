# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/21  15:21'
"""
读取配置文件操作方法 
读取ini的文件的方法 

"""
import configparser


class ReadIni:
    def __init__(self, file_name=None, nond=None):
        if file_name is None:
            file_name = self.load_ini('..\com_WebAuto\config\LocalElement.ini')
        if nond is None:
            self.nond = 'userElement'
        else:
            self.nond = nond
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf  # 返回文件ini文件对象

    def get_value(self):
        data = self.cf.get(self.nond, 'username')
        return data


if __name__ == '__main__':
    r = ReadIni()
    print(r.get_value())



