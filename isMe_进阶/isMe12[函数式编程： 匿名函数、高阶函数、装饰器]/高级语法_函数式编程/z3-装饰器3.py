"""
装饰器3
@ 符号装饰器
1 装饰器我们接受定义时候的复制，只要在我们调用的时候足够简单就可以了 ~
2 装饰器的又是就是不需要去修改我们本身的一种调用方式，原来的调用是什么就在调用的时候是什么，
  这个就是装饰器最大的优势
3 语法糖其实就是一种模式
4 高级的语法都是有助于我们写出更加优质的代码

"""

import time


# 这样的形式就是装饰器  这就是装饰器的原型
def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


def decor(func1):
    def wr():
        print("这是我的内部函数中的函数你知道吗")
        func1()

    return wr


@decor
def t1():
    print("我就是t1")


t1()

print('*******-----1------*******')

# 这样就是为我们的f1添加了新的功能 装饰器的核心点就是这个
# 也就是装饰器的核心点 只有这样的一个@才能保证我们的装饰器是不会被破坏的
@decorator
def f1():
    print("this is function")


@decorator
def f2():
    print('this is function2')


f1()  # 未改变函数原来所调用的方式 保持原有函数的调用方式不变，这就是函数调用的意义所在与优势
print('---------------------------------------')
f2()