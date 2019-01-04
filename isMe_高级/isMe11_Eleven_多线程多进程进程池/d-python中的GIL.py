# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/4  10:49'

"""
python 中的 GIL---
------------------
GIL全称Global Interpreter Lock
1 python中的一个线程是对应与一个C语言中的线程。
2 CPython是大部分环境下默认的Python执行环境。所以在很多人的概念里CPython就是Python，也就想当然的把GIL归结为Python语言
  的缺陷。所以这里要先明确一点：GIL并不是Python的特性，Python完全可以不依赖于GIL。
3 python为了解释简单，所以在前期都会在CPU上加一把很大的锁，也就是一次只能运行一个线程。
4 python中的多线程慢，单实际情况下，python多线程编程就是否是真的慢了 这实际上是分情况的
5 GIL也就是使得同一时刻只有一个线程在一个cpu上执行，执行我们的字节码，这就在某种程度上说明我
  们python在执行的过程中是安全的，所以就是由于这个GIL就导致了，我们的python的多线程运行的速度一直都不是很高，
  无法将多个线程映射到多个cpu上，这样就无法体现多核的优势了。但是了我们还是有很多编译器是去掉了GIL的，不如说pypy编译器
6 线程间的同步这个也是需要好好考虑的。
7 GIL也就是不是整个过程的占用，GIL会根据字节码的行数以及是时间片释放GIL，
  来进行一个释放的操作，所以可以通过时间片来进行一个计算的，还有一种释放的情况就是遇到了GIL的IO操作

"""
# import dis
#
#
# # dis 也就是字节码的函数
# def add1(a):
#     a = a + 1
#     return a
#
#
# print(dis.dis(add1))  # 反编译a 这样的整个过程就是函数变成字节码的一个过程

import threading

total = 0


def add():
    # 1 do something1
    # 2 io 操作
    # 1 do something3

    global total
    for i in range(10000000):
        total += 1


def desc():
    global total
    for i in range(10000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print(total)  # 这样的gil资源就是会释放的

