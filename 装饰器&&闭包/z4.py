"""
基于类实现的函数调用

像__call__这样前后都带下划线的方法在Python中被称为内置方法，
有时候也被称为魔法方法。重载这些魔法方法一般会改变对象的内部行为。
上面这个例子就让一个类对象拥有了被调用的行为。

回到装饰器上的概念上来，装饰器要求接受一个callable对象，并返回一个callable对象（不太严谨，详见后文）。
那么用类来实现也是也可以的。我们可以让类的构造函数__init__()接受一个函数，然后重载__call__()并返回一个函数，
也可以达到装饰器函数的效果。


"""


# # 所有的函数都是可调用对象。
# # 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
# # 我们把 Person 类变成一个可调用对象：
#
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)


# 现在可以对 Person 实例直接调用：

p = Person('Bob', 'male')
p('Tim')

print('------------------------------------------------------------------------------------------')
class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)  # 返回被装饰函数的本身


@logging
def say(something):
    print("say {}!".format(something))


say('重载')
