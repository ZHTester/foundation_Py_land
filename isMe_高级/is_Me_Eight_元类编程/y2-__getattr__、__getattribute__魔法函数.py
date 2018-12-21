# coding=utf-8
"""
__getattr__、__getattribute__魔法函数    ----->
1 这两个魔法函数对属性操作十分重要的
2 这个也就是对属性进行操作的内置魔法函数
----------------

1 魔法函数这个本身就是解释器内部所需要用到的方法 -内部也就指的是python解释 是python动态的最根本原因
2 __getattr__、__getattribute__ 这两者的区别
3 __getattr__ 在查找不到属性的时候调用

4 __getattribute__ 相对于 __getattr__、 更加的高级  也就是使用 self.info = info，我们首先就会先去调用
  __getattribute__  也就是不是找不到属性才会进入这个魔法函数，而是他是无条件都会进入这样的一个函数
  也就是访问存在属性，或者是访问不存在属性，都是返回这个函数中的逻辑，也就是把持了所有这样的函数属性的访问入口了
5 也就是__getattr__ 是放在__getattribute__ 魔法函数中的，也就是__getattribute__能不重写就尽量不要去重写这个
  __getattribute__ 函数，当然我们是在写框架的时候回用到这样的一个函数的，因为在某个时候，我们回去控制实例的过程
  以及类实例属性访问的一个过程



"""
from datetime import date


# class User:
#     def __init__(self, name, birthday, info={}):
#         self.Name = name
#         self.birthday = birthday
#         self.info = info
#
#     """
#     找不到属性的时候，这个时候，我们就会自动的去调用这个 __getattr__ 函数
#     """
#
#     def __getattr__(self, item):
#         # return 'not find attr'
#         # return self.Name
#         return self.info[item]
#
#
# if __name__ == "__main__":
#     user = User("landing", date(1988, 3, 1), info={"commpany_info": "北京王道"})
#     """
#     这个age是找不到的 age  那么这个时候我们就需要使用
#     AttributeError: 'User' object has no attribute '_age'
#
#     """
#     # print(user.age)  # 动态属性的值
#     # print(user.name)
#     print(user.commpany_info)  # 动态属性的值


class User:
    def __init__(self, info={}):
        self.info = info

    """
    找不到属性的时候，这个时候，我们就会自动的去调用这个 __getattr__ 函数
    """

    def __getattr__(self, item):
        # return 'not find attr'
        return self.info[item]

    def __getattribute__(self, item):
        return "调用了__getattribute__"


if __name__ == "__main__":
    user = User(info={"commpany_info": "jidian","name":"landing"})
    """
    这个age是找不到的 age  那么这个时候我们就需要使用
    AttributeError: 'User' object has no attribute '_age'

    """
    # print(user.age)  # 动态属性的值
    print(user.commpany_info)  # 动态属性的值
    print(user.name)  # 动态属性的值

