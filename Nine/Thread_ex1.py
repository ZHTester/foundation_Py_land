"""

进程和线程


1  线程是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务

2 线程就是操作系统等于一堆指令  os调用CPU最小的单位就是线程 线程是包含在进程中的

3 多线程是同时并发的

4 线程启动的方式

5 子线程和主线程是没有任何关系的

6 默认情况下主线程是不会等子线程执行完成的 在主线程的执行中等待子线程的执行结果 。。。
"""

import threading
import time


# 直接调用的方式 线程方式

def task(n):
    print("task", n)
    time.sleep(4)


start_time = time.time()
t_object = []  # 创建一个连续列表
# 循环启动50次线程
for i in range(50):
    t1 = threading.Thread(target=task, args=("t-%s" % i,))
    # t2 = threading.Thread(target=task, args=("t2",))
    # 启动线程
    t1.start()  # t2.start()
    t_object.append(t1)

for t in t_object:
    t.join()


# 计算时间差
print('constTime :', time.time() - start_time)
