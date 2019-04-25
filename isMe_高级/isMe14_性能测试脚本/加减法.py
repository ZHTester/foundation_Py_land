# # coding=utf-8
# __author__ = 'landing'
# __data__ = '2019/2/18  18:45'
# import threading
# from threading import Lock
#
# a = 0
# lock = Lock()
#
#
# class Adds(threading.Thread):
#     def __init__(self, name):
#         super().__init__(name=name)
#
#     def run(self):
#         global a
#         global lock
#         for i in range(1000000):
#             lock.acquire()
#             a += 1
#             lock.release()
#
#
# class Desc(threading.Thread):
#     def __init__(self, name):
#         super().__init__(name=name)
#
#     def run(self):
#         global a
#         global lock
#         for i in range(1000000):
#             lock.acquire()
#             a -= 1
#             lock.release()
#
#
# if __name__ == "__main__":
#     Thr_a = Adds("我是加法")
#     Thr_b = Desc("我是减法")
#
#     Thr_a.start()
#     Thr_b.start()
#
#     Thr_a.join()
#     Thr_b.join()
#
#     print(a)
from lxml import html
import requests

url = "http://group.dt-lotto-debug-admin.com/"
html_data = requests.get(url).text  # 转换成xpath对象
print(html_data)
xpath_data = html.fromstring(html_data)  # 已经转换成xpath
id = xpath_data.xpath('//a[@href="javascript:_reloadMvcCaptchaImage()"]/img/@id')
print(id[0])

