
"""
客户端
"""
import socket
client = socket.socket()

client.connect(('localhost', 6262))

while True:
    cmd = input('>>>：').strip()
    if len(cmd) == 0 : continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024) # 接受命令结果的长度
    print('命令结果的大小', cmd_res_size)

    recvice_size = 0
    recvice_data = b''
    while recvice_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        recvice_size += len(data)
        # print(data.decode())
        # print(recvice_size)
        recvice_data += data
    else:

        print('rescvie_done ....', recvice_size)
        print(recvice_data.decode())



client.close()
