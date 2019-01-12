# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/1/12  15:31'
"""
wait方法 --- 主线程 阻塞
from concurrent.futures import wait  这就是这样的一个方法
意思就是制定wait() 某些task 和很多task 执行完成才继续往下面执行

"""
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED


def get_html(times):
    time.sleep(times)
    print("get page {} sucess".format(times))
    return times


# ThreadPoolExecutor 实例化对象 --> def __init__(self, max_workers=None, thread_name_prefix=''):
# 线程池中同时运行多少个线程 max_workers
# 实例化线程池对象
excutor = ThreadPoolExecutor(max_workers=2)

urls = [4, 3, 2]  # 这里也就是sleep 请求多少秒
all_task = [excutor.submit(get_html, url) for url in urls]
# def wait(fs, timeout=None, return_when=ALL_COMPLETED):  fs 等待的task  return_when 什么时候就不等待了
wait(all_task, return_when=FIRST_COMPLETED)
print("main")

# for future in as_completed(all_task):  # 这样就能完成这样的一个获取然后返回正确的task
#     data = future.result()
#     print("get {} page ".format(data)) # excutor.map() 这样的方法就是比这样的方式更加的简单

# # 通过excutor获取已经完成的task 这里就是根据Url的顺序进行执行的
# for data in excutor.map(get_html, urls):
#     print("get {} page ".format(data))











