"""
实现装饰器的知识储备
1 函数也就是变量
2 高阶函数
3 嵌套函数 - 函数的嵌套
4 高阶函数+嵌套函数 = 装饰器


"""
"""
这一段是没有定义bar 所以会报错
"""
# def foo():
#     print('in the foo')
#     bar()
# foo()


"""
在foo(） 上面定义了bar代码 所以不会报错
"""

# def bar():
#     print('in the bar')
#
#
# def foo():
#     print('in the foo')
#     bar()
# foo()


# def foo():
#     print('in the foo')
#     bar()
#
#
# def bar():
#     print('in the bar')
#
#
# foo()

# def foo():
#     print('in the foo')
#     bar()
#
# foo()
#
#
# def bar():
#     print('in the bar')

# 匿名函数  函数也就是变量 匿名函数就是没有函数名
# 函数 与 变量的内存回收机制是一样的
# calc = lambda x: x * 3
# print(calc(3))
