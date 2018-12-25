"""
鸭子类型和多态
1 鸭子类型 - 当你看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟可以被称之为鸭子。
2 在Python中我们如果要实现多态，我们只需要实现共同的方法名称就可以了  -------> ，但是在java中我们需要去重写
  java中的父类方法，他能这么简单，也就是实现了Python的动态性
3 魔法函数也是充分的利用了我们的鸭子类型
4 鸭子类型，也就是我们在任何类型中，只需要指定某一个方法名，这些类我们都可以通用的，实际上在Python中
  他的魔法函数也是充分的利用了我们的鸭子类型，所以在python很多类型中，他都回去写入很多魔法函数，这些魔法函数
  就会被Python本身的解释器识别，所以说在很多Python内置的而方法或者内置的类中，他们都会具有一些很好使用的特性
  ，比如说可迭代的特性，返回len的特性，所以这就是代码本身给我们提供的灵活性了，
5 只要我们实现了某些魔法函数，也就是实现了Python内置函数的特性，那么我们就可以实现这个类的某些内置函数的特性了
6 鸭子类型在定义的最初就已经定义好了，需要含有共同的方法，鸭子类型是和我们方法相关的，鸭子类型会贯穿我们对Python的理解
7 我们可以复制任何Python的中的任何数据给我们Python中的任何变量
8 鸭子类型本身是我们Python中的协议 也就是Python中的数据类型   这些类型都是区别于我们静态语言的一些类型中的概念

"""


class Cat(object):
    def say(self):
        print('i am cat')


class Dog(object):
    def say(self):
        print('i am dog')

    """
    实现了这样的一个getitem 实际上这个类型就是可迭代的类型了
    """
    def __getitem__(self, item):
        return 'boby'[item]


class Duck(object):
    def say(self):
        print('i am duck')


class Company(object):
    def __init__(self, employ_list):
        self.employee = employ_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['tom', 'bob', 'jane'])


"""
1 首先animal 可以指向任意的一个类型 这是动态语言的一个特性，这也是和静态语言不一样的地方 

"""
# animal = Cat
# animal().say()

"""
1 animal_list = [Cat, Dog, Duck] 这样的调用方式有一个共同的相同点，就是实现了共同实现了
  同一个方法名
"""
# 这样的写法也就是可以指向任意一个方法名称，这样的类都可以归为一种类型，这样其实就是实现了我们的鸭子类型
animal_list = [Cat, Dog, Duck]

for animal in animal_list:
    # 这里就可以调用同一个方法名 这样也是可以实现了多态 都实现了一个say方法
    animal().say()



print('---------------------------------------------')

a = ['land1', 'land2']
b = ['land2', 'land']
name_tuple = ['land3', 'land4']
name_set = set()
name_set.add('land5')
name_set.add('land6')
'''
def extend(self, iterable) 这就是告诉了我们，这里不单单可以只用list对象
用可迭代的对象也是可以的(iterable),实际上在Python当中,tuple set 都是可迭代的对象
解释: 这样的用法也就是我们鸭子类型的用处了，他首先回去调用我们这个对象里面的迭代器比如说(
     def extend(self, iterable)),他是隐含的调用，他会去找到我们这个对象里面的迭代器
     def __iter__  或者获取找到这个里面的
     def __getitem__ 

'''
# a.extend(b)  # 将2个list合并成一个list
# a.extend(name_set)  # 将2个tuple合并成一个list
# a.extend(name_tuple)  # 将2个set合并成一个list
'''
  对象内部含有这样的一个可迭代的对象，
  那么他就可以变为一个可迭代的对象含有可迭代的方法 他就变成了可迭代的对象
  
  也就是说extend 函数接受 company这个对象，这个extend方法中会自动去调用company迭代器的方法 这样的话看起来就像鸭子了
'''
# a.extend(company)
dog = Dog()
a.extend(dog)  # 这样的话这个对象也将变为可迭代的对象  这也就是魔法函数的魅力














