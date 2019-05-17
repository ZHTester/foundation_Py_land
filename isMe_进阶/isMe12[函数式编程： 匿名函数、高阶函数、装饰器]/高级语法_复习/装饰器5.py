# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/17  16:57'
"""
多个参数的传递  --- 多个关键字参数的传递

"""
import time


# 这样的形式就是装饰器 - 这既是定义一个装饰器
def decorator(func):
    def wrapper(*args, **kwargs):  # 被装饰的函数是没有传入参数的
        print(time.time())
        func(*args, **kwargs)

    return wrapper


@decorator
def f1(d):
    print("this is function" + d)


@decorator
def f2(d1, d2):
    print(d1 + 'this is function2' + d2)


@decorator
def f3(func_name, func_name2, **kw):  # 支持关键字参数 关键字参数的用法
    print("this is function" + func_name, func_name2)
    print(kw)


f1('.....你大爷还是你大爷的.....')  # 这样语法糖的形式，是没有改变我们的本身函数调用的形式的。
print('-----------------------------------------------------------------------')
f2('爆炸了', '爆炸了', a=1)  # 多个参数的问题
print('-----------------------------------------------------------------------')
f3('test1', 'test2', a=1, b=2, c=123)
