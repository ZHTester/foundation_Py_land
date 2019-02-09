# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/9  13:32'
"""
select+回调+事件循环获取html2 

1 回调 register ----> 注册事件 
2 事件循环 ----> 回调事件循环  
3 实现事件循环的好处  ---> --1-- 并发性高
                         --2-- 目前我们使用的是单线程而没有使用多线程的方式


"""
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# 使用select来完成http请求
selector = DefaultSelector()
urls = ["https://www.baidu.com"]
stop = False


class Fetcher:
    # connect 连接回调函数
    def connect(self, key):
        # send 之前我们首先要注销掉我们监控的时间
        selector.unregister(key.fd)
        # 连接完成之后就是要发送数据
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # 这里的时候我们就需要去监听读的事件
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    # 接收数据函数
    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            # 如果读出数据为空,那么这个时候我们的代码就是读完的状态，这个时候我们就需要撤销回调函数
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            # 如果我们已经处理完成了一个urls，那么这个时候我们就主动移除这个urls
            urls.remove(self.spider_url)  # 这里获取的就是，我们传递进来的url
            if not urls:  # 判断urls是否为空
                global stop
                stop = True

    # 获取url
    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass
        # 注册 也就是将client注册到 DefaultSelector
        """
        def register(self, fileobj, events, data=None):
        ---
        Selector.register(self.client.fileno(), EVENT_WRITE)
        这句话的意思就是我们监控了这个socket然后我们的时间是写
        然后就回去调用这样的回调函数逻辑
        ---
        fileobj  <---> 这个也就是指代的是socket 
        events  <---> 这个也就是指的是事件 
        data=None <---> 这个也就是回调函数(这个回调函数还是十分的重要的) select 都是回调模式组成的
        ---
        self.client.fileno() 这个也就是指代文件符
        EVENT_READ,EVENT_WRITE -这个是写事件与读事件-
        """
        selector.register(self.client.fileno(), EVENT_WRITE, self.connect)


# 这里我们就需要不停的去循环调用select我们哪一个函数去回调，回调的本身是我们代码自己做的
def loop():
    # -回调+事件循环+select(poll,epoll),这些回调都是牵涉到协程多路复用都是采用这样的模式进行的,
    # -事件循环，在我们使用IO多路复用的时候，都会存在
    # -事件循环, 不停的请求socket的状态，并调用对应的回调函数。
    # -1: select本身是不支持 register模式的。
    # -2: socket状态变化以后的回调是由程序员来完成的不是操作系统完成的。
    # -ready里面就是list，list里面就含有tuple,tuple就是可以使用for循环循环出来。
    while not stop:  # 这里我们将不会使用循环的模式进行读取了，而是采用判断全局变量的方式来进行
        # 1 这样的情况是会在win上会出现的，在Linux上是不会出现的)如果select传入的值为空，
        # 2 那么实际上这里是会抛出异常的  r, w, x = select.select(r, w, w, timeout)
        # 3 OSError: [WinError 10022] 提供了一个无效的参数 - 这里就会报错但是仅仅限于win会出现这样的报错，在linux上是不会出现这样的报错的。
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data  # 拿到我们回调的函数
            call_back(key)  # 这个方法里面我可以传递一些参数进来


if __name__ == "__main__":
    import time
    start_time = time.time()
    f = Fetcher()
    f.get_url("https://www.baidu.com")
    loop()
    print(time.time() - start_time)
































