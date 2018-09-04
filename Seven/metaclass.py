class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs): # 给对象添加一个括号 对象就自动调用这个方法
        print("--MyType call---")

        obj = self.__new__(self, *args, **kwargs)
        obj.data = {"name": 111}
        self.__init__(obj, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType  #

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    # 通过New来实现实例化的 通过new来调用的 new是通过来创建类的
    def __new__(cls, *args, **kwargs):  # 类自带的方法
        print("Foo --new--")
        # print(object.__new__(cls))
        return object.__new__(cls)  # 继承父亲的__new__方法


# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo("Alex")
print(obj.name
      )
