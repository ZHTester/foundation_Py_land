# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/1/9  15:07'
"""
ThreadPoolExecutor 线程池 
1 from concurrent import futures 这个就是在Python3.2以后引入的线程池库concurrent(也就是线程池编程)
  from concurrent.futures import ThreadPoolExecutor --- ThreadPoolExecutor 也就是线程池函数
2 futures 这个包也就是做线程池编程与进程池编程的一个顶层包
3 线程池，我们为什么要线程池 ？  线程池第一个方面就是提供了数量控制的作用
4 主线程中可以获取某个线程的状态值或者说某一个人任务的状态，或者说返回值状态。
5 当一个线程完成的时候，我们的主线程能立刻知道，能知道返回的状态值。
6 futures 这个包可以让多线程的编码与多进程编码的接口变得一致，从而变得简单。所以后期将多线程变为多进程
  这样的切换将变得十分的平滑
7 
"""
from concurrent.futures import ThreadPoolExecutor


def get_html(times):
    time.sleep(times)
    print("get page {} sucess".format(times))
    return times


# ThreadPoolExecutor 实例化对象 --> def __init__(self, max_workers=None, thread_name_prefix=''):
# 线程池中同时运行多少个线程 max_workers
# 实例化线程池对象
excutor = ThreadPoolExecutor(max_workers=2)

"""这些就是futures给我们带来的一些方法与函数的好处"""
# 我们使用submit添加函数到线程池中,然后submit这个函数是存在返回值的 这就是futures类对象
# submit是立刻返回，非阻塞的
task1 = excutor.submit(get_html, 3)  # 向线程池中添加函数
task2 = excutor.submit(get_html, 2)  # 向线程池中添加函数

# 判断线程执行的状态
# done方法用于判定某个任务是否完成
print(task1.done())  # fasle 因为这里的停留时间是3秒,又因为submit是立刻返回，那么这里就是没执行完成的，所以是false
# 将某个方法cash掉 这个是属于futures类对象的方法
# 一个任务运行中与执行中，是不能cash掉的 由于我们这里task1以及提交上去了所以这里返回的就是false无法cash吊
print(task2.cancel())
time.sleep(4)
print(task1.done())
print(task1.result())  # result方法可以获取task的执行结果(返回的是3)
