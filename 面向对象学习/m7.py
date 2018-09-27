"""
python的 magic method 方法

    1magic method 长什么样子
     方法名称前后有两个下划线
     def __init__(self):

1 对象的创建和初始化
  1 常用类的定义
  class person(object):
    def __init__(self,name,age)
        self.name = name
        self.age = age

person  =  Person("landing", 25)

2 对象的实例化的过程

创建类的对象-------------》 初始化对象
def __new__(cls):          def __init__(self):


3 回收对象
1 首先python是有垃圾回收机制的，并不需要我们手动的去回收垃圾的
2 当一个python的对象回收的时候，python就会去调用__del__()

__del__()

"""
"""
构造函数实例化的过程

"""
class Programer(object):
    def __new__(cls, *args, **kwargs):
        print('all __new__method')
        print(args)
        return super(Programer,cls).__new__(cls,*args,**kwargs)

    def __init__(self,name,age):
        print('call __init__method')
        self.name = name
        self.age = age

if __name__ == '__main__':
    pro = Programer('landing',44)
    print(pro.__dict__)



















