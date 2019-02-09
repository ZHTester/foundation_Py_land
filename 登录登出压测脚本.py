# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/8  16:39'

import requests
import threading
from threading import Lock
from queue import Queue

lock = Lock()
que = Queue()


def get_login(queue, url, data):
    lock.acquire()  # 加一把锁
    res = requests.post(url=url, data=data).json()
    oid = res["data"]["oid"]
    name = res["data"]["username"]
    queue.put(oid)
    queue.put(name)
    lock.release()
    print("登录用户", name, res)


def get_loginout(queue):
    lock.acquire()
    oid = queue.get()
    name = queue.get()
    data_out = {"username": name, "oid": oid}
    url_out = "http://1029a.s1119.com/m/php//action.php?action=logout"
    res = requests.post(url=url_out, data=data_out).json()
    lock.release()
    print("登出用户", name, res)


for i in range(2, 20):
    q = Queue(maxsize=10)
    name = 'dstest000' + str(i)
    data = {"username": name, "password": "aeuio888", }
    url_login = "http://1029a.s1119.com/m/php/action.php?action=login"
    thread_login = threading.Thread(target=get_login, args=(q, url_login, data))
    thread_loginout = threading.Thread(target=get_loginout, args=(q,))

    thread_login.start()
    thread_loginout.start()

    thread_login.join()
    thread_loginout.join()
