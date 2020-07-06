# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/26  17:14'
"""
1 什么是迭代器和可迭代对象 ....  迭代器和可迭代对象的区别  .....
2 迭代器的设计模式  .... 这个有空需要好好了解一下  
3 我们在定义可迭代对象或者说可迭代类型的时候，我们不能将原有的数据类型拿到被定义的数据类型中来做。 
4 iter(a) Iterable 也就是实现了iter这个魔法函数 ，返回一个迭代器 Iterator ，这个也就是实现了next方法 这个就是迭代器的重点所在
  如果不是这样的一个逻辑那么他就会报错的 ~ 
5 我们在遍历大数据的时候，就不可能直接使用list内存中，我们是会使用迭代器的来操作的 

迭代器与常规序列的区别-------
它与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算（lazy evaluation）
方式返回元素，这正是它的优点。比如列表含有中一千万个整数，需要占超过400M的内存，而迭代器只需要几十个字节的空间。
因为它并没有把所有元素装载到内存中，而是等到调用 next 方法时候才返回该元素(按需调用 call by need 的方式，
本质上 for 循环就是不断地调用迭代器的next方法)
"""
from collections.abc import Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    """
    1 这里我们就必须定义一个 Iterator 也就是实现一个迭代器，也就是继承迭代对象都要实现一个新的迭代器
    这样的实现方式就是迭代器的实现方式 .....
    2 现在的迭代器是不支持切片操作的 .....
    3 不支持切片也就是在需要的时候，才产生数据
    4 这里就直接返回 return MyIterator(self.employee) 这样的一个迭代器
    """
    def __iter__(self):
        # 单独实现的迭代器对象
        return MyIterator(self.employee)

    """
    迭代对象 默认创建的迭代器
    """
    # def __getitem__(self, item):
    #     return self.employee[item]


# # 这样的方式就是基于迭代协议来实现的: 也就是魔法函数-迭代器的魔法函数
# class MyIterator:
#     def __iter__(self):
#         return self


# 用迭代器外部的迭代器对象, 来维护外部的迭代对象。
# 自定义迭代器 迭代器的前提实现了迭代协议
# 继承了 Iterator 也就是实现了迭代协议

class MyIterator(Iterator):
    """
    真正返回迭代逻辑的就是在next这个魔法函数种
    """
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    """
    1 next只能一步一步的传递值进来，并且不能传递索引值进来的
    2 所以这个时候，我们就需要维护内部的常规变量了 self.index
    3 迭代器是不支持切片的 迭代的时候在需要的时候才会产生数据
    4 
    """
    def __next__(self):
        # 真正返回迭代值是在next魔法函数中，这样才是实现了一个可迭代的对象，也就是迭代器
        try:
            word = self.iter_list[self.index]
        except IndexError:
            """
            for 语句是会处理 StopIteration 异常的，但是是不能处理  IndexError 所以这里需要做一个异常转换的 
            """
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['tom', 'bob', 'jane'])
    # 其实这样我们就可以实现一个for循环了
    """
    我们在调用for循环的时候，实际上for循环就会去寻找
    iter(company)，这个是python解释器内部去寻找的，如果没有这样的函数，他就会默认去寻找迭代对象，而不是去寻找迭代器。
    iter() 迭代器的退一步去创建默认的迭代器
    
        # def __getitem__(self, item):
    #     return self.employee[item]
    
    """
    my_iter = iter(company)

    # 这个其实就是初步的迭代器 for循环
    # while True:
    #     try:
    #         print(next(my_iter))
    #     except StopIteration:
    #         pass

    # next(my_iter)  # 实际上在for循环内部的原理也是一样的 for循环 = Next
    #
    for intem in company:
        print(intem)
