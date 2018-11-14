"""
super真的调用了父类吗？
1 super本身是调用了父类的构造函数，但是这样的说法本身是不够准确的，
2 那么super的执行顺序是什么


"""
from threading import Thread


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()

# 既然我们重写了B的构造函数，那么我们为啥还有去调用super构造函数
# Super - 执行顺序到底是什么样的 ？
# Super -


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        """
        在这里我们就不需要去重写name了，因为我们本身的类都继承了这个Thread的
        那么Thread中的__init__构造函数中就已经存在了name这个属性，那么我们
        就直接继承父类的构造函数，重写构造函数的属性就可以了，这样我们就重用了
        代码了
        
        """
        super().__init__(name=name)


if __name__ == "__main__":
    b = B()










