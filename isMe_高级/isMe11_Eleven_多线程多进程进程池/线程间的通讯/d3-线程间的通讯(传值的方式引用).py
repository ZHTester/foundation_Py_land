# coding=utf-8
import threading
import time
from isMe_高级.isMe11_Eleven_多线程多进程进程池.线程间的通讯 import variables

__author__ = 'landing'
__data__ = '2019/1/7  11:14'
# detail_url_list = []  # 共享全局变量url  也就现在把这个变量拿到了单独的文件中


# 这个数据的抓取是通过for循环顺序抓取的，所以这样的速度肯定是赶不上并发的速度的 通过for循环
# 申明全局变量然后再在线程中共享全局变量
def get_detail_htm():
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()  # 共享变量的方式进行通讯 这样的操作就是线程不安全的
            # 爬取文章详情页
            print("get detail html start....")
            time.sleep(2)
            print("get detail html end .....")


# 这个数据的抓取是并发进行一个操作的
def get_detail_url(detail_url_list):
    detail_url_list = variables.detail_url_list
    while True:
        # 爬取文章列表页-url
        print("get  detail url start....")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))  # 共享变量的方式进行通讯
        print("get detail url  end .....")


# 线程间的通讯 --- 也就是线程之间的共享变量[这样的是不够方便的]
# 线程间的通讯 --- 通过传入值的变量,来实现线程之间的通讯
# 线程间的通讯 --- 在多线程中共享变量是没有问题的，但是在多进程中贡献变量是不行的(也就是说不能共享变量的方式来进行通讯)


if __name__ == "__main__":
    # target=get_detail_htm, args=("",)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(variables.detail_url_list,))
    for i in range(2):
        html_thread = threading.Thread(target=get_detail_htm, args=(variables.detail_url_list,))
        html_thread.start()

    start_time = time.time()
    # 当主线程退出的时候, 子线程kill掉 ....
    print("last time:{}".format(time.time() - start_time))
