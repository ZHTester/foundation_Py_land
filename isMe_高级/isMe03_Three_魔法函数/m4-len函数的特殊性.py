"""
len函数的特殊性


"""


class Company(object):
    def __init__(self, employ_list):
        self.employee = employ_list

    # def __getitem__(self, item):
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['tom', 'bob', 'jane'])

"""
1 调用len方法，Python会隐含的去调用__len__ 魔法函数的
2 len是在用Python内置函数的时候，那么len - len(set),len(list),len(dict)
  的效率是十分的高的，也就是说相当于会走一个捷径.因为 set或者说list或者说dict
  都是使用cpython来写的，也就是c语言，而c语言的效率是十分的高效的，当我们使用len(set
  list dict)的时候，cpython会直接去读取这样的数，不会直接去遍历这样的一个数据结构，所以说
  len在读取Python内置函数(原生函数)的时候效率是十分的高效的。


"""
a = len(company)
print(a)
