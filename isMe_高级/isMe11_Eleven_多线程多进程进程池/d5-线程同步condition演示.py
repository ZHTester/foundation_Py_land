# coding=utf-8
import threading
from threading import Condition

__author__ = 'landing'
__data__ = '2019/1/8  15:51'
"""
condition - 生产者消费者模式(条件变量)
通过condition(源码)完成协同读诗
1 **1 def wait(self, timeout=None): 等待某个条件变量的通知
  **2 def notify(self, n=1): 这个方法就是去通知wait的信号源 
  这两个方法是condition的精髓 

2 notify  ---唤醒---> wait(--这个函数也就是等待条件变量的通知--)
3 with self.cond: 也就是调用了我们内部的acquire方法也就是 
4 condition 是有2把锁的，一般底层锁会在线程调用wait方法的时候释放
  上面的锁会在每次在调用wait的时候，分配一把放入到cond的等待队列中,的步伐带notify的唤醒
5 

"""


class xiaoAI(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        # 这就进入了条件变量(锁)的方式进入了
        # 也就是通过with语句就加入了这样的一把锁
        with self.cond:
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:好啊".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:汗滴禾下土".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:粒粒禾下土".format(self.name))
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

            print("{}:锄禾日当午 ~ ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:谁知盘中餐 ~ ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    cond = Condition()
    xiaoai = xiaoAI(cond)
    tianmao = tianJL(cond)

    # 在condition 线程同步中启动顺序是很重要的
    # 在调用with cond之后，才能调用wait notify
    xiaoai.start()
    tianmao.start()













