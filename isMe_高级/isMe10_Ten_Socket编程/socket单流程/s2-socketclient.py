# coding=utf-8
__author__ = 'landing'
__data__ = '2019/1/2  15:31'
"""
socketClient - 客户端
***********************
socket发送http请求 与 socketServer 通讯
1 通过这个列子我们将区别到socket编程与Https编程的一个区别
*****------******
2 socket编程模式(无论是python还是java socket编程方式都是一样的形式)
*****------******
server端                                      client端
------- 
socket发送http请求
--- sokcet是介于传输层与网络层之间的一个接口(协议)(这个时候也就是协议编程)
--- 每一个应用程序都添加上一个端口这样就能区分不同的应用程序了 这样我们就不需要指明应用了
bind(协议 地址 端口) 
listen(监听客户端socket请求)
accept                                          socket发送http请求
阻塞等待连接请求(新套接字)<------三次握手-----    connect()
recv()<--------------------------------------- send()
--- (只要连接不断开，服务端能一直给客户端发送请求,(而Http请求就是每次发送请求都会经历三次捂手协议))
--- 只要协议不断开，那么我们的连接就不会断开了，这就是客服端应用程序所实现的一种功能
send()----------------------------------------> recv()  
close()<--------------------------------------  close()


server必须随时处于一个监听的状态与服务的状态,因为我不知道客服端不知道什么时候会发送服务请求过来

"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
message = input("输入您的数据")
client.send(message.encode("utf8"))
client.close()










