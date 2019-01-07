# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/7  11:44'
"""
消息队列其实也就是一个队列，在很多时候
共享变量queue - 安全可靠 - 通过queue的方式来实现线程间的数据同步。
1 Queue也就是消息队列
2 queue的常用方法就是 put(阻塞的方法) 和 get 
3 queue就是可以再多个线程请求参数的时候，做到线程安全的一个效果，不会造成资源的争抢而导致数据的不安全性
4 _qsize 得到队列的长度 
  empty 判断队列是否为空
  full 判断队列是否已满，如果已满，那么执行put就会实现一个阻塞，等到有空闲的容量为止。
  put_nowait 也就是在往数据放入数据的时候，没有必要等到数据完成后才返回，异步存放数据的方法
  get_nowait 也就是在往数据取出数据的时候，没有必要等到数据完成后才返回，异步提取数据的方法
  
  --- 这两组数据就是成对出现的 这样也是为我们提供了很多方便的
  task_done 也就是调用了这个函数我们的join函数才会退出的。
  join 也就是从我们队列的角度来阻塞我们的主线程。
"""
from queue import Queue
import threading
import time


def get_detail_htm(queue):
    while True:
        url = queue.get()  # 共享变量的方式进行通讯
        # 爬取文章详情页
        print("get detail html start....")
        time.sleep(2)
        print("get detail html end .....")


# 这个数据的抓取是并发进行一个操作的
def get_detail_url(queue):
    while True:
        # 爬取文章列表页-url
        print("get  detail url start....")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))  # 共享变量的方式进行通讯
        print("get detail url  end .....")


if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)  # 消息队列Queue

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_htm, args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()
    # 当主线程退出的时候, 子线程kill掉 ....
    print("last time:{}".format(time.time() - start_time))





