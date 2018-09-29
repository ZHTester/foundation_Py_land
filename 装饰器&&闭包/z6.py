"""
1 内置函数装饰器
内置的装饰器和普通的装饰器原理是一样的，只不过返回的不是函数，而是类对象，所以更难理解一些。

属性有三个装饰器：setter, getter, deleter ，都是在property()的基础上做了一些封装，
因为setter和deleter是property()的第二和第三个参数，不能直接套用@语法。
getter装饰器和不带getter的属性装饰器效果是一样的，估计只是为了凑数，
本身没有任何存在的意义。经过@property装饰过的函数返回的不再是一个函数，
而是一个property对象。
------------------------------------------------------
@property
def x(self): ...

# 等同于

def x(self): ...
x = property(x)
------------------------------------------------------

"""


def getx(self):
    return self._x


def setx(self, value):
    self._x = value


def delx(self):
    del self._x


# create a property  创建属性
x = property(getx, setx, delx, "I am doc for x property")
print(x)  # 返回的是property对象
