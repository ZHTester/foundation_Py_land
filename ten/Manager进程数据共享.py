"""
进程数据共享
Manager（）返回的管理器将支持类型
list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition,
Event, Barrier, Queue, Value and Array. For example,


数据共享 并且实现修改

进程之间数据共享

Manager 方法

"""
from multiprocessing import Process, Manager
import os


def f(d, l):
    # d[1] = '1'
    # d['2'] = 2
    # d[0.25] = None
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  # 生成一个可在多个进程传递数据的一个字典 和共享

        l = manager.list(range(5))  # 生成一个在多个进程之间可以传递的列表 默认还有5个数据 和共享
        p_list = []  # 生成多个进程 等到join放入到这个列表中
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)

        for res in p_list:  # 等待结果
            res.join()

        print(d)
        print(l)
