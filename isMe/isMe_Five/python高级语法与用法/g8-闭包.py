"""

1 闭包是有一个函数在定义时候外部一个环境变量所构成的一个整体，我们称之为闭包，
如果形成了闭包，那么在函数调用的时候，函数是不会受到其他模块或者或者说是全局变量下的影响
2 闭包 = 函数+环境变量(函数定义的时候一个外部的局部变量，但是他不能是一个全局变量)
  构成了这样的一个闭包，其中环境变量一定是要在函数的外部，如果环境变量定义成了内部函数那么
  这样的函数就不能称之为闭包了，还有就是这个环境变量也不能称之为全局变量，必须是局部变量

闭包的意义，意义的所在就是保存了一个环境变量，把函数当时调用的一个现场保存起来了，如果单纯的是函数的调用，那么就很容易
受到其他环境变量的影响
"""


def cure_pre():
    a = 25

    def cure(x):
        return a * x * x  # print("this is function")

    return cure  # 作为结果返回来，其实实际上是返回了一个闭包并不是一个函数


def cure_pre1():  # 这样的话我们就形成了2个闭包
    a = 25

    def cure(x):
        return a * x * x  # print("this is function")

    return cure  # 作为结果返回来，其实实际上是返回了一个闭包并不是一个函数

a = 10
f = cure_pre()
print(f(2))  # 实质上就是在调用f(2) == cure(2)等价的一个调用关系 这样的一个函数
