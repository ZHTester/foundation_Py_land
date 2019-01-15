# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  11:34'

"""
进程间的通讯 ~ Queue Pipe Manager
from multiprocessing import Process,Queue ----
Queue 这里是不能使用 from queue import Queue 线程中的Queue
multiprocessing 中的Queue 不能应用于Pool进程池中
"""
from multiprocessing import Process,Queue,Pool
import time


def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    queue = Queue(10)
    pool = Pool(2)
    pool.apply_async(producer,args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()  # multiprocessing 中的Queue 不能应用于Pool进程池中

    # 常规情况下的线程中的Queue
    # myp = Process(target=producer, args=(queue,))
    # myc = Process(target=consumer, args=(queue,))
    #
    # myp.start()
    # myc.start()
    #
    # myp.join()
    # myc.join()
