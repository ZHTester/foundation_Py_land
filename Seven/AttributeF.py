"""

属性方法

1 属性方法就是把一个方法变成一个静态属性
2 __dict__ 查看类或对象中的所有成员
3 __str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。

"""


class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self, name):
        self.name = name
        self.__food = None

    # @staticmethod #实际上跟类没什么关系了
    # @classmethod
    @property  # attribute
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

    def talk(self):
        print("%s is talking " % self.name)

    def __call__(self, *args, **kwargs):
        print("running call", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name


# print(Dog.__dict__)  # 打印类里面的所有属性

# print(Dog.__doc__)   # 打印类的描述信息

# d = Dog("ChenRonghua")
# d(1, 2, 3, name='123')

d = Dog("ChenRonghua")
print(d)  #
# print(d.__dict__)  # 打印所有实例属性，不包含类属性
# print(d)
