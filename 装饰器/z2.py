# """
# python 闭包
#
# 1 闭包  closure 内部函数对enclosing作用域变量进行引用 这样的函数就称之为闭包
#
# 2 函数实质和属性
# 1 函数是一个对象
# 2 函数执行完成后内部变量回收
# 3 函数属性
# 4 函数返回值
#
# 闭包的作用:
#
#
#
#
# """
#
# # passline = 60  # 全局变量
#
#
# def func_150(val):  # local
#     passline  = 90
#     # print('%x' %id(val))
#     if val >= passline:
#         print('%d pass'% val)
#
#     else:
#         print('failed')
#
# def func_100(val):  # local
#     passline = 60
#     # print('%x' % id(val))
#     if val >= passline:
#         print('%d pass'% val)
#
#     else:
#         print('failed')
#
#
#     # def in_func():  # 也就是在运行in_fun的时候，我们就去会去函数属性中去查找 (val,)
#     #     print(val)  # 在in_func() 中没有val那么我们就向上方法查找变量 这就是闭包
#
#     # """
#     # 如果说我们引用了外部函数的作用域的话，那么我们就会将外部函数的属性
#     # 添加到函数属性中，然后我们再次去查找的时候，并不是去函数中去查找，
#     # 而是去函数的属性中查找，查找完成后我们就会打印出来，也就是把相关的值也打印出来
#     #
#     #
#     # """
#     # in_func()  # 在函数的内部中调用
#     # return in_func  # in_func 函数内部返回的函数
#
#
# # f = func(89) # 当这个函数运行完成后，其实就没有了内存变量计数器了
# #
# # f() # in_func
# # print(f.__closure__)  #
#
# func_100(89)
# func_150(89)
#
#
#

"""
闭包就是对外包函数的一个作用域的使用

1 闭包的作用
  封装
  代码的复用性

"""


def set_passlint(passline):  # 60
    def cmp(val):  # 内部函数就是在使用外部的方法变量 passline 这就是cmp的一个闭包
        if val >= passline:
            print('pass')
        else:
            print('failed')

    return cmp  # 直接返回


f_100 = set_passlint(60)
print(type(f_100))
print(f_100.__closure__)
f_100(100)
f_100(22)

打印测试数据打印测试数据