"""
实现装饰器的知识储备
1 函数也就是变量
2 高阶函数
3 嵌套函数 - 函数的嵌套
4 高阶函数+嵌套函数 = 装饰器


2 高阶函数
 a: 把一个函数当做实参传给另外一个函数(在不修改被装饰函数源代码的情况下为其添加功能)

"""
import time


def bar():
    time.sleep(5)
    print('in the bar')


def test1(func):
    star_time = time.time()
    func  # 运行的是bar函数
    stop_time = time.time()
    print('总耗时 %s' %(stop_time - star_time))


# test1(bar)  # bar 其实就是bar当做参数进行传递  这样的形式test1 就是装饰器 但是调用的方式就是被改变了。
bar()  # bar直接bar() 当做参数进行传递




























