"""

写一个装饰器

"""
import time

"""
定义一个高阶函数
timmer 使用到了高阶函数与嵌套函数


这就是装饰器 


"""


def timer(func):   # timer(test1) func = test1
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return deco


# def timmer():
#     def deco():
#         pass

def test1():
    time.sleep(3)
    print('in the test1')


def test2():
    time.sleep(3)
    print('in the test2')


# test2()
# test1()

# deco(test2)
# deco(test1)

# 不修改函数的内存地址 也不修改函数的调用方式
# test1 = deco(test1)
# test1()
#
# test2 = deco(test2)
# test2()


test1 = timer(test1)

test1()   # 实际上就是执行了deco的函数











