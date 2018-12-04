"""
类变量与对象变量(实例变量)
1 类变量必须通过类来访问，有时候也是可以通过对象来访问 ......
2 类不能访问实例变量，不然就会报错 ....
3 类变量改变了，实例属性的变量也会跟着改变的 .....
4 a.aa =100 类下面的变量a=1是不会修改的，但是实例对象a.aa = 100 那么实际上实例属性就会多一个属性值a.aa=100
  这样的话他就会新建一个aa=100 放到我们的a实例属性值下面去 也就是aa=100 是a实例下面了实际上就含有2个值了，
  A.aa = 11 这样会修改类下面的属性

"""


class A:
    aa = 1  # 这个就是类变量

    def __init__(self, x, y):   # self <---> 也就是实例,也就是这个A对象的实例
        self.x = y
        self.y = y


a = A(4, 5)
A.aa = 11
a.aa = 100
print(a.x, a.y, a.aa)  # 实例对象来访问实例变量  类变量是需要通过类对象来访问的
print(A.aa)  # 类来访问类变量

# print(A.X)  # 这里是不会向下查找，自然会通过向上查找的方式进行查找，也就是通过继承关系 所以这里是会报错的






