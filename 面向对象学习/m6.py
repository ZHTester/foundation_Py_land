"""
类的多态

1 啥是多态
    多态的要素
    1 继承
    2 方法的重写


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
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('my name is %s \ni am %s years old\n' % (self.name, self.language))

def introduce(programer):
    if isinstance(programer,Programer):
        programer.self_introduction()

if __name__ == '__main__':
    pro = Programer('bej', 25, 99)
    back = BackendProgramer('tim',30,80,'python')
    introduce(pro)
    introduce(back)
