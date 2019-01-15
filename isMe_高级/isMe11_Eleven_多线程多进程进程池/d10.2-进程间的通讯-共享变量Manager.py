# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  16:52'
"""
Manager 用于进程池中的数据


"""
from multiprocessing import Process, Queue, Pool,Manager
import time


def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    # from queue import Queue
    # from multiprocessing import managers
    # from multiprocessing import Queue
    # pool间的进程间通讯需要使用manager中的Queue
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
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
