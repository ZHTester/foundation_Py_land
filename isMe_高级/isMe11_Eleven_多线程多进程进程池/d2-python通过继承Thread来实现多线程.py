# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/5  14:55'
"""
通过实现继承Thread来实现多线程
***1*** class GetDetailEmail(threading.Thread):
"""
import threading
import time


class GetDetailHtml(threading.Thread):
    # 多线程编程多多写写集成init方法
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html start....")
        time.sleep(2)
        print("get detail html end .....")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url start....")
        time.sleep(6)
        print("get detail url end .....")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl('get_detail_url')

    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("last time{}:".format((time.time())-start_time))
