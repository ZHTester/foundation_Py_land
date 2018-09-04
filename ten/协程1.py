"""
协程 .......


1 协程又叫微线程  协程就是一种用户态的轻量级的微线程
2 协程在CPU中是认不到的   cpu只认识线程 。。。
3 两个线程在修改同一个数据的时候，就会产生线程锁的概念，但是在协程中就不设计这一的一个问题 。
  因为协程就是单线程中实现的，那么这么说的话就是串行的

在单线程的情况下实现并发的效果 这就是通过协程来实现的
多并发的效果就是在单线程的情况下多次的切换
优点：
1 无须上下文切换的开销
2 高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理。
  因为一个协程是已在一个线程中，所以一个协程处理上万个协程的并发都是没有问题的。
缺点：
   1 携程无法利用多核的资源
   2 无法利用多核资源：协程的本质是个单线程,它不能同时将 单个CPU的多个核用上,协程需要和进程配合才能运行在多CPU上.
   3 当然我们日常所编写的绝大部分应用都没有这个必要用在用多线程的，除非是cpu密集型应用(Nginx中能支持大量的并发是因为他默认是单线程的)
     他的一个进程里面就只有一个线程，nginx一个线程能支持上w的并发，但是nginx能配制成多线程，每个线程都能支持是上w的并发协程
   进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序



我们是通过yiled 生产者消费者模型 实现在单线程下实现多并发的一个效果
"""

import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield   # yield 是可以接受数据的  唤醒后就会执行下面的程序代码
        print("[%s] is eating baozi %s" % (name, new_baozi))  # time.sleep(1)


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0

    while n < 5:
        n += 1
        time.sleep(1)
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()




























































