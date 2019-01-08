# coding=utf-8
import threading
from threading import Condition

__author__ = 'landing'
__data__ = '2019/1/8  15:51'
"""
condition - 生产者消费者模式(条件变量)
通过condition(源码)完成协同读诗
1 **1def wait(self, timeout=None): 等待某个条件变量的通知
  **2def notify(self, n=1): 这个方法就是去通知wait的信号源 
  这两个方法是condition的精髓 

2 notify  ---唤醒---> wait
3 with self.cond: 也就是调用了我们内部的acquire方法也就是 
4 condition 是有2把锁的，一般底层所会在线程调用wait方法的时候释放
  上面每次在调用wait的时候，分配一把放入到cond的等待队列中,的步伐带notify的唤醒


"""


class xiaoAI(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:好啊".format(self.name))
            self.cond.notify()


class tianJL(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}:小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:我们来对古诗吧 ~ ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = xiaoAI(cond)
    tianmao = tianJL(cond)

    # 在condition 线程同步中启动顺序是很重要的
    # 在调用with cond之后，才能调用wait notify
    xiaoai.start()
    tianmao.start()













