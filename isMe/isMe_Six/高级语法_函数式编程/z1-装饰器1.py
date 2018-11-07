"""
装饰器

1 装饰器更多的是一种设计模式。
2 对修改是封闭的，对扩展是开放的。
3 装饰器的本质就是给函数新增了功能，在不破坏函数内部接口的情况下
"""
import time


# def f1():
#     print('this is function')
#
# # unix 时间戳 这个就需要去百度了
# def f2():
#     print('this is function')
#
# def print_current_time(func):
#     print(time.time())
#     func()

def f1():
    print('this is function_one !')


def f2():
    print('this is function_two !')


def f3(func):
    print(time.time())
    func()


f3(f1)
print("-------------")
f3(f2)
