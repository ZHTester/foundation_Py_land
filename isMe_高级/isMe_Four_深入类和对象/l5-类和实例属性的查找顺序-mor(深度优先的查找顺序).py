"""
深度优先的查找顺序

"""


class D:
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
