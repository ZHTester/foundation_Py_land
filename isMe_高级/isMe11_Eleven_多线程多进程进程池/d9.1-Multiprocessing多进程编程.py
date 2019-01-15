# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  9:58'
"""
多进程编程 ·····
multiprocessing这个包是要比ProcessPoolExecutor更加底层的多进程编程的包 
# 这个也就是我们进行多进程编程的首选这个包和我们的Future是一样的原理
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

multiprocessing.Process  # 这样也就代表一个进程
"""
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time
import os


def get_html(n):
    time.sleep(n)
    print("sub_Progess sucess ")
    return n

# class My_Multiprocessing(multiprocessing.Process):


if __name__ == "__main__":
    # 单纯的写法 进程
    progess = multiprocessing.Process(target=get_html, args=(2,))
    progess.start()
    progess.join()
    print(progess.pid)
    print("main progess ")
    """
    1 如果我们不申明有多少个线程池的大小，那么Python就会根据我们有多少个cpu来申明我们有多少个线程池
      因为我们多进程的数量，最好是等于我们cpu的数量这样的性能是最高的。
            if processes is None:
            processes = os.cpu_count() or 1
    2 pool = multiprocessing.Pool(multiprocessing.cpu_count()) 这样就直接获取到我们cpu的数量
    3 
    """
    # 使用进程池 --- multiprocessing里面的线程池 ***************
    pool = multiprocessing.Pool(3)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    """
    apply_async ---- ApplyResult(返回所有的执行任务) 
    1 get(ApplyResult源码解释) 的一些返回值
    """
    result = pool.apply_async(get_html, args=(2,))  # 异步的从线程池中提交任务 这里的返回就是 ApplyResult
    # pool.close()  # 这里也就是关闭我们的进程池，不在接受新的数据进入
    # # 将所有的Thread join一下，也就是等待所有的线程(任务)执行完成 执行完成后也就是在result中get数据
    # pool.join()
    # print(result.get())

    # # imap  位置顺序打印*************************
    # for result in pool.imap(get_html,[1,5,3]):
    #     print("{} sleep sucess".format(result))

    # imap  时间顺序打印
    for result in pool.imap_unordered(get_html,[1,5,3]):
        print("{} sleep sucess".format(result))

