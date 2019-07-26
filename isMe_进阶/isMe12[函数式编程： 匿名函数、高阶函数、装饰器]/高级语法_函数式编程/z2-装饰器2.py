"""
装饰器2  - 装饰器只是一种模式 所谓的模式也是一种设计模式

1 体现对函数的功能的增加不是修改函数的本身
2 体现函数之间的关联性 并没有所谓的依赖性 解耦性

"""

import time


# # 这样的形式就是装饰器
# def decorator(func):
#     def wrapper():
#         print(time.time())
#         func()
#
#     return wrapper


# 这样的形式就是我们称之为的装饰器
def decorator_one(func):  # 闭包
    def wrapper():
        print(time.time())
        func()

    return wrapper  # 这里返回的就是func传入的方法


def decoratt_two(func2):
    def wrapperr():
        print(time.time())
        func2()

    return wrapperr


def f1():
    print("this is function_one")


def f2():
    print("this is function2_two")


f4 = decoratt_two(f2)
f4()

print('*****-------******')

f = decorator_one(f1)
f()
