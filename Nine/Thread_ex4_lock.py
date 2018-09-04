"""
1核执行的操作其实是执行了上下文的切换的 所以看起来是执行了一个并发的操作的

2 多核的意义就是在能干多见识

3 在python中无论你有多少核 那么同一个时间只有执行的只有一个线程 python执行的线程只有一线程 因为是不断的在进行上下文的切换

4 python的线程是调用系统的原生线程 是调用的c写的线程

5 线程之间是可以共享数据的

6 全局解释器锁只是保证同一时间只有一个线程在执行

7

"""
import threading
import time


# 直接调用的方式 线程方式

def task(n):
    # 全局解释器锁
    # 获取一把锁
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    # 释放锁
    lock.release()


# 生成一个锁的实例
lock = threading.Lock()

num = 0
t_object = []  # 创建一个连续列表
# 循环启动50次线程
for i in range(50):
    t1 = threading.Thread(target=task, args=("t-%s" % i,))
    t1.setDaemon(True)  # 把当前线程设置为守护线程 t1那么就是守护线程  主线程不是守护线程
    t1.start()  # t2.start()
    t_object.append(t1)

for t in t_object:
    t.join()


# 打印线程的名称 这就是主线程 查看当前活跃的线程

print("----all threading has finsished", threading.current_thread(), threading.active_count())  # 主线程
print(num)
