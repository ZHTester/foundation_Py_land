"""
储存在缓冲器端的多余的数据
手动超时也是不会在发送多余的消息
服务端先发送大小给客户端，客户端在按照这个大小来接收，不断的循环的接收

"""
import socket
import os

server = socket.socket()
server.bind(('localhost', 6565))

server.listen()

while True:
    conn, addr  = server.accept()
    print('new conn', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('客户端已经断开')
            break
        print('执行指令', data)
        cmd_res = os.popen(data.decode()).read()  # 接受字符串， 执行的结果也是字符串
        print('cmd len',len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no data output'
        conn.send(str(len(cmd_res)).encode('utf-8'))  # 先发送大小给客户端
        conn.send(cmd_res.encode('utf-8'))
        print('send done')


server.close()
