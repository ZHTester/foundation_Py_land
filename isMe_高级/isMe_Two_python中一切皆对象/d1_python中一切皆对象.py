"""
一切皆对象

  还有就是python函数和类也是一个对象，其中他就是可以
  1赋值给一个变量
  2可以添加到集合对象中
  3可以作为参数传递个函数4
  4可以当做函数的返回值(装饰器的概念与使用-一个函数可以返回另外一个函数)

"""


# 函数对象赋值给变量
def f(name):
    print(name)


fun = f
fun("landing")


# 类也是对象
class Person:
    def __init__(self):
        print("landing_two")


my_class = Person
my_class()

# 对象可以添加到集合中
obj_list = []
obj_list.append(f)
obj_list.append(Person)

for item in obj_list:
    print(item)














