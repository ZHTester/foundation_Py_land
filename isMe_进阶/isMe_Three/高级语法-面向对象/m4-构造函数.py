"""
1 构造函数 构造对象 初始化对象方法 与一些属性
2 实例化与实例化的意义在于什么了
3 调用构造函数的返回结果是什么了 - 显式调用 对象.__init___ 默认返回的None-但是在实际项目中没有这样的调用方式
4 init 函数是不能返回除开none之外的任意的值的
5 python函数中的None只能返回None之内的变量内省
6 构造函数的作用不是为了去返回某个值 初始化对象的方法 与一些属性
7 构造函数的作用就是让你的类生成不同的对象 初始化对象的属性
"""


class StudentHomework:
    # 构造函数
    """
    1 构造函数是自动进行的，当你在实例化的过程中，python就自动的调用了构造函数
    2 构造函数就是初始化类的特征值 ，初始化对象的属性
    3 paython中构造函数中左边的值代表是定义的变量，右边的值代表是传入的参数
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("student")

    def do_homework(self):
        print('home_work')


# class Printer:
#     # 能做什么事情了-就是行为-行为就是方法
#     # 行为与特征
#     # 行为的主体是什么 行为没找到主体
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))


# 实例化类 实例化这三个对象是一样的 他们的特征是相同的 name age
# 但是在内存中的地址是不相同的，说明在计算机是不相同的 但是在现实世界上是相同的，这也就是现实世界刻画在计算机世界的一个概念
# 下面的过程在调用构造函数是三次

student1 = StudentHomework('北京大人', 28)
# print(student1.name)  # 直接去调用方法下面的属性
# pass

student2 = StudentHomework('北京大人1', 28)
student1.do_homework()
# print(student1.name)

# a = student2.__init__()  # 在实际的调用过程中是不存在这样的一个调度方式的
# print(a)
# print(type(a))


# student.print_file()  # 调用类下面
