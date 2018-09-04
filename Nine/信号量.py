"""
信号量

互斥锁 同时只允许一个线程更改数据，
而Semaphore是同时允许一定数量的线程更改数据 ，
比如厕所有3个坑，那最多只允许3个人上厕所，后
面的人只能等里面有人出来了才能再进去。

信号量和所的区别就是 信号量有多把锁

系统不会默认限制启动多少个线程，但是启动的线程越多其实就是把整体的系统变慢或者说是把程序变慢


"""

import threading, time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()


if __name__ == '__main__':

    num = 0
    # 声明信号量锁
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    print(num)