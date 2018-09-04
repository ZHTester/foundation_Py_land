"""


"""
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):   # 每一个请求过来都会实例化MyTCPHandler
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
# 重写handle方法 和客户端所有的交互都在handle完成的
    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))  # 格式化 打印客户端的IP地址

            print(self.data)  # 赋值
            if not self.data: # 代表客户端断开连接了
                print(self.client_address, '断开了')
                break
            self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # 你必须实例化TCPServer并且床底server ip和你上面创建的请求处理类，给这个TCPServer
    # 多并发ThreadingTCPServer
    # server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 多线程
    server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)  # 多进程

    server.serve_forever()





