"""
开闭元组
装饰器结尾工作
1 如果我们相对某些单元进行一些修改我们可以不去改动这些函数的实现，我们可以通过装饰器的形式来改变这个函数的行为代码的稳定性

2 代码的复用性-把这样的一个逻辑封装成了一个装饰器也就是一个逻辑-如果现在我们要为一个函数增加一个功能，但是也不想去修改函数
  内部的实现，这个时候装饰器的优势就体现出来了，不会去破坏代码的内部实现

3 装饰器可以多个装饰器装饰同一个函数

4 装饰器就是体现了aop的一个思想

1 如果我们相对某些单元进行一些修改或者说增加一些功能，我们可以再不去修改这些函数的实现，我们可以通过装饰器的形式
  来修改代码行为的稳定性

2 代码的复用性吧这样的逻辑封装成了一个装饰器，也就是这样的一个逻辑，如果我们要为一个函数增加一个功能，但是也不想去修改函数
  的内部实现，这个时候装饰器的优势就能体现出来，不会去破坏代码内部的实现

3 装饰器可以同时装饰多个函数

4 装饰器就是体现了aop的一个思想
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










