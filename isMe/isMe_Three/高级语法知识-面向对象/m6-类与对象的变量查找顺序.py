"""
类与变量的查找顺序
1 动态语言的坑就是，如果你对一些机制理解不是很深刻那么就很容易出现很多坑的
2 python 去寻找变量的一个机制
3 如果我们要去访问一个实例变量，那么python会在类中的实例变量列表中去查找
  是否含有这样的一个实例变量列表，如果没有这样的一个实例变量的值，那么python不会返回我们
  这样的一个None，python会继续到类变量中的这样一个类变量列表中去寻找，这就是为什么当我们使用
  对象去访问实例变量的时候，我们返回的是类变量中的值，因为实例变量中没有值，那么就会去实例变量中
  去寻找，在类变量中找到了，那么就会返回出来了，如果是类变量中那么就会去类的父类中去寻找，如果还是
  没有这样的一个形式，那么就会报错为定义的变量

4

"""


class StudentHomework:
    name = 'bayue'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        """
        这就是定义实例变量的一个方法 和对象有关和类没关系
        :param name:
        :param age:
        """
        name = name
        age = age

    def do_homework(self):
        print('home_work')


"""
不同的特征值来表示，也就是实例变量
"""
student = StudentHomework('北京大人', 28)
print(student.name)  # 这里直接打印的是类的变量而不是我们预期的实例变量
print(student.__dict__) # 查看对象下面的变量 __dict__
print(StudentHomework.__dict__)
