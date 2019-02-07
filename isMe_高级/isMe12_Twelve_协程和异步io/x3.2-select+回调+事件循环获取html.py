# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/6  15:44'

"""
使用select Http请求
import select  这样的情况下去引出select包的
select.select()
------------
from selectors import DefaultSelector 这里使用的selectors是在select包装下的selectors 使用会更加的方便

1: selectors 其中就包含了epoll 和 poll 这个两个就会在selectors自动选择在win(epoll)下还是在linux(poll)下
   其中DefaultSelector 也是提供了方法的选择
2: DefaultSelector 也提供了注册的方法 将我们的socket注册到select中
3: select中的事件循环，回调实际上是我们自己来进行一个操作的，而并不是代码自己本身完成的

"""
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# 使用select来完成http请求
Selector = DefaultSelector()


class Fetcher:
    # connect 连接回调函数
    def connect(self, key):
        # send 之前我们首先要注销掉我们监控的时间
        Selector.unregister(key.fd)
        # 连接完成之后就是要发送数据
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # 这里的时候我们就需要去监听读的时间
        Selector.register(self.client.fileno(), EVENT_READ, )

    # 接收数据函数
    def readable(self, key):
        Selector.unregister(key.fd)
        data = b""
        "接收数据的操作,如果上一步操作没完成建立好连接，这一步就会报错"
        while True:
            try:
                d = self.client.recv(1024)
            except BlockingIOError as e:
                continue  # 这里也就是如果读取不出值，我们就在这里继续读取值 continue

            if d:
                data += d
            else:
                break
        data = data.decode("utf8")
        html_data = data.split("\r\n\r\n")[1]
        print(html_data)
        self.client.close()

    # 获取url
    def get_url(self, url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
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
        Selector.register(self.client.fileno(), EVENT_WRITE, self.connect)


# 这里我们就需要不停的去循环调用select我们哪一个函数去回调，回调的本身是我们代码自己做的
def loop():
    # 1: select本身是不支持 register模式的
    # 2: socket状态变化以后的回调是由程序员来完成的不是操作系统完成的
    # ready里面就是list，list里面就含有tuple,tuple就是可以使用for循环循环出来
    while True:
        ready = Selector.select()
        for key,mak in ready:
            call_back = key.data  # 拿到我们回调的函数
            call_back(key,)  # 这个方法里面我可以传递一些参数进来


if __name__ == "__main__":
    import time
    start_time = time.time()
    f = Fetcher()
    f.get_url("https://www.baidu.com")
    print(time.time() - start_time)


