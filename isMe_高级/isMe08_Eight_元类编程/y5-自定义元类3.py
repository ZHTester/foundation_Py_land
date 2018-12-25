"""
1 元类就是创建类的类，type就是创建类的类 也即是元类，对象<-class<-type
2 *type-其实这个东西他就是元类*

"""

"""
1 这里继承了type其实他就是一个元类 -> 元类就是控制对象的一个生成过程 
  这个类的创建其实就是为了控制User这个类实例化的一个过程-> 这个就要说道
  Python中实例化的过程了, 如果不去继承这样的属性以及方法 metaclass=MetaClass
  他就会自动去调用我们的这个type这个元类的,type就会去创建这个类对象也就是类，也就是实例,也就是 class User

2 如果说有这个metaclass=MetaClass 这个属性就不一样了，他们就会首先去寻找metaclass=MetaClass
  这个属性，如果找到了他就会去调用这个MetaClass这个元类，去实例化我们的User，然后通过MetaClass去
  创建我们的User类。---> 当然如果我们本身的类中没有metaclass，那么Python会自动去基类中去需要metaclass
  这样的一个属性，如果基类中含有metaclass那么他就回去调用这个基类的metaclass去创建我们的User，如果基类找不到
  那么就回去模块中选择这样的一个metaclass，如果都找不到Python才回去调用我们这个type去创建我们的这个User这样的一个
  对象，这个就是Python中控制类对象生成的一个过程

3 User = type("User", (BaseClass,), {"name": "landing","say": say})  # 这样也是创建了一个类
  其中cls 是type中的"User", 其中*args 是type中的tupe(继承的基类)，dict自然就是属性了kwargs
  
4 如果说某些基类没实现某些方法，那么我们在实现它的时候，就应该抛出异常
"""


class MetaClass(type):
    # 这样就将生成对象的过程委托给type也就是父类来进行了
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
    print("这就是我的_new_")


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


if __name__ == "__main__":
    my_obj = User("landing")
    """
    # 这样就生成了obj的实例<--->这里在调用这个类的时候，因为我们已经重载了Str自然就有函数的打印了
    # 这样就就是字符串的表现形式
    """
    print(my_obj)
