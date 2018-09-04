"""
1 多继承的区别
2 多继承继承了第一个类中的构造函数，就不会继承第二个类中的构造函数
3 广度优先查询方式
"""


class A:
    def __int__(self):
        print("A")


class B(A):
    def __int__(self):
        print("B")


class C(A):
    def __int__(self):
        print("C")


class D(B, C):
    pass


obj = D()



