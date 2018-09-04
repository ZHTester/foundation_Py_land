"""

进程锁

"""
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()  # 枷锁
    print('hello world', i)
    l.release()  # 释放锁


if __name__ == '__main__':
    lock = Lock()  # 首先需要生成锁的实例

    for num in range(100):
        Process(target=f, args=(lock, num)).start()   # 在将锁的实例传递给方法变量中去


