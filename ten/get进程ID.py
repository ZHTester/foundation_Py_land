"""

获取进程ID

1 每一个进程都是由父进程启动的
2 每一个子进程都是由父进程启动的

"""
import multiprocessing
import os


def info(title):
    print(title)
    print('module name:', __name__)    # __name__ 模块名称
    print('parent process:', os.getppid())  # 获取副进程的ID 515
    print('process id:', os.getpid())  # 获取自己的ID 子进程  1129
    print("\n\n")


def f(name):
    info('\033[31;1m call function f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()
    # p.join()


