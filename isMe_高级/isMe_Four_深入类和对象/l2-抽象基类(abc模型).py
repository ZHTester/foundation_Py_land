"""
抽象基类也就是 ---abc模块 -- (--其实这里就可以理解成java中的接口--)
说明: java 是静态类型的语言，所以说他只能单一的继承一个类，但是可以继承多个接口 接口不能实例化的
1 首先Python是动态类型的语言，所以Python接口也是不能实例化的，动态语言是没有数据类型的，在Python中数据类型
  只是一种符号而已，他是可以指向任何类型的对象，所以在Python中从语言的角度上来说，Python本身就是一个支持多态的语言
  动态语言和静态语言最大的区别就是，动态语言是不需要我们去指明数据的类型，而静态语言是需要的。

2 python中信丰的是我们的鸭子类型，所以鸭子类型是贯穿我们整个Python面向对象的过程当中，所以我们在设计或者使用Python类中
  我们都需要把Python的鸭子类型放在第一位，他和我们实现class类型的时候，我们是不需要去继承或者去实现指定的类型的
  我们的一个类，所具有什么特性，不是去看这个类继承或实现了什么样的接口，而是主要就是去看，我们这个类主要实现了什么样的魔法函数，
  魔法函数造成了我们类的独有的特性，所以我们一定要弄，明白Python和java 动态语言和静态语言的一种区别搞清楚，

3 鸭子类型和魔法函数构成了我们动态语言Python的一个基础，也就是我们Python里面中的一种协议，Python本身不是通过继承
  某一个类或者某一个接口，就有某些特性，而是说我们只要去实现指定的魔法函数，我们的类，就是某种类型的对象(如果我们实现了某些魔法函数
  ，那么我们的类就是执行的某些方法的指定类型)，这点还是十分的重要的，然后不同的魔法函数，具有不同的特性，或者类型，
  那么我们的类就是指定的某种数据类型，这种特性，在我们的Python当中，我们也把他叫做协议。我们在Python编码中都要遵循这样的协议，
  这样的代码才是Python的代码

4 ·1 抽象基类，在这个基础的类中，我们去设定好一些方法(这个也就是魔法函数)，然后所有继承这个基类的类的他都必须覆盖这个抽象基类中的方法，
  ·2 抽象基类是无法用来实例化的，


场景:
    我们去检查某个类是否含有某种方法
    我们来检查这个Company是否是一个具有长度这个方法的类型

hasattr 来判断一个类是否含有一个属性
isinstance 判断某种类的类型
"""
from collections.abc import Sized


class Company(object):
    def __init__(self, employ_list):
        self.employee = employ_list

    # def __len__(self):
    #     return len(self.employee)


com = Company(['json', 'path', 'dir'])

# 判断某个对象是否含有某个属性 hasattr 也就是说在类中都含有这样的类型属性
a = hasattr(com, '__len__')
# print(a) # True  这样就能判断我们这样的一个类型是具有这样的函数属性的

"""
我们在某些情况下(我们是需要直接去判断这个对象是否具有这样的类型属性的)，
需要判断某个对象的类型，这个时候我们就需要用到我们的抽象基类

"""
print(isinstance(com, Sized))
list_demo = [1, 2, 3, 4]
print(len(list_demo))

"""
我们需要强制某个子类必须实现某些方法 
实现了一个web框架，集成cache(redis,cache,memorychache)
需要设计一个抽象基类，指定子类必须实现某些方法

如果我们不实现这一的抽象基类，那么用户肯定就会到我们的代码中去修改，所以我们还是需要去实现一些抽象基类的
我们在配置文件设置好以后，那么用户的实现就十分的方便了

如何去模拟一个抽象基类了，需要考虑的点

abc模块 也就是存放了2个地方的 
第一个就是: from collections.abc
           import abc 这个需要重点去了解全局的abc模块
        

"""

# 这样就实现了一个抽象基类

import abc
from collections.abc import *

"""
····from _collections_abc import __all__ 
····这里面实现的都是抽象基类 
··········································································1
"Awaitable", "Coroutine",
           "AsyncIterable", "AsyncIterator", "AsyncGenerator",
           "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
           "Sized", "Container", "Callable", "Collection",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           "ByteString",
Awaitable
每种抽象基类都是实现了这样的要给---魔法函数
def __subclasshook__(cls, C):
"""

class CacheBase(metaclass=abc.ABCMeta):

    # 这里就定义了一个抽象方法 因为添加了一个装饰
    # 这里默认抛出异常后，如果继承这个抽象基类的方法，没重写这个方法，那么就会抛出异常，这里就强制抛出异常
    @abc.abstractmethod
    def get(self, key):
        pass
        # raise NotImplementedError

    @abc.abstractmethod
    def set(self, key, value):
        pass
        # raise NotImplementedError


"""
1 采用了这样的抽象基类，这样的方法实现，就是会强制子类去实现或者说去重载父类的方法，这样就是bac基类的作用
因为子类在初始化的时候，就会抛出异常。

2 抽象基类在Python当中，实际上是它已经实现了一些通用的抽象基类，让我们可以去了解我们Python数据结构
的一些接口，他是放在我们 from collections.abc import * 当中的

3 抽象基类可以给我给接口的一些强制规定，也就是Python中的抽象基类的实现 这个时候我们就需要使用python中的抽象基类

4 但是抽象基类并不是十分的推荐去使用

5 抽象基类是由哪些基类构成了我们dict的接口了，这个是需要我们去研究的

6 抽象基类也不是让我们去继承的，他只是让我们去理解Python当中的一些继承关系


"""


# 这里我们继承了这个抽象基类的子类，那么我们就需要去重写父类中的抽象方法
# 采用了这样的抽象基类,就必须强制要求子类必须实现父类的某些方法

class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass


redis_cache = RedisCache()
# 调用的时候就抛出异常，我们现在希望的是在初始化当中就抛出异常。这个时候我们就需要使用abc模块
# redis_cache.set("key", "value")
