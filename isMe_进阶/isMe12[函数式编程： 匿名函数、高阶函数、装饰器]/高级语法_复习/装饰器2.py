# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/17  15:16'
"""
1 装饰器只是一种设计模式
2 装饰器最大的特点就是，将外部的函数返回内部的函数，其实这样的设计模式就是闭包。
3 
"""
import time


# 这样的形式其实就是将被封装的函数封装到了内部
# 这样的写法内聚性也是颇为高的 不是单一的装饰器写法
def decorator(func):  # 装饰的意思
    def wrapper():  # 被封装的含义
        print(time.time())
        func()
    return wrapper


def f1():
    print('this is function1')


a = decorator(f1)
a()  # 其实这里就是封装了一个wrapper参数加上括号也就是函数式的调用











