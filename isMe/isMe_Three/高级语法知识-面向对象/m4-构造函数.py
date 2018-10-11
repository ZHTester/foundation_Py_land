"""
1 构造函数
2 实例化与实例化的意义在于什么了
3 调用构造函数的返回结果是什么了 - 显式调用
4 init 函数是不能返回除开none之外的任意的值的
5 python函数中的None只能返回None之内的变量内省
6 构造函数的作用不是为了去返回某个值
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
# 但是在内存中的地址是不相同的，说明在计算机是不相同的
# 下面的过程在调用构造函数是三次

student = StudentHomework('北京大人', 28)
print(student.name)  # 直接去调用方法下面的属性

# a = student2.__init__()
# print(a)
# print(type(a))


# student.print_file()  # 调用类下面
