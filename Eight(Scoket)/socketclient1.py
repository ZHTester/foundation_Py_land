"""

网络发送都是存在缓存区 发送视频文件
r

"""
import socket
"""
客户端
"""
# 申明socket 类型同时生成socket连接对象 ， 协议类型 申明地址簇
client = socket.socket()
client.connect(('localhost', 6969))

# '''发送的英文'''
# client.send(b"hhh")
# '''发送中文'''
# client.send('我要发a送中文'.encode('utf-8'))
while True:
    msg = input(">>").strip()
    if len(msg) == 0:continue  # 如果输入的字符长度是0 那么就是继续编写
    client.send(msg.encode('utf-8'))
    data = client.recv(1024000000)  # 手机1024个字节
# print("recv:", data.decode())  #发送中文decode
#     print("recv:", data.decode())  # 发送中文decode
    f = open('copy12.avi', 'wb')
    f.write(data)
    f.flush()
    # f.close()

client.close()






