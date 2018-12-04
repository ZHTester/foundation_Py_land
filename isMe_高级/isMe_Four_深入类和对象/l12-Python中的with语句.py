"""
python中上下文管理器，其实也就是with语句的一个缩写
1 什么是上下文管理器 - 实际上Python也就是基于协议来进行一个开发的，上下文管理，其实也就是基于上下文管理协议来进行编程的
  既然是协议，那么肯定就是和我们的魔法函数相关联的 其中的魔法函数也就是 __enter__ __exit__ 这两种协议而进行的

2 python中的with(上下文管理器)语句就是为了 简化我们 try - finally 这样的写法诞生的

"""


def exe_try():
    try:
        r_read = open('landing.txt')
        print("----我们已经打开文件了----")
        raise KeyError
        return 1
    except KeyError:
        print("key Error !")
        return 2
    else:
        print("other error !")
        return 3
    finally:
        print("finally !")
        return 4


"""
上下文管理器
1 Python中有很多魔法函数，其中我们把某些魔法函数定义到这个类的下面，这个类就满足了我们魔法函数所支持的协议
  这样我们就实现了我们了上下文管理器的协议，上下文管理器协议的好处就是，我们可以直接使用with语句来进行使用 
  


"""


class Sample:
    def __enter__(self):
        # 获取资源
        print("entering")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exiting")
        return self

    def do_something(self):
        print("doing something")

"""

这个就是具体的with语句的使用方法   - 十分重点
1 with语句 在调用这样的上下文管理器协议的时候，首先回去默认的
  调用enter这样的一个魔法函数，再去调用exit这样的一个魔法方法 这个过程我们完全是由Python解释器来给我进行一个操作的
  我们只需要通过这个with语句来进行操作，所以有了这样的一个上下文管理器协议之后，我们只需要在exit中释放资源，我们在enter中
  获取资源  -  这样的实现方式就可以了。


"""
with Sample() as simple:
    simple.do_something()


# if __name__ == "__main__":
#     res = exe_try()
#     print(res)
