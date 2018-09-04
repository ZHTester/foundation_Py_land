"""
1 怎样在单线程的模式下实现协程的并发效果了
   遇到IO操作就切换 IO就是耗时 协程之所以能支持大量并发就是把IO操作给挤掉了
   所以就是说协程就是没有io操作 ，所以只有cpu的操作，那么就是快。

2 实现IO操作已完成就开始执行并发的操作，IO操作就切换回去执行相关的操作。

3 程序如何实现监控IO操作的自动完成的了

"""
import time

def bbs():
    print('fun1')
    time.sleep(5)

def cdn():
    print('fun2')
    time.sleep(4)
    
def login1():
    print('fun3')























































