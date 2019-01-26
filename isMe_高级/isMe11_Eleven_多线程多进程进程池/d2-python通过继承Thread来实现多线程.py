# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/5  14:55'
"""
通过实现继承Thread来实现多线程  - 也就是使用了重载了Thread的方法 这个时候我们就可以添加更多的逻辑来实现多线程编程
***1-2*** class GetDetailEmail(threading.Thread):
          1 但是这样的方式，我们就需要重载run方法，这个也就是多线程的逻辑
          2 我们在这里也是可以重载__init__方法 这个是线程中添加一些属性方法 他在这里就会去调用父类的构造方法
   
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
