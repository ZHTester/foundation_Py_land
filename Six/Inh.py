"""
继承

1 单继承 多继承
2 新式类的写法主要体现在继承上

"""


class People(object):   # 新式类 多继承的方式变了

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating .....' % self.name)

    def talk(self):
        print('%s is taking ......' % self.name)

    def sleep(self):
        print('%s is sleep .....' % self.name)

    # 继承函数


class Man(People):
    # 覆盖父类的构造方法  对构造方法进行重构
    # super就是继承父类的的方法  单继承 多继承
    def __init__(self, name, age, money):
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)
        self.money = money
        print('%s 一出生就有 %s money' % (self.name, self.money))   # 新式类的写法

    # 新增子类的方法
    def piao(self):
        print('%s is piaowanle  20s done' % self.name)

    # 重构父类的方法
    # 首先调用父类的方法在调用子类的方法
    def sleep(self):
        People.sleep(self)
        print('%s is sleeping sun' % self.name)


class Woman(People):
    def get_birth(self):
        print('%s is born a baby' % self.name)


m1 = Man('Niuhanyang', 22, 20)
m1.eat()
m1.piao()
m1.sleep()

w1 = Woman('chongzhonghua', 26)
w1.get_birth()






