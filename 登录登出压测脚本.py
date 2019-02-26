# coding=utf-8
import os

__author__ = 'landing'
__data__ = '2019/2/8  16:39'

"""
10 人的登录登出  

1 首先需要2个线程 2个方法 1-login 2-loginout
2 线程之间的通讯   - lock Queue(消息队列) 
3 threading 线程库 
                           target - 线程要运行的什么东西     args 传入参数 tuple 传入一个参数 args=(5,)
4 login = threading.Thread(target="",args=(5))  --- 线程的方式 
5 login.start()
6 login.join()

import threading
from threading import Lock
from queue import Queue
import requests

"""
import requests
import threading
from threading import Lock
from queue import Queue

lock = Lock()
que = Queue()  # 消息队列 对象


# 登录接口
def get_login(queue, url, data):
    global res, oid, name
    lock.acquire()  # 加一把锁
    res = requests.post(url=url, data=data).json()  # post请求 200
    try:
        oid = res["data"]["oid"]  # null
        name = res["data"]["username"]
    except KeyError as e:
        # os._exit(0)  # 退出程序
        pass

    queue.put(oid)  # 往消息队列放入数据
    queue.put(name)  # 往消息队列放入数据
    lock.release()
    print("登录用户------", name, res)


def get_loginout(queue):
    global res
    lock.acquire()
    oid = queue.get()  # 取数据了
    name = queue.get()  # 取数据了
    data_out = {"username": name, "oid": oid}
    url_out = "http://1029a.s1119.com/m/php//action.php?action=logout"
    res = requests.post(url=url_out, data=data_out).json()
    lock.release()
    print("登出用户------", name, res)


for i in range(2, 200):
    q = Queue(maxsize=10)  # 消息队列
    name = 'dstest000' + str(i)  # 造数据 dest0001 int txt excle mysql
    data = {"username": name, "password": "aeuio888", }
    url_login = "http://1029a.s1119.com/m/php/action.php?action=login"

    thread_login = threading.Thread(target=get_login, args=(q, url_login, data))
    thread_loginout = threading.Thread(target=get_loginout, args=(q,))

    thread_login.start()
    thread_loginout.start()

    thread_login.join()
    thread_loginout.join()
