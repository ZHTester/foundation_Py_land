# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/29  16:16'
"""
操作Excle单元格
"""
import xlrd


class opearExcel:
    def __init__(self, excle_path=None, index=None):
        if excle_path is None:
            excle_path = '../config/casedata.xls'
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(excle_path)  # excle_data
        self.table = self.data.sheets()[index]  # excle_table
        self.rows = self.table.nrows  # 拿到行数

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)  # 拿出一列的数据
            result.append(col)
        return result


if __name__ == "__main__":
    o = opearExcel()
    print(o.get_data())
