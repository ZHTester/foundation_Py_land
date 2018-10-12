"""
self与实例方法

1 如果我们在一个类的下面需要去定义一个实例方法，那么我们就需要在方法的参数列表中第一个参数固定放入一个self
  当我们调用实例方法的时候，我们是不需要传入这样的一个self，self是类为我们的实例方法固定传入的，我们是不需要
  为实例方法传入self的

2 this或者是self 都是可以指定实例变量的
3 self就是当前调用某个方法的对象
4 self之和对象有关和类是没有关系的
5 谁调用了他的方法，那么self就是指代那个谁的对象，换句话来说self代表的是实例而不是类
6 实例可以调用的方法就叫做实例方法，最大的特点就是第一个参数必须传入一个self

"""


class StudentHomework:
    name = 'bayue'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        """
        这就是定义实例变量的一个方法 和对象有关和类没关系
        self.name = name self.name 也就对象的属性 = name 我们传入的值的name赋值给对象的值
        :param name:
        :param age:
        """
        self.name = name
        self.age = age
        print(name)
        print(age)

    def do_homework(self):
        print('home_work')


"""
不同的特征值来表示，也就是实例变量
"""
student = StudentHomework('北京大人', 28)
print(student.name)  # 这里直接打印的是类的变量而不是我们预期的实例变量
student.do_homework()  # 其中do_homeword中的self就是指student
