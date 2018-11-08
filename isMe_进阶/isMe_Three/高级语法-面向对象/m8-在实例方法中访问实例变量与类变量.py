"""
在实例方法中访问实例变量与类变量

1 如何在实例方法的内部去访问类变量？
  2 访问实例变量需要加上self.变量名称
2 在实例方法中如何去访问类变量了
3 在类的外部使用类名称.类变量名称
  在类的内部也是使用类名称.类变量名称

"""


class StudentHomework:
    sum1 = 0
    name = 'bayue'
    age = 0

    # 构造函数可以看做特殊的实例方法 只是和其他的实例方法调用的方式是不一样的
    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        print('__init__:', self.name)  # 这里读取的是实例变量
        print(self.__class__.sum1)  # 在实例方法中直接访问类变量是会报错的
        # print('class name', name) # 这里读取的是形参Name并不是实例变量

    def do_homework(self):
        print('home_work', self.name)  # 操作实例方法


"""
不同的特征值来表示，也就是实例变量
"""
student = StudentHomework('北京大人', 28)
print(student.name)  # 这里直接打印的是类的变量而不是我们预期的实例变量
student.do_homework()  # 其中do_homeword中的self就是指student
