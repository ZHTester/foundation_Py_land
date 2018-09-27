"""
定义类的方法

1 函数和方法
    1 函数是直接调用函数名来调用
    2 方法是和对象结合在一起使用 - 方法是类的一部分

2 类方法也是类的属性

3 方法的访问控制
  1 也是跟属性是一样的，基本上是没有访问控制的
class oo(object)
  def add(self):
    pass
  2 方法的装饰器
  @classmethod
   1 调用的时候用类名，而不是某个对象
  @property
   2 向访问属性一样调用方法

"""
class Programer(object):
    hobby = 'Play japanse'

    def __init__(self, name, age, weight):
        self.name = name  # 公有方法来访问的
        self._age = age  # 私有属性 但是我们还是可以访问的(一条下划线)
        self.__weight = weight  # 在类里面是可以访问的，但是想在类的对象里面访问是不可以的(两条下划线)


    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('my name is %s \ni am %s years old\n' %(self.name,self._age))


if __name__ == '__main__':
    pro = Programer('bej', 25, 99)
    print(dir(pro))  # 打印所有的方法
    print(Programer.get_hobby())
    print(pro.get_weight)  # 这样的访问形式就想访问一个属性一样的调用
    print(pro.self_introduction())  # 正常的调用方式










