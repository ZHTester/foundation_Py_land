"""

event 时间-线程

1 event 时间是用于线程之间同步的

event = threading.Event()  生成一个event对象
event.wait() 标志位未设置就阻塞  标志位一设置就不会阻塞 等待标志位被设定
标志位设定了代表设定，代表直接走了
event.set() 设置一个event全局变量
event.clear()  清空全局变量  如果标志位清空，就代表没有标志位了
"""
import time
import threading

event = threading.Event()  # 生成一个event对象


def lighter():
    count = 0
    event.set()  # 先设置绿灯
    while True:
        if count > 5 and count < 10:
            event.clear()  # 把标志位清空
            print('\033[41;1m--****** 变为红灯了 *****---\033[0m')
        elif count > 10:
            event.set()  # 变为绿灯
            count = 0
        else:
            print('\033[42;1m--****** 变为绿 灯了 *****---\033[0m')
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 设置了标志位代表绿灯
            print('[%s] runint 跑快点哦 ......' % name)
            time.sleep(1)
        else:
            print("[%s] waiting 等红绿灯......" % name)
            event.wait()
            print("[%s] 绿灯亮了快跑吧 ......" % name)


light = threading.Thread(target=lighter)
light.start()
car1 = threading.Thread(target=car, args=("bengbeng",))
car1.start()
