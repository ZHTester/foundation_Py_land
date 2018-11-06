"""
装饰器2  - 装饰器只是一种模式

1 体现对函数的功能的增加不是修改函数的本身
2 体现函数之间的关联性 并没有所谓的依赖性
3
"""

import time


# 这样的形式就是装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


def f1():
    print("this is function")


f = decorator(f1)
f()
