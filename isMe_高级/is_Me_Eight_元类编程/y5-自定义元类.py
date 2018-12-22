"""
自定义元类
1 首先类也是对象，type创建类的类
2 类的本身也就是一个对象
3 也就是动态创建类

"""

# 这样我们就可以通过一个函数的传递动态的创建一个类


def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User  # 返回一个类对象，类对象实际上也是一个类

    elif name == "company":
        class Company:
            def __str__(self):
                return "company"  # 返回一个类对象，类对象实际上也是一个类
        return Company


if __name__ == "__main__":
    """
    这样我们就可以通过函数，和一个变量，动态的去获取一个类，这样在我们java中是十分的困难的
    但是在我们的java中是十分简单的，
    """
    myClass = create_class("user")  # myClass 其实就是user这个类，这个类我们是可以用来生成实例的
    my_obj = myClass()  # 调用这个类 这个实例my_obj<--->其实是user类型的
    print(my_obj)  # 这里就会打印出一个user  这个实际上的类就是User这样的一个类
    pass


































