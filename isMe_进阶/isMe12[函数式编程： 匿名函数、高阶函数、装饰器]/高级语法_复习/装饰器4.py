# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/17  16:31'
"""
1 装饰器中多个参数的传入
2 含有一个参数和多个参数的传入，·1个参数 ·2个参数  ·多个参数


"""
import time


# 这样的形式就是装饰器 - 这既是定义一个装饰器
def decorator(func):
    def wrapper(*args):  # 被装饰的函数是没有传入参数的
        print(time.time())
        func(*args)

    return wrapper


@ decorator
def f1(d):
    print("this is function"+d)


@ decorator
def f2(d1, d2):
    print(d1+'this is function2'+d2)


f1('.....你大爷还是你大爷的.....')  # 这样语法糖的形式，是没有改变我们的本身函数调用的形式的。
print('-----------------------------------------------------------------------')
f2('爆炸了', '爆炸了')  # 多个参数的问题
























































