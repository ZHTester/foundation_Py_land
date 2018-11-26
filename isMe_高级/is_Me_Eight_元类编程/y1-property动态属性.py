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
        self._age = 0
    # def get_age(self):
    #     return datetime.now().year - self.birthday.year  # 返回当前时间点

    """
    1 这样的模式就是将取函数的模式变为取属性的模式了
    """
    @property
    def age(self):
        return datetime.now().year - self.birthday.year  # 返回当前时间点

    @age.setter
    def age(self,value):
        self._age = value


if __name__ == "__main__":
    user = User("landing", date(1988, 3, 1))
    user.age = 44
    # 这样也就是取属性的模式来进行调用函数
    print(user._age)  # 设置值
    print(user.age)  # 动态属性的值














