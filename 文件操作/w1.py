"""
1 文件打开的方式
open(name,[mode[buf]])
name: 文件路径
mode: 打开方式 只读r 只写w(文件不存在那么就创建文件，如果文件存在则就要清空文件内容 )有读有写的方式打开r+w+
      a 追加方式打开(文件不存在创建文件), a+追加和读写方式打开

buf: 设置对写文件的大小 -  缓冲buffering大小

rb wb ab rb wb ab 二进制方式打开

2 python读取的方式
read([size]):读取文件(读取size个字节，默认读取全部) 会占用很大的内存空间
redline([size]) 读取一行
readlines([size]) 读取文件，返回每一行所组成的列表 访问列表的形式访问文件

3 python写文件
write(str) 将字符串写入文件
writeline - 一次性能写入多行文件
"""

# 读取文件
f = open('../装饰器/z2.py', encoding='UTF-8')  # 打开文件
c = f.read()  # 读取文件
print(c)
# 写文件
q = open('../2.txt', 'w', encoding='UTF-8')  # 只是添加写的权限，那么如果文件不存在，那么文件就会创建，如果文件存在那么就会清空文件
q.write('这是我写的测试数据，请查看')
q.close()

q = open('../2.txt', 'w')  # 如果文件存在，那么文件中的数据全部都会被清空的
q.close()

# 文件追加模式
f = open('../装饰器/z2.py', 'a', encoding='UTF-8')  # 打开文件 文件追加模式
f.write("打印测试数据")  # 在文件末尾追加数据
f.close()

# # 使用w+的方式打开文件
ff = open('1.txt', 'w+')
fff = ff.read()
print(fff)
