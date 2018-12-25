# coding=utf-8
"""
属性描述符和属性查找过程

如果说User是一张表，那么字段我们有时候需要去判断他的字符串类型

"""
import numbers
from datetime import date, datetime

"""
这个类如何变为属性描述符
1 类实现了get set 或者说是delete (魔法函数)方法 我们只需要实现这三个魔法函数中的任意一个
属性描述描述符，但是属性描述符能做什么了，他可以将逻辑拿来检查。
    def __get__(self, instance, owner):
    def __set__(self, instance, value):
    def __delete__(self, instance):
2 所以我们通过属性描述符，就能控制我们对属性赋值的一种行为。
"""


# 这里面就需要统一去判断Int类型的字段 而这样的类实际上就是属性描述符
class IntFeild:
    def __get__(self, instance, owner):
        pass
        return self.value

    """
    这里的对象就是User对象
    value就是我们设置的30 
    """

    def __set__(self, instance, value):
        # 这里就需要对传入的值进行一个判断了，进行属性描述符的控制了
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need ")

        if value < 0:
            raise ValueError("你的值需要大于0")
        self.value = value

    def __delete__(self, instance):
        pass


class User:
    """
    这个age 就不输入User中的变量类型了
    IntFeild() 传递给这个 age ---->对象 age这个属性是属于User这个类的，
    而不是属于
        def __init__(self, name, email, birthday):
        self.name = name
        self.birthday = birthday
        self.email = email
        self._age = 0
        这个实例的
    """
    age = IntFeild()  # 所以说这个age就是属性描述符的对象


# class User:
#     def __init__(self, name, email, birthday):
#         self.name = name
#         self.birthday = birthday
#         self.email = email
#         self._age = 0
#
#     # def get_age(self):
#     #     return datetime.now().year - self.birthday.year  # 返回当前时间点
#
#     """
#     1 这样的模式就是将取函数的模式变为取属性的模式了
#     2 检查这个age是否是字符串类型 - property 属性描述符
#     """
#
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year  # 返回当前时间点
#
#     @age.setter
#     def age(self, value):
#         # 检查是不是字符串类型
#         self._age = value


if __name__ == "__main__":
    user = User()
    user.age = -8  # 这样赋值的时候，实际上是会调用属性描述符中的set方法
    pass
    # user = User("landing", date(1988, 3, 1))
    # user.age = 44
    # # 这样也就是取属性的模式来进行调用函数
    # print(user._age)  # 设置值
    print(user.age)  # 动态属性的值
