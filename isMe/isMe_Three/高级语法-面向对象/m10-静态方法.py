"""
静态方法

1 一个类或者是一个对象都是可以调用静态方法的
2 类方法与静态方法是否能访问我们的实例变量了,答案是不能的 这个就是报错变量没定义
3 静态方法有什么用，你能使用静态方法的地方都可以使用类方法来代替，而且类方法更加方便点
  使用类方法我们需要使用cls.类变量，但是使用静态方法我们需要使用类名.类变量
4 和类和对象都没有什么关系的时候就可以使用静态方法
"""


class Student(object):
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print("当前班级的人数:" + str(self.__class__.sum))

    # 实例方法
    def do_homeWork(self):
        print("homework")

    # 类方法  其中就是cls  其中类方法就是用来操作与类相关的变量
    @classmethod
    def pls_sum(cls):  # 类方法 默认的参数cls
        cls.sum += 1
        # print(self.name) 不能调用实例方法中的变量
        print("班级的人数" + str(cls.sum))

    # 静态方法
    @staticmethod
    def add(x, y):
        # print(self.name) 不能调用实例方法中的变量
        print(Student.sum)  # 静态方法的内部也是可以访问我们的类变量的
        print("this is a staticmethod")


student = Student("石敢当", 33)
student1 = Student("石敢当", 33)
Student.pls_sum()  # 类方法直接调用类方法
Student.add(2, 3)
student1.add(3, 4)
