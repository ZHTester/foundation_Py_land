# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/17  15:39'
"""
1 装饰器的语法糖 @
2 我们可以接受定义时候的复杂，只要他让我们在调用的时候足够简单就可以了，这才是装饰器中的含义
3 未改变函数原来所调用的方式 保持原有函数的调用方式不变，这就是函数调用的意义所在与优势，这就是装饰器最大的特点
4 我们可以接受定义时候的复杂，但是我们不能接受调用时候的复杂，这就是基本的原则性问题。、
5 AOP的编程模式 - 思想
"""
import time


# 这样的形式就是装饰器 - 这既是定义一个装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


@ decorator
def f1():
    print("this is function")


def f2():
    print('this is function2')


f1()  # 这样语法糖的形式，是没有改变我们的本身函数调用的形式的。


