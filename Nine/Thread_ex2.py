"""
继承式调用threading

"""
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num, sleep_time):
        super(MyThread, self).__init__()
        self.num = num
        self.sleep_time = sleep_time

    def run(self):
        print("runing task ", self.num)
        time.sleep(self.sleep_time)  # 执行停止2秒
        print("task done", self.num)


t1 = MyThread("t1", 4)
t2 = MyThread("t2", 5)

t1.start()
t2.start()
t1.join()  # wait() 变成串行的
t2.join()


print("main thread ... ")

