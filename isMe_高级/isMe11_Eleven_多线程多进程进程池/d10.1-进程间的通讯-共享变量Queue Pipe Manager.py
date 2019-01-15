# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  16:31'

"""
1 全局共享变量的方式-在进程中通讯
2 共享全局变量，在我们多进程中是不适用的，在多线程中才能使用的 
3 进程中的数据是相互独立的，所以进程中的数据修改后，是不会影响其他的数据的

"""
from multiprocessing import Process,Queue
import time


def producer(a):
    a += 1
    time.sleep(2)


def consumer(a):
    time.sleep(2)
    print(a)


if __name__ == "__main__":
    a = 1
    myp = Process(target=producer, args=(a,))
    myc = Process(target=consumer, args=(a,))

    myp.start()
    myc.start()

    myp.join()
    myc.join()



