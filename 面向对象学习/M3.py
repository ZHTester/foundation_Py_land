"""
类的属性定义
1 python定义类的的属性是有私有访问控制的变量的
2 如果确实是需要类的私有属性访问控制，那么就是通过python的命名规范来变写的

"""


class Programer(object):
    def __init__(self, name, age, weight):
        self.name = name  # 公有方法来访问的
        self._age = age  # 私有属性 但是我们还是可以访问的(一条下划线)
        self.__weight = weight  # 在类里面是可以访问的，但是想在类的对象里面访问是不可以的(两条下划线)

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    pro = Programer('bej',25,99)
    print(dir(pro))  # 打印所有的方法
    print(pro.__dict__)  # 从构造函数中获取的属性
    print(pro.get_weight())
    print(pro._Programer__weight)  # 变向的访问私有属性
