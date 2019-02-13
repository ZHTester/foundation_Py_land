# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/11  9:48'
"""
1 yield - from 方法 是Python3.3中新加的特性 这个函数也是十分重要难以理解的一个函数知识点
2 from itertools import chain ----> 将我们迭代的类型连接起来做一个for循环
3 协程也是一个可迭代(iterable)的对象 也就是说yield from 后面是需要跟一个可迭代的对象 
4 因为有了yield from 我们去调用另外一个协程才变的可行

"""
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "landing1": "https://www.baidu.com",
    "landing2": "https://www.baidu.com"
}


# yield from iterable
def my_chain(*args):  # 这里传入的数量是不确定的
    for my_iterable in args:
        yield from my_iterable


# from itertools import chain ----> 将我们迭代的类型连接起来做一个for循环
for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)

# ---------------------------对比分隔线--------------------------------

# def my_chain(*args):  # 这里传入的数量是不确定的
#     for my_iterable in args:
#         yield from my_iterable
#         for value in my_iterable:
#             yield value
#
#
# # from itertools import chain ----> 将我们迭代的类型连接起来做一个for循环
# for value in my_chain(my_list, my_dict, range(5, 10)):
#     print(value)
