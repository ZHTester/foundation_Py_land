# coding=utf-8
"""
1 __new__ && __init__的区别 ----高级python开发会经常问道这个问题
2 def __new__(cls, *args, **kwargs): 这个是在python2.2以后才有的版本，也就是新试类中才有，老版本的python是没有的。
  在这里面，我们可以再生成User这个对象之前加逻辑，其实这样的一个类就是用来描述类实例化的一个过程,这里面传递的是类cls
3 def __init__(self): 这里面传递的就是实例
4 这样的赋值方式 user = User(name='landing') 就会进入到__new__这个类初始化函数当中 kwargs-当中
5 这样的复制方式 user = User('landing') 就会进入到__new__当中 args当中

"""


class User:
    def __new__(cls, *args, **kwargs):
        print('in new ')

        return super().__new__(cls)

    def __init__(self, name):
        print('in init')
        self.name = name


# new是用来控制对象的生成过程，在对象生成之前
# init就是用来完善对象的属性
# 如果new方法不返回对象，则不会调用init函数


if __name__ == "__main__":
    user = User(name='landing')
    # user = User('landing')
    pass



















