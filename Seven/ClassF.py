"""

类方法
 1 类方法只能访问类变量不能访问实例变量
 
"""


class Dog(object):

    # n = 333
    name = 'macLi'

    def __init__(self, name):
        self.name = name
        # self.n = 3333

    @classmethod  # 实际上跟类没有什么关系了 类下面的一个函数
    def eat(self):
        print('%s is eating is ...... %s' % (self.name, 'dd'))

    def talk(self):
        print('%s is taklking ' % self.name)


d = Dog('Mac Chen')
d.eat()

