# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/7  15:05'
"""
线程同步 ---  也就是线程会抢占系统资源，这个时候我们就是需要线程锁(Lock)来保证线程之前的锁OK
1 多线程应该解决的2个问题，第一个就是多线程通讯的问题(通讯的问题就是Queue来解决)，
  第二就是线程同步的问题就是通过lock锁来解决的问题。
2 多线程编写都线程最棘手的一个问题，也就是线程同步的问题,其实这也就是很大的问题。
3 线程资源的抢占，也就是需要线程锁，来保证这样的同步机制  --- 这就是线程同步机制。
4 当线程被锁住的饿时候，实际上也就是只有一个代码段，来运行这段代码，等待运行完成后锁才能释放，等待下一个资源的进入。
5 锁最大的问题就是性能，获取锁和释放锁都是需要时间的  --- 这个问题也就是我们并发性能必然会引起的一个问题。
6 锁会引起死锁 -  所以就会存在很多锁。
7 死锁的情况就会出现互相等待的情况  --- 资源竞争的一个关系就会很容易的造成了死锁的关系。
8 可重入的锁RLock,在同一个线程里面可以连续调用多次acquire，但是要注意acquire的次数要和release的次数相等。

"""
import threading
from threading import Lock, RLock

# import dis

total = 0

# 申明一把锁 锁住以后才能允许其他的代码段允许
lock = Lock()


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()  # 将锁加入进来
        # lock.acquire()  # 将锁加入进来 这里就会存在死锁的情况 也就是说在这样的情况下，代码就不会在运行了
        total += 1
        lock.release()  # 释放锁-如果没有释放的话其他的线程是无法进入的


def dosomething(lock):
    lock.acquire()  # 将锁加入进来
    # do something
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








# """
#  36           0 LOAD_FAST                0 (a)
#               2 LOAD_CONST               1 (1)
#               4 INPLACE_ADD
#               6 STORE_FAST               0 (a)
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE
# None
#  40           0 LOAD_FAST                0 (a)
#               2 LOAD_CONST               1 (1)
#               4 INPLACE_SUBTRACT
#               6 STORE_FAST               0 (a)
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE
# None
#
# 每次执行一次GIL的时候，他都是有可能释放的，因为他的GIL已经满了，也就是切换给了另外一个线程的
# """
#
#
# def add1(a):
#     a += 1
#
#
# def desc1(a):
#     a -= 1
#
#
# print(dis.dis(add1))
# print(dis.dis(desc1))
#
