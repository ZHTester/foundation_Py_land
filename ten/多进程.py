import multiprocessing

"""多进程"""
"""启动一个进程 
   启动多个进程"""
from multiprocessing import Process
import time, threading


def thread_run():
    print(threading.get_ident())  # 打印线程号


def f(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_run)
    t.start()


"""

并发测试

"""
if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=f, args=('bob %s' % i,))
        p.start()  # p.join()
