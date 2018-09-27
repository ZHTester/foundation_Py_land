"""
1 类与运算符  魔术方法

2 比较运算符
__cmp__ (self,other)
__eq__ (self,other)
__it__(self,other)
__gt__(self,other)

3 数字运算符
__add__(self,other)
__sub__(self,other)
__mul__(self,other)
__div__(self,other)


4 逻辑运算符
__or__(self,other)
__and__(self,other)




"""


# s = 'test'
# print(s == s)
# print(dir(s))

class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception("age must be int")

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('the type of object must be Programer')

    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programer')


if __name__ == '__main__':
    pro1 = Programer('landing', 33)
    pro2 = Programer('tom', 33)
    print(pro1 == pro2)
    print(pro1 + pro2)
