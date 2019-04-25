# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/25  14:51'
"""
事件钩子  - requests
1 钩子都是事件驱动型的开发他是可以稍微改变一下我们的开发思路 js 基于回调的，回调也就是基于事件完成以后一系列的函数
2 其中request是一种线性处理的方式，而钩子事件其实就是一种非线性处理的方式。
3 处理响应时间的钩子  

IO 请求     
    ------> 程序
自动将这个response放入到回调函数中
   <------> 回调函数 

"""
import requests


def get_key_info(response, *args, **kwargs):
    """
    这个函数就是所谓的回调函数
    :return:
    """
    print(response.headers)


def run_main():
    # 这样的形式就通过回调模式 钩子的事件进行调度的
    # 这样的会更加好的管理我们的函数与程序

    requests.get('https://www.baidu.com', hooks=dict(response=get_key_info))


if __name__ == "__main__":
    run_main()
