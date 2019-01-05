# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/5  13:38'

"""
1 python中的多线程编程，首先我们需要知道python能调度的最小单元是线程。
  由于进程对资源的消耗是比较的大的，所以后期就演变成了线程，但是了线程
  是依赖于进程的。就是这样的道理。 
2 对于IO操作来说，多线程和多进程的操作，性能差别不大。 甚至我们的多线程
  比我们的多进程的性能还要高。对于系统来说，线程的调度是要比进程的调度更
  加轻量级的。
3 通过Thread类来实例化 
4 在python中我们可以继承Thread来进行一个多线程的编程

**************************
1 我们去爬虫操作，一个去获取列表页面的Url一个得到Url然后再去爬取到页面的数据，
  这两个操作可以是同时进行的。GIL在遇到IO操作的时候，就会切换多线程的操作,也就是
  他在利用我们等待网络返回的时候，就切换到另外一个线程中去执行操作了

"""
import threading
import time


def get_detail_htm(url):
    print("get detail html start....")
    time.sleep(2)
    print("get detail html end .....")


def get_detail_url(url):
    print("get  detail url start....")
    time.sleep(4)
    print("get detail url  end .....")


if __name__ == "__main__":
    # target=get_detail_htm, args=("",)
    # 这里也就是含有三个线程 2个新建的线程和一条我们所使用的主线程都是并行的
    thread1 = threading.Thread(target=get_detail_htm, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # setDaemon 也就是将对应的线程设置为守护线程 非守护线程执行完成后，守护线程就kill掉了
    # thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()  # 启动线程
    thread2.start()
    # 阻塞主线程 等到子线程执行完成后，再去执行主线程 join() 这也就是阻塞的功效
    # 线程的运行时间 --- 是线程等待的最大时间并不是两者相加的时间
    thread1.join()
    thread2.join()
    # 当主线程退出的时候, 子线程kill掉 ....
    print("last time:{}".format(time.time()-start_time))



