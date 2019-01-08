# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/8  14:47'
"""
线程同步 - condition 使用以及源码分析  ---- 条件变量
condition 也就是用于线程之间的锁，用于复杂间的线程数据同步(锁)(也称之为条件变量)
condition - 生产者消费者模式(条件变量)


"""
from threading import Condition
import threading


class xiaoAI(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="小爱")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{}:好啊".format(self.name))
        self.lock.release()

        self.lock.acquire()
        print("{}:在".format(self.name))
        self.lock.release()


class tianJL(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="天猫精灵")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{}:小爱同学".format(self.name))
        self.lock.release()

        self.lock.acquire()
        print("{}:我们来对古诗吧 ~ ".format(self.name))
        self.lock.release()


if __name__ == "__main__":
    lock = threading.Lock()
    xiaoai = xiaoAI(lock)
    tianmao = tianJL(lock)

    tianmao.start()
    xiaoai.start()


