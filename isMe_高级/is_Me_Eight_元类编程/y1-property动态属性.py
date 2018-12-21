# coding=utf-8
"""
property 动态属性

1 @property 将函数变为属性描述符  也就是可以将这样的取值方式理解成get方法
2 那么既然有了get方法自然就有set方法，
"""
from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        # self._age = 0
    # def get_age(self):
    #     return datetime.now().year - self.birthday.year  # 返回当前时间点

    """
    1 这样的模式就是将取函数的模式变为取属性的模式了
    2 这样也就是将age变为属性描述符了，这样我么在调用age函数的时候，就和调用属性一样的调用了。 
    3 动态属性获取自己的方法逻辑
    
    """
    @property
    def age(self):
        return datetime.now().year - self.birthday.year  # 返回当前时间点

    """
    1 这里添加了下划线，也就是属性描述符的性能或者方法名称来访问的一种形式
    2 动态属性设置 变量的值，通过属性方法来调度
    
    """
    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User("landing", date(year=1987, month=3, day=1))
    user.age = 44
    # 这样也就是取属性的模式来进行调用函数
    print(user._age)  # 设置值
    # print(user.age)  # 动态属性的值














