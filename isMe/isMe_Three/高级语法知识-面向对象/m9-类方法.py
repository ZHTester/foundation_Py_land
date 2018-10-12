"""
类方法

1 实例变量通常是用来操作实例方法的
2 但是了类变量也有操作实例方法的一个变量符号 这个方法就是类方法
3 类方法与实例方法的区别 - 区别就是类与对象的一个区别
  1 实例方法所关联的是我们的对象
  2 类方法所关联的是我们类本身
  3 如果你想操作和实例对象本身无关的对象最正确的方式还是操作类方法中的类变量
  4
4 我们可以使用类来调用一个类方法我们也可以使用一个对象来调用这个类的实例方法
5 在逻辑上是不要使用一个对象来去调用类方法
"""


class Student(object):
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print("当前班级的人数:"+ str(self.__class__.sum))

    # 实例方法
    def do_homeWork(self):
        print("homework")

    # 类方法  其中就是cls  其中类方法就是用来操作与类相关的变量
    @classmethod
    def pls_sum(cls):  # 类方法 默认的参数cls
        cls.sum += 1
        print("班级的人数"+str(cls.sum))


student = Student("石敢当", 33)
student1 = Student("石敢当", 33)
Student.pls_sum()  # 类方法直接调用类方法
