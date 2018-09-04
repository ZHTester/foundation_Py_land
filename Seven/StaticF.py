"""
静态方法  一般都不常用

1 通过@staticmethod装饰器即可把其装饰的方法变为一个静态方法，什么是静态方法呢？其实不难理解，普通的方法，
可以在实例化后直接调用，并且在方法里可以通过self.调用实例变量或类变量，但静态方法是不可以访问实例变量或类变量的，
一个不能访问实例变量和类变量的方法，其实相当于跟类本身已经没什么关系了，它与类唯一的关联就是需要通过类名来调用这个方法
-----
2 想让上面的代码可以正常工作有两种办法
1. 调用时主动传递实例本身给eat方法，即d.eat(d)
2. 在eat方法中去掉self参数，但这也意味着，在eat中不能通过self.调用实例中的其它变量了
3 上面的调用会出以下错误，说是eat需要一个self参数，但调用时却没有传递，没错，当eat变成静态方法后，
  再通过实例调用时就不会自动把实例本身当作一个参数传给self了。
-----
3 静态方法可以放在脚本中的任何地方

"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod  # 实际上跟类没有什么关系了 类下面的一个函数
    def eat(self):
        print('%s is eating is ...... %s' % (self.name, 'dd'))

    def talk(self):
        print('%s is taklking ' % self.name)


d = Dog('Mac Chen')
d.eat(d)
d.talk()
