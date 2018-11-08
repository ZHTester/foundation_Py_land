"""
type object class 关系  - 理解python一切皆对象的关系
1  type 是有两种用法的 第一就是生成一个类 第二就是返回我们所想返回的数据类型
2  type是用来生成我们的类对象的
3  我们的类是由type这个类来生成的对象，我们平时所熟悉的对象他是由我们的类对象来创建的一个对象，type是用来生成类的
4  obj所有的类都需要继承的基础类
5  obj是最顶层的基类 所有的类推到最顶层的类都是obj类
6  type本身也是一个类，同时type也是一个对象
7  type-obj-type 也是个闭环的关系 互相生成互相 type继承了object 但是了object是type的实例，也就是type生成了obejct这个实例
8  type是创建了所有的对象 object = type()
9  list 是一个类也是一个对象因为他是被type创建出来的 这就是我们python一切对象的一个理念
10 类一旦创建，我们在吧这个类加载到内存中，实际上这个类是不能再被修改的，但是在python中我们把类变成对象这样的问题就可以很好的解决了
   因为对象我们可以随时修改
11 type也是自身的一个实例 但是type继承了object 这样就做到了一切皆对象的概念同时继承了object
12 相当于就是自己都是自己的对象，那么也即是一切皆对象了，所以其他成为type的对象，那么自己能把自己变为自己的对象，那么也就是
   python中所说的一切皆对象 一切都继承了object
13 我们需要深入的去理解一下python中一切皆对象是如何去做到的





"""
a = 1
b = 'abc'
# 1 实际上通过
'''
type->int->1
也就是说type可以生成我们的对象class，然后了class也可以生成我们的对象也就是obj

1实际上是通过 int这个类来生成的对象<class 'int'>
int本身也是一个对象，他是由type来生成的

**********
print(type(int)) -> <class 'type'>
'''
print(type(1))
print(type(int))

print(type(b))
print(type(str))


class Student:
    pass


class MyStudent(Student):
    pass


stu = Student()
print('-------student--------')
print(type(stu))
print(type(Student))
print('------int str--------')
"""
int str 等一些python内建函数都的基类都是object的，但是他是由type生成的 

"""
print(int.__bases__)
print(str.__bases__)
print('-------Mystudent-------')
"""
1 obj所有的类都需要继承的基础类  不去继承任何类那么他就会去继承obj的
2 obj是最顶层的基类 所有的类推到最顶层的类都是obj类

Student.__bases__ 基类 (<class 'object'>,)
MyStudent.__bases__ 基类 (<class '__main__.Student'>,)

"""
print(MyStudent.__bases__)
print(Student.__bases__)
print('------type-object-------')
"""
type本身也是一个类，但是他也是一个对象，type的基类本身也是obj
type.__bases__ 基类 (<class 'object'>,)

object.__bases__  的基类  为空 ()


"""
print(type.__bases__)
print(object.__bases__)
print('-----object---------')
"""
object的基类也是由type生成的
object - <class 'type'>
"""
print(type(object))
