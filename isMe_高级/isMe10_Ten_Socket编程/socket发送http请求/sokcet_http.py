# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/2  18:43'
"""
1 socket 也就是处于http请求之下的一种请求模式，也就是基于数据层与传输层之间的一种socket接口
2 request库其实也就是基于urllib来完成的，而这个urllib其实也就是基于socket来完成的，
  所以说socket就是http与传出层之间的接口，就是这样的解释啦. 数据库连接，网络连接，底层都是基
  于socket来完成的一种通讯协议的，所以socket也就是一种接口(在网络5层协议中就是这样的定义),只是基于
  每种语言封装的接口类型不一样而已。 

from urllib.parse import urlparse ---- urlparse其实就是用来解析url的，这里并不是用来发起socket连接的

"""
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html页面
    url = urlparse(url)  # 这里也就是传入的url的host的
    host = url.netloc  # 这里也就是创建了host
    path = url.path  # 这里也就是得到了URL的子路径
    if path is None:
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 8000))  # 这里是可以传入一个Url的地址的
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    print(data)
    client.close()


if __name__ == "__main__":
    # http 返回都是返回出了一个http字符串了
    get_url("http://www.baidu.com")


