"""
嵌套函数
是在一个函数函数体中用def申明一个新的函数，这就叫做函数的嵌套。


"""

"""
全部变量 局部变量

嵌套函数
"""


def foo():
    print('in the foo')

    def bar():  # 具备局部变量的作用
        print('in the bar')

    bar()


foo()


# 局部作用域和全局作用域的访问顺序
# 作用域从里往外开始一层一层的执行

# x=0
# def grandpa():
#     x=1
#     def dad():
#         x=2
#         def son():
#             x=3
#             print x
#         son()
#     dad()
# grandpa()










