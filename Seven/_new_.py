"""
1 上述代码中，obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，
  Foo类本身也是一个对象，因为在Python中一切事物都是对象。 每个实例中肯定含有对象

2 创建类就可以有两种方式

3 类 是由 type 类实例化产生

------------------------
那么问题来了，类默认是由 type 类实例化产生，type类中如何实现的创建类？类又是如何创建对象？
答：类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，所以，我们可以为 __metaclass__
设置一个type类的派生类，从而查看 类 创建的过程
------------------------

"""


# 创建类的方式 普通方式

#
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#
# f = Foo('Mac GG')
# print(type(f))
# print(type(Foo))

# 特殊方式创建类


def func(self):
    print('hello %s age is %s', self.name)


def __init__(self, name, age):
    self.name = name
    self.age = age


Foo = type('Foo', (object,), {'func': func, '__init__': __init__})
f = Foo('Mac cheng ', 45)
f.func()
print(type(Foo))
