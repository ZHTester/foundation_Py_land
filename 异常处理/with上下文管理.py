"""

witch语句其实就是一套上下文的管理：
    1 上下文管理协议包含的方法: __enter__() 和 __exit__() 支持该协议的对象要实现这两个方法
    2 上下文管理器：定义执行with语句时候，要建立的运行时上下文，负者执行with语句块上下文中的进入与退出的操作
    3 进入上下文管理器：调用管理器_enter()方法，，如果没有设置as var变量就接受_enter_方法返回值
    4 退出上下文管理器：调用管理器__exit__方法

with语句应用场景：
    1 文件操作
    2 进程线程之间互斥对象，例如互斥锁
    3 与自定义一些支持上下文的其他对象

"""


class MyResource:
    def __enter__(self):
        print("查询开始")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("查询结束")

    def query(self):
        print("查询中")


with MyResource() as f:
    f.query()
