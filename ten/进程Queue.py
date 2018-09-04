"""
进程Queue

主进程和子进程内存是不能共享的

子进程一旦被父进程启动，他们之间的内存就是相互独立的，那么父进程中的变量就不能被子进程中访问到。

实现了数据的传递，并没有实现对同一份

queue实现了这个进程的数据传递给另外一个进程

只是数据的传递而不是数据的共享


"""
from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()



