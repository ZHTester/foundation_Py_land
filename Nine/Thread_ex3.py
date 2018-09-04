"""

1 主线程与子线程的关系

2 守护进程

3 不加 join 那么主线程和子线程是并行进行的是没有依赖关系的

4 加了join以后主线程是依赖子线程执行完毕在执行

5 守护进程 子线程是守护主线程  程序退出之前是还有个join后

6 只要主线程执行完毕 他不管子线程是否执行完毕 那所有的线程都执行完毕
7 线程之间是可以共享数据的



"""

import threading
import time


# 直接调用的方式 线程方式

def task(n):
    print("task", n)
    time.sleep(2)
    print('task down', n, threading.current_thread())


start_time = time.time()
t_object = []  # 创建一个连续列表
# 循环启动50次线程
for i in range(50):
    t1 = threading.Thread(target=task, args=("t-%s" % i,))
    t1.setDaemon(True)   # 把当前线程设置为守护线程 t1那么就是守护线程  主线程不是守护线程
    t1.start()  # t2.start()
    t_object.append(t1)

# for t in t_object:
#     t.join()


# 打印线程的名称 这就是主线程 查看当前活跃的线程
time.sleep(2)
print("----all threading has finsished", threading.current_thread(),threading.active_count())  # 主线程

# 计算时间差
print('constTime :', time.time() - start_time)
