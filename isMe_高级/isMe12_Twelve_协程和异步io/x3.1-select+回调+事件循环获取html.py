# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/6  14:38'

"""
select+回调+事件循环获取html   --- IO多路复用也就是并发中应用比较多的技术 --- 这里演示的就是非阻塞式Http请求
--- 通过非阻塞IO实现Http请求 ---
1 这个也就是非阻塞IO在编程中给我们带来的好处



"""
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接 - 非阻塞式IO
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """
    BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
    client.setblocking(False) 这里设置的false是非阻塞式的IO，所以在这样的情况下就是会抛出异常
    
    """
    client.setblocking(False)  # 把client设为阻塞模式那么我们在调用client.connect这个函数的时候是会抛出异常的
    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好， 需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""

    "接收数据的操作,如果上一步操作没完成建立好连接，这一步就会报错"
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue  # 这里也就是如果读取不出值，我们就在这里继续读取值 continue

        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == "__main__":
    import time
    start_time = time.time()
    get_url("https://www.baidu.com")
    print(time.time() - start_time)

    # import time
    #
    # start_time = time.time()
    # for url in range(20):
    #     url = "http://shop.projectsedu.com/goods/{}/".format(url)
    #     get_url(url)
    # print(time.time() - start_time)
