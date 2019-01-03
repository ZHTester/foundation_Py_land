# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/2  15:31'
"""
1 socket 也就是处于http请求之下的一种请求模式，也就是基于数据层与传输层之间的一种socket接口
2 request库其实也就是基于urllib来完成的，而这个urllib其实也就是基于socket来完成的，
  所以说socket就是http与传出层之间的接口，就是这样的解释啦. 数据库连接，网络连接，底层都是基
  于socket来完成的一种通讯协议的，所以socket也就是一种接口(在网络5层协议中就是这样的定义)
3  



"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    # 获取从client接受到的数据 指定一次获取多少数据(单位是字节) 但是这里返回的bytes数据，所以我们这里需要decode一下
    re_data = input()  # 手动输入返回数据
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))











