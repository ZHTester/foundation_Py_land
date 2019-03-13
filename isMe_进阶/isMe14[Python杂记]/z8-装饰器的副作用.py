# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/12  17:08'
"""
装饰器的副作用 

解决这样的装饰器的另外的方法就是通过包的形式来解决 
from functools import wraps

"""
import time
from functools import wraps


# 这样的形式就是装饰器
def decorator(func):
    @wraps(func)  # 这样就实现了装饰器的功能也保留了原有函数的一个功能 保持原有函数的不变
    def wrapper():
        print(time.time())
        func()

    return wrapper


# 这样就是为我们的f1添加了新的功能 装饰器的核心点就是这个
# 也就是装饰器的核心点 只有这样的一个@才能保证我们的装饰器是不会被破坏的
# --- 添加了装饰器会对我们原有的f1函数会产生什么样的影响 ---
# --- 加有装饰器的情况下，这个是会改变我们装饰器本身的名称的，这样的情况在某些情况下是会出现错误的
@decorator
def f1():
    """
        this is f1

    """
    print(f1.__name__)  # 这是含有装饰器的情况 打印函数的名称 def wrapper()


print(help(f1))

# f1()
