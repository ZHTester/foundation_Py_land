# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/15  10:40'
"""
1 实例化与实例化的意义在于哪里  ---  构造函数 
2 构造函数是自动进行的，不需要重复调用 
3 调用构造函数的返回结果是什么了 - 显式调用 对象.__init___ 默认返回的None-但是在实际项目中没有这样的调用方式 
4 __init__ 函数是不能返回除开none之外的任意的值的,这个就是Python中普通函数与构造函数的区别(这个要清楚) 
5 python函数中的None只能返回None之内的变量内省 
6 构造函数的作用就是让你的类生成不同的对象 初始化对象的属性 
7 
"""


class Student:
    #  构造函数
    """
    1 构造函数是自动进行的，当你在实例化的过程中，python就自动的调用了构造函数.
    2 构造函数就是初始化类的特征值 ，初始化对象的属性.
    3 python中构造函数中左边的值代表是定义的变量，右边的值代表是传入的参数.

    """
    # 构造函数的作用就是让你的类生成不同的对象 初始化对象的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('----student-----')

    def doHomework(self):
        print("做作业")

    def print_file(self):  # 打印档案
        print('name:' + str(self.name))
        print('age:' + str(self.age))


if __name__ == "__main__":
    student = Student('张三', 28)  # 这里就是需要通过构造函数来创建构造函数
    # print(Student.__init__())  # 显示调用就没有任何的数据，因为在init的函数中没有return中任何值
    print('---------------------------')
    print(student.name)
    print(student.age)
    print('---------------------------')
    student.print_file()

