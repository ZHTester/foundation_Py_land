"""
抽象基类abc模型
说明: java 是静态类型的语言，所以说他只能单一的继承一个类，但是可以继承多个接口 接口不能实例化的
1 首先Python是动态类型的语言，所以Python接口也是不能实例化的，动态语言是没有数据类型的，在Python中数据类型
  只是一种符号而已，他是可以指向任何类型的对象，所以在Python中从语言的角度上来说，Python本身就是一个支持多态的语言

2 python中信丰的是我们的鸭子类型，所以鸭子类型是贯穿我们整个Python面向对象多，所以我们在设计或者使用Python类中
  我们都需要把Python的鸭子类型放在第一位，他和我们实现class类型的时候，我们是不需要去继承或者去实现指定的类型的
  我们的一个类，主要就是去看，我们这个类主要实现了什么样的魔法函数，魔法函数造成了我们类的独有的特性，所以我们一定要弄
  明白Python和java 动态语言和静态语言的一种区别搞清楚，

3 鸭子类型和魔法函数构成了我们动态语言Python的一个基础，也就是我们Python里面中的一种协议，Python本身不是通过继承
  某一个类或者某一个接口，就有某些特性，而是说我们只要去实现指定的魔法函数，我们的类，就是某种类型的对象，这点还是十分
  的重要的，然后不同的魔法函数，具有不同的特性，或者类型，那么我们的类就是指定的某种数据类型，这种特性，在我们的Python当中
  我们也把他叫做协议。我们在Python编码中都要遵循这样的协议，这样的代码才是Python的代码

4 抽象基类，在这个基础的类中，我们去设定好一些方法，然后所有继承这个基类的类的他都必须覆盖这个抽象基类中的方法，
  抽象基类是无法用来实例化的，


场景:
    我们去检查某个类是否含有某种方法
    我们来检查这个Company是否是一个具有长度这个方法的类

hasattr 来判断一个类是否含有一个属性
isinstance 判断某种类的类型
"""
from collections.abc import Sized


class Company(object):
    def __init__(self, employ_list):
        self.employee = employ_list

    def __len__(self):
        return len(self.employee)


com = Company(['json', 'path', 'dir'])

a = hasattr(com, '__len__')
# print(a)
"""
我们在某些情况下，需要判断某个对象的类型，这个时候我们就需要用到我们的抽象基类

"""
print(isinstance(com, Sized))
print(len(com))

"""
我们需要强制某个子类必须实现某些方法 
实现了一个web框架，集成cache(redis,cache,memorychache)
需要设计一个抽象基类，指定子类必须实现某些方法

如果我们不实现这一的抽象基类，那么用户肯定就会到我们的代码中去修改，所以我们还是需要去实现一些抽象基类的
我们在配置文件设置好以后，那么用户的实现就十分的方便了

如何去模拟一个抽象基类了，需要考虑的点

"""


class CacheBase(object):
    def get(self, key):
        pass

    def set(self,key,value):
        pass


