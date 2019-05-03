# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/25  17:00'

"""
requests http请求验证 : -----> 
1 为什么需要进行Http认证 
2 通过http通讯，我们所有的资源都是可见的，这样的协议我们就可以看待为Https协议 
  其中这个协议就是加了SHL协议 这就是加密的一个操作 
3 http的基本认证 也就是basic 
4 oath认证 与基本认证的写法是差不多的 不会把明文的数据传输给client端 这就是很好的一种http的认证模式

"""
import requests

BASE_URL = 'https://api.github.com/'


def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auto():
    """
    基本认证  ---  这个时候我们就需要提供用户名和密码的
                  基本认证也并不是那么安全的一种认证方式
    :return:
    """
    r = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(r.text)
    print('---------------------------')
    print(r.request.headers)


if __name__ == "__main__":
    basic_auto()
