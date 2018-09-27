"""
类的展现
1 我们在print的时候实际上就是在展现类，实际上print的时候，我们就是转换成了字符串

__str__
__repr__
__unicode__  适合机器看到额字符串

如果一个对象能被一个方法转换成字符串的话，那么就是定义了或者继承了父类的方法

展现类的属性
python的内建方法
__dir__ 如果有时候我们不想展现对于的属性，我们就可以从新定义这个__dir__的方法



"""


class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception("age must be int")

    def __str__(self):
        return "%s is %s years old" % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()   # 属性的键返回


if __name__ == '__main__':
    p = Programer('landing', 44)
    print(p)
    print(dir(p))
