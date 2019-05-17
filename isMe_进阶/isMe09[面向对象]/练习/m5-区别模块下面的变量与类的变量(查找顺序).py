# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/15  11:12'
"""
区别模块下面的变量与类下面的变量
1 局部变量是不会覆盖全局变量的在python中 - 这个就是模块的变量的概念
  ---> 我们在函数中定义了与全局变量相同名称的变量一致，那么的话局部变量是不会覆盖全局变量
2 类变量实例变量 查找顺序
3 实例变量--->类中变量--->继承类中---->继承类中实例变量---继承类中的类变量---->报错
4 类变量肯定是和类关联在一起的，实例变量是和对象关联在一起的
5 self实例变量的指代，但是self不是关键字指代
6 
"""


class StudentHomeWork:
    name = '类变量值'  # 类变量
    age = 0

    def __init__(self, name, age):
        self.name = name  # 实例变量
        self.age = age

    def do_homework(self):
        print("{}:在做作业".format(self.name))


if __name__ == "__main__":
    s = StudentHomeWork("实例变量值", 33)
    s1 = StudentHomeWork("实例变量值1", 33)
    print(s.name)  # 打印实例变量
    print(s1.name)  # 打印实例变量
    print(StudentHomeWork.name)  # 打印类变量
    print('--------------------------------')
    print(s.__dict__)  # 保存当前变量中的所有变量
    print('--------------------------------')
    s1.do_homework()
