"""
自定义元类
1 首先类也是对象，type创建类的类

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


# 通过type() 动态创建类  # 其实也是可以创建一类的 我们可以通过源码的方式来进行查看
"""
我们现在就通过type来创建一个类，其中第一个参数就是我们要创建类对象的名称，第二属性就是我们要创建这个类
要继承的基类，如果不填写这个tuple那么默认就是继承的obj，第三个参数就是这个类的属性dict
"""
User = type("User", (), {"name": "landing"})  # 这样也是创建了一个类

if __name__ == "__main__":
    """
    这样我们就可以通过函数，和一个变量，动态的去获取一个类，这样在我们java中是十分的困难的
    但是在我们的java中是十分简单的，但是这样创建类的方式还是相对于复杂了，我们还是可以不需要写
    class这样的赋值语句的
    """
    # myClass = create_class("user")  # myClass 其实就是user这个类，这个类我们是可以用来生成实例的
    # my_obj = myClass()  # 调用这个类 这个实例my_obj<--->其实是user类型的
    # print(type(my_obj))  # 这里就获取到了这个my_obj这个类型的 <class '__main__.create_class.<locals>.User'>

    User = type("User", (), {"name": "landing"})  # 这样也是创建了一个类
    my_obj = User()
    print(type(my_obj))  # <class '__main__.User'> 这个类最要是在main函数下的
    print(my_obj.name)  # 这样就可以访问这个类下面的属性


    pass
