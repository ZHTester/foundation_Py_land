"""
1 Python的数据封装以及私有属性
2 私有属性在Python中还是能访问这样的数据了
3 这样的方式是我们对做python语言中的一种规范而已，其实Python中的私有属性还是可以访问的
4 python这样的私有属性的访问方式同样也是继承了我们 同样变量的一种冲突的问题
5 selef.__birthday
6 user._Student.birthday 同样变量名访问冲突的问题


这一节课主要关注7月老师的讲解课程

"""
from isMe_高级.isMe_Four_深入类和对象.类方法_静态方法_实例方法 import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday  # 私有属性双下划线

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == "__main__":
    user = User(Date(2000, 1, 1))
    print(user.get_age())


















