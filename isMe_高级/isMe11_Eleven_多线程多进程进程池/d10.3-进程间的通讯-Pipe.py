# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  17:33'
"""
1 通过Pipe 实现进程间的通讯 ---
2 pipe的性能是高于queue的

"""
from multiprocessing import Process, Queue, Pool,Manager,Pipe
import time


def producer(pipe):
    pipe.send("landing")
    time.sleep(2)


def consumer(pipe):
    print(pipe.recv())


if __name__ == "__main__":

    # pool间的进程间通讯需要使用manager中的Queue
    # pipe只适用于2个进程
    recevie_pipe, send_pipe = Pipe()
    pool = Pool(2)
    my_producer = Process(target=producer, args=(send_pipe,))
    my_consumer = Process(target=consumer, args=(recevie_pipe,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()






