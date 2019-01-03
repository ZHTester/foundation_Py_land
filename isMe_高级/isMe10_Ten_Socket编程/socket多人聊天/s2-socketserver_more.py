# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/2  15:59'
"""
socketServer - 服务端

"""
import socket
import threading

# 这里指代的就是TCP协议 (socket发送http请求.AF_INET(指定网络协议), socket发送http请求.SOCK_STREAM(指定Udp网络协议))
# 这里的server也就是监听所需要的
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 绑定ip地址
server.listen()  # 监听


# 这里就是监听返回了 socket发送http请求 addrs 而这里的sock也就是我们client所需要传输进入的sock
# 但是这样的server端只能接受一个请求数据,只要是一个客户端连接进入以后，其实就是在while True中出不来了，也就是
# 这个时候的client就出现了阻塞的状态了，这样就出现了单对单的阻塞了，我们现在就是实现多个人的进入聊天
# sock, addr = server.accept()

def hand_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()  # 手动输入返回数据
        sock.send(re_data.encode("utf8"))


while True:
    sock, addr = server.accept()
    # 这个时候我们就需要实现多线程的方式，来实现聊天室的功能
    # 用线程的方式来处理新接收的连接(用户)
    client_thread = threading.Thread(target=hand_sock, args=(sock, addr))
    client_thread.start()  # 这里我们就是开始启动线程啦 这样的形式我们就是可以实现一个聊天室的功能啦

    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # re_data = input()  # 手动输入返回数据
    # sock.send(re_data.encode("utf8"))
