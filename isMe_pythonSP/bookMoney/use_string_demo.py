# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/6  14:56'
"""
使用优雅的字符串

1 使用%来格式化字符串 
2 使用format来格式化字符串 高级的使用方式

"""


def format_str():
    name = "我是你大爷"
    print("你是我的谁=%s" % name)

    # 保留3位小数
    num = 54.33
    print("你输入的数字是%.3f" % num)


def format_str2():
    # 位置取值方式 format
    print("你的位置是,{0}{1} -----{0}".format("张三", "好久不见"))
    name = "大锅"
    print("你的姓名:{username} 你的编号是:{num}".format(username=name, num=123))

    # 字典的方式进行传值的操作 解码字典 **
    d = {
        "username": "小锅",
        "num": 34
    }
    print("你的姓名:{username} 你的编号是:{num}".format(**d))

    # 坐标位置的选择
    point = (0, 1)
    print("我的坐标位置:{0[0]}:{0[1]}".format(point))

    user = User("成功", "22")
    user.fot()


class User(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age

    # 格式化类
    def fot(self):
        print("用户名:{self.username},年龄:{self.age}".format(self=self))


if __name__ == "__main__":
    format_str2()
