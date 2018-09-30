"""
函数的 LEGB
local 函数的作用域
enclosing 函数内部内嵌函数之间  这个时候我们就称之为闭包
global 全局作用域
build-in 内置函数的作用域

函数查找的顺序也是依据上面的作用域来操作的 。。。。
作用域就是向上查找的一个过程

"""
passline = 60  # 全局变量


def func(val):  # local
    passline = 90  # 局部变量
    if val >= passline:
        print('pass')

    else:
        print('failed')

    def in_func():
        print(val)  # 在in_func() 中没有val那么我们就向上方法查找变量 这就是闭包

    in_func()  # 在函数的内部中调用


def Max(vu1, vue2):
    return max(vu1, vue2)


func(89)
print(Max(90, 200))
