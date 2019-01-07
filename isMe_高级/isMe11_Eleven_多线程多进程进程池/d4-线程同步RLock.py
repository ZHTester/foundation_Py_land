# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/7  16:16'

import threading
from threading import Lock, RLock


"""
7 死锁的情况就会出现互相等待的情况  --- 资源竞争的一个关系就会很容易的造成了死锁的关系
8 可重入的锁RLock,在同一个线程里面可以连续调用多次acquire，但是要注意acquire的次数要和release的次数相等
9 但是必须是在同一个线程中使用RLock
"""
total = 0
# lock = Lock()  # 申明一把锁
lock = RLock()  # 申明一把锁


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()  # 将锁加入进来
        lock.acquire()  # 将锁加入进来 这里就会存在死锁的情况
        total += 1
        lock.release()  # 释放锁-如果没有释放的话其他的线程是无法进入的
        lock.release()  # 释放锁-如果没有释放的话其他的线程是无法进入的


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()  # 将锁加入进来
        total -= 1
        lock.release()  # 释放锁-如果没有释放的话其他的线程是无法进入的


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
# 这样的gil资源就是会释放的 但是这样的资源的值不是恒定的 这就是线程同步需要考虑的
# 增加了锁，就能保证数据的同步了
print(total)
