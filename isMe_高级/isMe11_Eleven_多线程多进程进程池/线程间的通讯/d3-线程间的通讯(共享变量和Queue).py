# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/7  10:28'

"""
线程间的通讯(共享变量和Queue)  ---  安全性(这个也就是共享变量带来最大的坏处(并不推荐用作我们的通讯))
--- 安全性 也就是需要在线程上加一把锁，让我们的线程中的数据保持同步(按照指定的顺序)

"""
import threading
import time

detail_url_list = []  # 共享全局变量url


# 这个数据的抓取是通过for循环顺序抓取的，所以这样的速度肯定是赶不上并发的速度的 通过for循环
# 申明全局变量然后再在线程中共享全局变量
def get_detail_htm():
    global detail_url_list
    url = detail_url_list.pop()  # 共享变量的方式进行通讯 pop的用法
    # 爬取文章详情页
    print("get detail html start01....")
    time.sleep(2)
    print("get detail html end01.....")


# 这个数据的抓取是并发进行一个操作的
def get_detail_url():
    global detail_url_list
    # 爬取文章列表页-url
    print("get  detail url start02....")
    time.sleep(4)
    for i in range(20):
        detail_url_list.append("http://projectsedu.com/{id}".format(id=i))  # 共享变量的方式进行通讯
    print("get detail url  end02.....")


# 线程间的通讯 --- 也就是线程之间的共享变量[这样的是不够方便的 也是极力不推荐的
#                                         这个也是在十分了解锁的情况下才能使用这样的方式]


if __name__ == "__main__":
    # target=get_detail_htm, args=("",)
    thread_detail_url = threading.Thread(target=get_detail_url)
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_htm)
        html_thread.start()

    start_time = time.time()

    # 当主线程退出的时候, 子线程kill掉 ....
    print("last time:{}".format(time.time() - start_time))
