"""
contextlib 简化我们的上下文管理器协议
@contextlib.contextmanager 就可以使用这个装饰器，将这个函数变为一个上下文管理器，他是如何做到的了，其实他就是很巧妙的使用了


 生成器的方式来进行搞的 ------> 这个自己先百度吧

"""
import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print("file open")  # 这就相当于上下文管理器魔法函数中的enter
    yield {}
    print("filed end") # 这个就相当于上下文管理器魔法函数中的exit


with file_open("landing.txt") as f_open:
    print("file processing")
