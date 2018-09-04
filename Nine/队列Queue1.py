"""
生产者消费者模型 就是典型的利用队列，解耦模型，
运维所使用的集群其实就是一个 生产者消费者模型，

解决了解耦 和效率的问题

生产骨头  吃骨头

"""

import queue

import threading, time

q = queue.Queue(maxsize=10)  # 队列的最大值  如果队列没有值还在取值就会出现卡住的效果


# 生产者
def Producer(name):
    count = 0
    while True:
        q.put("骨头%s" % count)
        print("生了骨头", count)
        count += 1
        time.sleep(2)


# 消费者
"""  
# while q.qsize() > 0: 如果q.qsize    等于0 那么线程就会出现一个卡顿的现象
"""
def ConSumer(name):
    while True:
    # while q.qsize() > 0:
        print("[%s] 取到了骨头[%s] 并且吃了它 。。。" % (name, q.get()))
        time.sleep(1)


p = threading.Thread(target=Producer, args=('chengdu',))
c = threading.Thread(target=ConSumer, args=('哈佛',))
c1 = threading.Thread(target=ConSumer, args=('特斯拉',))

p.start()
c.start()
c1.start()
