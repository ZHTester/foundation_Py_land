"""
编程中的开闭原则....
继承
单继承
    1 继承性的作用  1 避免我们定义重复的方法与重复的变量
    2 学生人之间就构成了一个继承的关系
    3 子类继承父类中的变量
    4 如果子类没有构造函数那么就应该继承父类里面的构造函数 如果在子类创建对象就会报错，因为继承了
      父类的构造函数那么也就继承了父类里面的一切属性包括了构造函数的属性
    5 父类的实例变量也是可以被我们子类所继承的
    6 如果子类全部都是继承于父类那么我这样的集成是没有任何意义的，所以说子类通常都是需要有自己的一些变量的
    7 子类的方法和父类的方法同名称 这样的编写方式是允许的
    8 如果子类的方法和父类的方法同名那么python并不会报错，但是子类的方法会重写父类的方法，并且打印子类的方法
      python会打印子类的方法
python中是允许多继承   一个子类可以继承多个父类

不给构造函数 类默认给一个无参的构造函数
"""


# from .m13-继承 import People
# from isMe.isMe_Three.高级语法-面向对象.m13 import Human

class Human:
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_home_work(self):
        print("这是一个父亲的方法")


class Student(Human):  # 继承
    # sum = 0
    #
    def __init__(self, schoole, name, age):
        """
        # 继承与父类 在子类中调用父类的构造函数 所以父类的构造函数也会得到初始化,在这里就是显示的调用
        一个类去调用实例方法 本身从严格意义上来说就是不正确的
        这里就是一个普通方法的调用 所以就需要传入一个self

        """
        # Human.__init__(self,name, age)
        super().__init__(name, age)
        self.schoole = schoole

    def do_home_work(self):
        # super().do_home_work()  # 调用父类的方法 super可以调用构造函数 也是可以调用子类的普通的方法
        print("这是儿子的方法")


student = Student("北京大学", "北京", 22)
print(Student.sum)  # 子类继承父类里面的特征 变量
print(student.sum)
print(student.name)
student.get_name()  # 调用父类的方法
print(student.age)
print(student.schoole)
student.do_home_work()

