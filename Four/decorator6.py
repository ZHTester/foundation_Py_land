"""

写一个装饰器

"""
import time

"""
定义一个高阶函数
timmer 使用到了高阶函数与嵌套函数
这就是装饰器 

    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
    *args, **kwargs  使用收集参数的功能 *args可以不传递传递那么就是元组是空数组
                                      **kwargs 可以传递多个参数那么就不是空数据
        
"""


def timer(func):  # timer(test1) func = test1
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return deco


@timer  # test1 = timer(test1)  运行的操作test1
def test1():
    time.sleep(3)
    print('in the test1')


@timer  # test2 = timer(test2)  =  deco test2(name) = deco(name)
def test2(name):
    print('test2', name)


test1()  # 实际上就是执行了deco的函数
test2('Mac Hao')
