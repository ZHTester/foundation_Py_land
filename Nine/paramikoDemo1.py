import paramiko

"""
创建ssh执行命令 
python 自己实现了一个客户端
"""

# 创建SSH对象  ssh客户端
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='localhost', port=22, username='Zhanghao', password='85184499')

# 执行命令  stdin标准输入, stdout标准输入(命令执行结果), stderr 命令执行过程中出现的错误
stdin, stdout, stderr = ssh.exec_command('df')

# 获取命令结果
result = stdout.read()
result2 = stdout.read()
error1 = stderr.read()
print(result)

print("连接成功")
# 关闭连接
ssh.close()


