"""
继承

1 多继承

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


class Relatio(object):
    # self 就是代表的是当前对象类
    def make_friends(self, obj):
        print('%s is make friends with %s' % (self.name, obj.name))

    # 多继承函数
    # 多继承的顺序就是从左到右边


class Man(People, Relatio):
    # 覆盖父类的构造方法  对构造方法进行重构
    # super就是继承父类的的方法  单继承 多继承
    def __init__(self, name, age, money):
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)
        self.money = money
        print('%s 一出生就有 %s money' % (self.name, self.money))

    # 新增子类的方法
    def piao(self):
        print('%s is piaowanle  20s done' % self.name)

    # 重构父类的方法
    # 首先调用父类的方法在调用子类的方法
    def sleep(self):
        People.sleep(self)
        print('%s is sleeping sun' % self.name)


class Woman(People, Relatio):
    def get_birth(self):
        print('%s is born a baby' % self.name)


m1 = Man('Niuhanyang', 22, 20)


w1 = Woman('chongzhonghua', 26)


m1.make_friends(w1)






