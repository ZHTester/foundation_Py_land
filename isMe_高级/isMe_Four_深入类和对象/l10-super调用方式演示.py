"""
Super本身不是调用父类的构造函数，而是调用MRO算法下一个的构造函数 不是本身的一个继承关系


"""


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == "__main__":
    print(D.__mro__)  # 展示D的一个调用顺序
    d = D()











