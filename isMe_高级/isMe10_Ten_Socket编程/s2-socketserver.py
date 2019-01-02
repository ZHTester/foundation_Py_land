# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/2  15:59'
"""
socketServer - 服务端


"""
import socket

# 这里指代的就是TCP协议 (socket.AF_INET(指定网络协议), socket.SOCK_STREAM(指定Udp网络协议))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 绑定ip地址
server.listen()  # 监听
# 这里就是监听返回了 socket addrs
sock, addr = server.accept()

# 获取从client接受到的数据 指定一次获取多少数据(单位是字节) 但是这里返回的bytes数据，所以我们这里需要decode一下
data = sock.recv(1024)
print(data.decode("utf8"))
sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))
# 这里都需要关闭 server端与sock端
server.close()
sock.close()
















