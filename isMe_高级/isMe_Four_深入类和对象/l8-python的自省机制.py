"""
python 自省机制

1 是通过一定的机制查询到对象的内部结构  （也就是通过__dict__来访问到了这样的一个数据内部结构）。
2 dict在我们的Python当中是用C语言实现的而且他的效率很高。
3 dir是要比dict函数更加的强大，列出的功能函数更加的全面
"""


class Person:
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.schoole_name = school_name


if __name__ == "__main__":
    user = Student("建国长城")
    """
    这样打印__dict__ 那么他就会自动去找到我们
    user这个实例的属性，也就是叫为实例属性
    
    """
    print(user.__dict__)

    """
    动态操作我们user对象的一个过程
    
    """
    user.__dict__['schoole_addr'] = "北京市"
    print(user.schoole_addr)  # 但是实际上我们是不会这样来引用的
    """
    类比我们的实例更加的丰富所以的类的属性值要比对象的多
    
    """
    print(Person.__dict__)
    print(user.name)  # 这里就会向上查找 也就是通过继承的关系去查找的

    """
    1 dir 的使用方式也是列出对应的属性
    2 dir列出的只有属性的名称，是没有属性的值的
    3 
    
    """
    print(dir(user))
    """
    内置函数与方法，我们通过__dict__这样的方式是无法访问的
    但是我们通过dir是可以访问我们内置函数中的一些数据结构
    
    """
    a = [1,2]
    # print(a.__dict__)
    print('--------dir()--------')
    print(dir(a))
    print('------__dir__---------')
    print(a.__dir__())









