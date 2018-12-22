# coding=utf-8
"""
1 __new__ && __init__的区别 ----高级python开发会经常问道这个问题  --- 这个也是元类编程的一个核心点
2 def __new__(cls, *args, **kwargs): 这个是在python2.2以后才有的版本，也就是新试类中才有，老版本的python是没有的。
  在这里面，我们可以再生成User这个对象之前加逻辑，其实这样的一个类就是用来描述类实例化的一个过程.
  这里面传递的是(类)cls,而在__init__中所传递的是self，其中self也就是传入的是实例，其中new的时候是没有生成我们的对象的。


3 def __init__(self): 这里面传递的就是实例(对象)
4 这样的赋值方式 user = User(name='landing') 就会进入到__new__这个类初始化函数当中 kwargs-当中
5 这样的复制方式 user = User('landing') 就会进入到__new__当中 args当中


1.首先用法不同，__new__()用于创建实例，所以该方法是在实例创建之前被调用，它是类级别的方法，是个静态方法；
而 __init__() 用于初始化实例，所以该方法是在实例对象创建后被调用，它是实例级别的方法，用于设置对象属性的一些初始值。
由此可知，__new__()在__init__() 之前被调用。如果__new__() 创建的是当前类的实例，会自动调用__init__()函数，通过return调用的__new__()的参数cls来保证是当前类实例，如果是其他类的类名，
那么创建返回的是其他类实例，就不会调用当前类的__init__()函数。
　　2.其次传入参数不同
　　__new__()至少有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别；
　　__init__()至少有一个参数self，就是这个__new__()返回的实例，__init__()在__new__()的基础上完成一些初始化的操作。
　　3.返回值不同
　　__new__()必须有返回值，返回实例对象；
　　__init__()不需要返回值。
"""


class User:
    """
    1 new 是用来控制对象生成过程的，在对象生成之前 .....
    2 如果new方法不返回对象，则不会调用__init__函数
    """
    def __new__(cls, *args, **kwargs):
        print('in new ')
        return super().__new__(cls)

    def __init__(self, name):
        """
        init 是用来完善对象的属性操作
        :param name:
        """
        print('in init')
        self.name = name


# new是用来控制对象的生成过程，在对象生成之前
# init就是用来完善对象的属性
# 如果new方法不返回对象，则不会调用init函数


if __name__ == "__main__":
    user = User(name='landing')
    # user = User('landing')
    pass



















