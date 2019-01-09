# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/9  10:43'
"""
信号量
用于控制进入数量的锁 (Semaphore)
1 文件读写 写一般只用于一个线程写,读可以允许多个。读和读不是互斥的，写和写是互斥的
2 信号量 - Semaphore 也就是基于Condition来实现的 这一点从源码上我们就能查看的到

"""
import threading
from threading import Semaphore
import time


class HtmlSProducer(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("go to html text sucess")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(300):
            self.sem.acquire()
            html_thread = HtmlSProducer("https://www.baidu.com/{}".format(i),self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    urlP = UrlProducer(sem)
    urlP.start()































