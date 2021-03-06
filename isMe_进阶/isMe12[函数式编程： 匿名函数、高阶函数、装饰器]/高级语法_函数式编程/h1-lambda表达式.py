"""
lambda表达式

匿名函数 - 我们在定义一个函数的时候不需要去定义它的函数名称
在python中我们需要定义一个匿名函数我们需要一个关键字也就是lambda也是可以做为一个匿名函数

"""


# 非匿名函数
def add(x, y):
    return x + y  # 这里就能可以表达一个代码块也可以表达成一个表达式


# 匿名函数

f = lambda x, y: x + y  # 其中expression只能实现简单的表达式不能实现主要的代码块 不能是个代码块
# f1 = lambda x, y: a = x + y  # a = x + y 不是表达式是一个完成的代码语句了这样就会导致报错了


print(f(1, 2))
print(add(1, 2))
