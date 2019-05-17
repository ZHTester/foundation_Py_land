# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/15  10:05'
"""
1 类是一系列事物的统称 
2 行为与特征，行为没找对主体 --- 这也是导致面向对象不合格的
3 类就是一个模板，通过这个模板可以产生很多个对象的 ，我们通过类的实例就是可以生成
  不同的实例通过模板可以生成不同的实例，实例的话只是成员变量的不同而已。



"""


class Student:
    name = ''
    age = 0

    def doHomework(self):
        print("做作业")

    def print_file(self):  # 打印档案
        print('name:' + self.name)
        print('age:' + str(self.age))


if __name__ == "__main__":
    student = Student()  # 类和对象的关系就是通过实例化来关联在一起的
    student.print_file()
