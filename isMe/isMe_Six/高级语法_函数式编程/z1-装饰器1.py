"""
装饰器

1 装饰器更多的是一种设计模式。
2 对修改是封闭的，对扩展是开放的。
3



"""
import time


def f1():
    print('this is function')


# unix 时间戳 这个就需要去百度了
def f2():
    print('this is function')


def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print("-------------")
print_current_time(f2)
