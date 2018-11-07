"""
区别模块下面的变量与类下面的变量
1 局部变量是不会覆盖全局变量的在python中 - 这个就是模块的变量的概念
2 模块的变量与类的变量机制是不一样的

3 类变量与实例变量 理解这两个变量对于我们理解面向对象是十分重要的
4 所谓的类变量就是和类相关的变量
5 实例变量就是和对象相关联在一起的
6 self不能称之为关键字
7 实例变量与类变量 之间有什么不同了 。。。。
8 类变量是和具体的对象是没有关的 包括啥属性了啥方法了
9
"""


class StudentHomework:
    """
    在类下面的变量也就是我们所说的类变量
    """
    '-----------'
    sum = 0  # 一个班级的所有学生的总数
    # name = 'bayue'
    # age = 0
    # 构造函数
    """
    1 构造函数是自动进行的，当你在实例化的过程中，python就自动的调用了构造函数
    2 构造函数就是初始化类的特征值 ，初始化对象的属性
    3 paython中构造函数中左边的值代表是定义的变量，右边的值代表是传入的参数
    4 使用self来报错类的特征值的
    """

    def __init__(self, name, age):
        """
        这就是定义实例变量的一个方法 和对象有关和类没关系
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def do_homework(self):
        print('home_work')


"""
不同的特征值来表示，也就是实例变量
"""
student = StudentHomework('北京大人', 28)
student1 = StudentHomework('石敢当', 19)
'''

'''
print(student.name)  # 直接去调用方法下面的属性
print(student1.name)
print(StudentHomework.name)  # 对于类而言类的变量只和类相关，他不受对象的影响
