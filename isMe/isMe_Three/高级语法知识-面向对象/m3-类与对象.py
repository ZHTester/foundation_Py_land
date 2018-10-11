"""
类与对象
1 类和对象最直接的关系就是通过实例化来关联起来的
2 类就是现实世界与思维世界中实体在计算机的一个反应，
  他将数据与数据之上的一些封操作装在了一起
3 所以说类就是一类事物的总称
4 如何表示具体的了就是对象要做的事情了 对象就是具体的对象
5 实例化我们就需要具体的传入实际的年级或者啥
6 类相当于就是一个应刷机，通过类你就可以做出各种各样的对象的
7 所谓不同的对象就是说 name 和age不相同的同一个类下面的对象 因为他
8 通过模板生成不同对象的一个过程就是实例化的一个过程 ~
"""


class StudentHomework:
    name = ''
    age = 0

    def do_homework(self):
        print('home_work')


# class Printer:
#     # 能做什么事情了-就是行为-行为就是方法
#     # 行为与特征
#     # 行为的主体是什么 行为没找到主体
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))


if __name__ == '__main__':
    # 实例化类
    student = StudentHomework()
    student.print_file()  # 调用类下面的方法
