"""
用python定义类

python有老式类
python新式类

如果一个类没有继承其他的类，那么最好就是继承objcet

"""


# class ClassName(object):
#     """
#     对类的属性和方法进行设置
#     1 构造函数就是对类的属性与方法进行设置的也就是类的初始化
#     """
#     def __init__(self):
#         pass
#     """
#     类的相关对于的方法
#     """
#     pass
#     """
#     析构函数，也就是在销毁函数中所使用的函数
#     1 python的垃圾回收机制中，那么就会来调用这个析构函数
#     2 是和垃圾回收有关系的，但是和python的内建函数是没有关系的
#     """
#     def __del__(self):
#         pass
class OldStyle:
    def __init__(self,name,description):
        self.name = name
        self.description = description


class NewStyle(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description


if __name__ == '__main__':
    old = OldStyle('old', 'Old style class')
    print(old)
    print(type(old))
    print(dir(old))
    print('-------------------')
    new = NewStyle('new','new style class')
    print(new)
    print(type(new))
    print(dir(new))  # 新式类继承了object那么新式类就存在了比老式类更多的方法，由于存在这些方法，就代码了新式类比老式类有更加强大的功能


































