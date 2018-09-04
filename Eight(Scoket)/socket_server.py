# 服务器端

import socket
import os

server = socket.socket()  # 建立连接
server.bind(('localhost', 6969))  # 绑定要监听的端口
server.listen(5)  # 监听 如果是5那么就是默认监听最多5个 只有在异步的情况下才会出现最大限制的问题
print('我要开始等电话了')
# 断开线程继续不断会话
while True:
    conn, addr = server.accept()  # 等待线程的进入 conn对方打过来的实例 addr对方给的地址
    print(conn, addr)
    print('电话来了')
# 循环会话
    while True:
        data = conn.recv(1024)  # 接收消息
        print("recv:", data)  # 显示消息
        if not data :
            print('断开了')
            break
        # res = os.popen(data).read()
        conn.send(data.upper())  # 将消息转换成大写

server.close()
