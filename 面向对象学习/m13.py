"""
属性方法

1 属性方法的作用就是通过@property把一个方法变成一个静态属性.
2 调用会出以下错误， 说NoneType is not callable, 因为eat此时已经变成一个静态属性了，
3 不是方法了， 想调用已经不需要加()号了，直接d.eat就可以了.
"""


class Dog(object):

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(" %s is eating" % self.name)


d = Dog("ChenRonghua")
# d.eat()
d.eat
