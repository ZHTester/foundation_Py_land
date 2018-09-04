"""

进程池
用到多进程肯定是会用到进程池的

进程池中有两个方法：

apply  同步执行 川行
apply_async  异步执行  并行

"""

from multiprocessing import Process, Pool
import time, os


def Foo(i):  # 这是一个进程
    time.sleep(2)
    print("in presss(子进程1:):", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg,("子进程2:%s" % os.getpid()))


if __name__ == '__main__':

    pool = Pool(processes=5)  # 允许进程池同时放入5个进程
    print("主进程PID:",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar) # callback= 回调 先执行完成Foo 在执行Bar 回调函数是在主进程中执行的
                                                            # 向进程池中放入一个进程  并行
                                                            # pool.apply(func=Foo, args=(i,)) 串行

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。