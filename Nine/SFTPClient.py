"""

用于连接远程服务器并执行上传下载
上传或者下载文件

"""

import paramiko

# 创建好一个连接 并且创建好实例 这本身只是一个建立的通道 sftp
transport = paramiko.Transport(('192.168.0.107', 22))
transport.connect(username='', password='')

# 传输协议是在SFTPClient中定义完成的
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/Users/zhanghao/test.py', '/')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')
print('OK')

transport.close()




















