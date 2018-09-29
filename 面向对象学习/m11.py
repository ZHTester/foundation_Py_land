"""
静态方法 。。。。。。

在eat方法中去掉self参数，但这也意味着，在eat中不能通过self.调用实例中的其它变量了

通过@staticmethod装饰器即可把其装饰的方法变为一个静态方法，什么是静态方法呢？其实不难理解，
普通的方法，可以在实例化后直接调用，并且在方法里可以通过self.调用实例变量或类变量，
但静态方法是不可以访问实例变量或类变量的，一个不能访问实例变量和类变量的方法，其实相当于跟类本身已经没什么关系了，
它与类唯一的关联就是需要通过类名来调用这个方法

"""


# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod  # 把eat方法变为静态方法
#     def eat(name):
#         print("%s is eating" % name)
#
#
# d = Dog("ChenRonghua")
# Dog.eat('riben')


class Big(object):
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return self.name
    # @staticmethod
    def check(self):
        print('%s is eating' % self.name)


c = Big('beij')
print(c.check())
