"""
装饰器5
1
2
3
4
5
6
7
8


"""
import time


# # 这样的形式就是装饰器 支持一个参数的装饰器
# def decorator(func):
#     def wrapper(func_name):
#         print(time.time())
#         func(func_name)
#
#     return wrapper


# 这样的形式就是装饰器 支持多个参数的装饰器 利用可变参数
def decorator(func):
    def wrapper(*func_name, **kw):
        print(time.time())
        func(*func_name, **kw)  # 解码   # 支持关键字参数

    return wrapper


# 这样就是为我们的f1添加了新的功能 装饰器的核心点就是这个@
# 也就是装饰器的核心点 只有这样的一个@才能保证我们的装饰器是不会被破坏的
@decorator
def f1(func_name):
    print("this is function" + func_name)


@decorator
def f2(func_name, func_name2):
    print("this is function" + func_name, func_name2)


@decorator
def f3(func_name, func_name2, **kw):  # 支持关键字参数 关键字参数的用法
    print("this is function" + func_name, func_name2)
    print(kw)


f1('test func')  # 未改变函数原来所调用的方式 保持原有函数的调用方式不变，这就是函数调用的意义所在与优势
f2('test1', 'test2')
f3('test1', 'test2', a=1, b=2, c=123)
