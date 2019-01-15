# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/14  9:46'
"""
多进程编程 - Multiprocessing多进程编程

"""
import os
import time
# fork()中会新建一个子进程,，但是子进程与主进程的行为是不一样的。
# fork()只能是用于Linux&&unix win下面是不能使用的
# 进程和线程的数据是完全隔离的
# 父进程退出后子进程如果没退出，那么子进程则就不会退出了

pid = os.fork()  # 这个一旦创建我们就是能看到一个进程的
# 主进程的数据会全部拷贝一份到子进程
print("我是你大爷的大爷 ~~~~~")
if pid == 0:
    # 子进程的数据会全部拷贝一份到子进程，这样的话他们的数据就会出现完全隔离的状态
    print("子进程是{}, 父进程是{}. ".format(os.getpid(), os.getppid()))  # ···这个就是子进程会运行的
else:
    print("我是父进程:{}".format(pid))  # ···这个就是父进程会运行的

time.sleep(2)


















