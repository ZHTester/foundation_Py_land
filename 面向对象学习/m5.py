"""
1 继承 使得大量的代码被复用 也就是实现了大量代码被复用的一个所在
2 object是一切类的父类，如果没有其他的类继承那么就需要继承object父类

3 继承的子类
    1 会继承父类的属性和方法
    2 也可以自定义，覆盖父类的属性和方法
    3 用super()调用父类的方法 -  子类调用父类的方法就使用super
    class A(Object):
        def method(self, arg)
           pass

    class B(A):
        super(B,self).method.(arg)

    4 子类的类型判断(内建函数)  - 判断类型
        * isinstance
        * issubclass
4 多继承 展示也不会使用到
    class DerivedClassName(Base1,base2,base3):
    《statement -1》
    .
    .
    .
    <statement -N>


"""


class Programer(object):
    hobby = 'Play japanse'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod  # 类方法
    def get_hobby(cls):
        return cls.hobby

    @property  # 属性方法
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('my name is %s \ni am %s years old\n' % (self.name, self._age))


"""
实现单继承
"""


class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        """
        调用了父类的构造函数
        :param name:
        :param age:
        :param weight:
        :param language:
        """
        super(BackendProgramer, self).__init__(name, age, weight)  # 集成了父类的构造方法
        self.language = language


if __name__ == '__main__':
    pro = BackendProgramer('bej', 25, 99, 'python')
    print(dir(pro))  # 打印所有的方法
    print('------------------------------')
    print(pro.__dict__)  # 打印出字典类型的数据
    print('------------------------------')
    print(type(pro))  # 这样的访问形式就想访问一个属性一样的调用
    print('------------------------------')
    print(pro, Programer)  # 判断类型
