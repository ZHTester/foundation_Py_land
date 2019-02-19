# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/18  18:45'
import threading
from threading import Lock

a = 0
lock = Lock()


class Adds(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global a
        global lock
        for i in range(1000000):
            lock.acquire()
            a += 1
            lock.release()


class Desc(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global a
        global lock
        for i in range(1000000):
            lock.acquire()
            a -= 1
            lock.release()


if __name__ == "__main__":
    Thr_a = Adds("我是加法")
    Thr_b = Desc("我是减法")

    Thr_a.start()
    Thr_b.start()

    Thr_a.join()
    Thr_b.join()

    print(a)
