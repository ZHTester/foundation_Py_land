# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  17:33'
"""
1 进程间的通讯Pipe
2 Pipe是简化版的Queue 

"""
from multiprocessing import Process, Queue, Pool,Manager,Pipe
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
    recevie_pipe, send_pipe = Pipe()
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()  # multiprocessing 中的Queue 不能应用于Pool进程池中



