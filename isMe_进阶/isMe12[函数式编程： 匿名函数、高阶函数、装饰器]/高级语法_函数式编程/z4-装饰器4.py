"""
如果说在装饰器中我们需要传入某些参数而进行一些改变，才能支持带参数的函数的装饰器了
1 支持一个参数的装饰器
2 支持2个参数的装饰器，支持多个参数的装饰器，多个参数支持 *args  **kw



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
    def wrapper(*func_name):
        print(time.time())
        func(*func_name)  # 解码

    return wrapper


def decorator_one(func):
    def wrapper(*func_name):
        print(time.time())
        func(*func_name)

    return wrapper


# 这样就是为我们的f1添加了新的功能 装饰器的核心点就是这个@
# 也就是装饰器的核心点 只有这样的一个@才能保证我们的装饰器是不会被破坏的
@decorator
def f1(func_name):
    print("this is function" + func_name)


@decorator
def f2(func_name, func_name2):
    print("this is function" + func_name, func_name2)


f1('test func1')  # 未改变函数原来所调用的方式 保持原有函数的调用方式不变，这就是函数调用的意义所在与优势
print('--------------------')
f2('test1', 'test2')
