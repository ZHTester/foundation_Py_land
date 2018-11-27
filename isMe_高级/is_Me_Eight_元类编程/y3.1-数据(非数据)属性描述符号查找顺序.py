# coding=utf-8
"""
属性描述符和属性查找过程

1 如果说User是一张表，那么字段我们有时候需要去判断他的字符串类型 比如说email 还是 name
2 数据描述符与非数据属性描述符，对我们的属性的查找顺序是不一样的
3 属性查找其实就是django的一个module，其实也是orm实现的一个基础

"""
from datetime import date, datetime
import numbers

"""
这个类如何变为属性描述符
类实现了get set 或者说是delete (魔法函数)方法 我们只需要实现这三个魔法函数中的任意一个
属性描述描述符，但是属性描述符能做什么了，他可以将逻辑拿来检查，
    def __get__(self, instance, owner):
    def __set__(self, instance, value):
    def __delete__(self, instance):

"""


# 这个类就是属性描述符的对象 所以说age就是一个属性描述符号的对象
# 这样的方式我们就控制到了，在属性设置的时候的一个参数检查
class IntFeild:
    # 数据属性描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need ")

        if value < 0:
            raise ValueError("你的值需要大于0")
        # 将值保存起来 self就是指代当前的类对象<------>IntFeild
        self.value = value
        pass

    def __delete__(self, instance):
        return self.value


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        pass


class User:
    """
    这个age 就不输入User中的变量类型了
    IntFeild() 传递给这个 age ---->对象 age这个属性是属于User这个类的，
    而不是属于
        def __init__(self, name, email, birthday):
        self.name = name
        self.birthday = birthday
        self.email = email
        self._age = 0
        这个实例的
    """
    # age = IntFeild()  # 这时候的age就是一个属性描述符
    age = NonDataIntField()  # 这个时候他就进入到我们的非数据属性描述符中


'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：

（1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor(属性描述符)， 那么调用其__get__方法, 否则

（2）如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则

（3）如果“age”出现在User或其基类的__dict__中

（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则

（3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError
'''

if __name__ == "__main__":
    user = User()
    """
    这里进行赋值的时候实际上是会调用，属性描述符中的set方法
    def __set__(self, instance, value):
    这个时候instace 就是User value就是我们设定的值30 

    """
    # user.age = 30
    """
    如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]，
    则我们直接返回这样的一个属性描述符的参数
    """
    user.__dict__["age"] = "abc"
    '''
    # 这样查找的方式就是dict中的属性而不是age中的属性，这就是.操作符的特殊之处
    # 查找到dict其实就是对dict进行一个操作了，这样就和属性查找就没有关系了
    '''
    print(user.__dict__)
    print(user.age)  # 虽然说这样的方式是将我们的user中的age放入到了dict中，但是我们的顺序还是按照属性描述符来进行的
    """
    ValueError: int value need 
    如果这里的值不是int类型那么自然就会报错了
    ----
    raise ValueError("int value need ")
    ValueError: int value need 
    """
    # user.age = 'abc'
    """
    # age = IntFeild()  # 这时候的age就是一个属性描述符
    
    给对象的属性赋了一个值，其实实际上我们之前的认知就是在我们的对象当中的__dict__ 
    但是属性描述符中的对象描述符的优先级是最高的，它就进入了我们数据描述符的对象中 
    
    这个时候其实没有进入到 user.__dict__ 当中的
    print(user.__dict__) 就会打印出{}
    """
    """
    age = NonDataIntField()  # 这个时候他就进入到我们的非数据属性描述符中
    但是如果我们调用的非数据属性描述符中，那么首先就会去调用__get__()方法
    {'age': 30}
    30
    
    """
    # print(getattr(user, "age"))



