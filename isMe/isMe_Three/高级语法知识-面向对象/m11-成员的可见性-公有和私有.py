"""
成员的可见性 共有和私有
1 成员我们可以简单的理解成变量和方法  - 方法和变量的可见性
2 类的内部和类的外部
3 方法有内部调用和外部调用的区别 - 外部调用的区别就是使用对象去调用类的内部的函数
                             内部调用就是在类的内部的函数去调用类的内部函数
4 类变量与实例变量都存在内外调用的一个方式
5 通过外部调用内部的函数或者说是变量那么这样就会导致我们类内部的封装的数据不安全性 造成数据的不安全性
6 通过方法来对变量进行一个修改比通过对变量进行数据修改是安全了很多的，通过方法是可以判断
7 有什么办法使不让人对类的变量在外部进行一个赋值改变了 或者是读取操作
8 变量的可见性也就是public  所以可以赋值和读取 ---
  私有的变量可见性private  -- 如果是私有的那么我们就无法在外部进行读取和修改
9 如何吧变量或者方法修改成一个私有的变量或者方法了？
  在方法或者变量加上了双下划线 那么这个变量或者方法都变为私有的 __socre 这样就是变成了私有变量


没有什么是不能访问的:
    1 私有变量在类的外部进行改变为啥不会报错了
    2 严格意义上来说python是没有这个私有变量的


"""


class Student(object):
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1
        print("当前班级的人数:" + str(self.__class__.sum))

    def marking(self, score):
        if score <= 0:
            return "不能够给别人打负分"
        self.__score = score
        print(self.name + "本次考试负分数为:" + str(score))

    # 实例方法
    def do_homeWork(self):
        self.do_homeWork()  # 在类的内部调用类的函数
        print("homework")

    def do_english(self):
        """
        在类函数中的中的函数去调用函数这样的调用方式
        就叫做在类的内部函数内调用函数
        :return:
        """
        print('doEnglish')

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


student1 = Student("石敢当", 33)
a = student1.marking(99)  # 对私有方法进行调用那么会报错
print(a)
"""
在这里设置的私有变量与读取都是生效了的？
1 由于python动态语言的机制，其实这这里设置的__score是新添加了一个实例变量
2 python可以通过对象.变量(student1.__score)来添加一个新的实例变量的

"""
student1.__score = 1  # 对私有变量不会报错
"""
{'name': '小诺', 'age': 55, '_Student__score': 0  --- 这里就是原有的
__score 名称都修改了 所以我们去访问私有变量就会报错 因为我们找不到这样的一个名称了
所以我们不能通过动态的方式来进行读取或者修改私有变量的 }
"""
print(student1.__score)  # 这里有一个强行复制的一个操作 这里的score并不是构造函数中的score
"""
{'name': '石敢当', 'age': 33, '_Student__score': 99, '__score': 1}
_Student__score 就是类本身愿挨的变量
__score 就是动态语言的特性 新生成的__score
"""
print(student1.__dict__)

student2 = Student("小诺", 55)
print(student2.__dict__)
# print(student2.__score)  # 在这里他就会报错 为什么会报错了，因为python已经把私有变量的名称修改了自然就是找不到了
"""
但是我们可以通过间接的方式来读取这样的私有变量
student2._Student__score 访问这样的一个私有变量的方式
"""
print(student2._Student__score)
