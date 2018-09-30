"""
1 文件打开的方式
open(name,[mode[buf]])
name: 文件路径
mode: 打开方式 只读r 只写w(文件不存在那么就创建文件，如果文件存在则就要清空文件内容 )有读有写的方式打开r+w+
      a 追加方式打开(文件不存在创建文件), a+追加和读写方式打开
buf: 设置对鞋文件的大小 -  缓冲buffering大小

rb wb ab rb wb ab 二进制方式打开

2 python读取的方式
read([size]):读取文件(读取size个字节，默认读取全部) 会占用很大的内存空间
redline([size]) 读取一行
readlines([size]) 读取文件，返回每一行所组成的列表 访问列表的形式访问文件

3 python写文件
write(str) 将字符串写入文件
writeline - 一次性能写入多行文件


"""

f = open('../装饰器/z1.py')  # 打开文件
print(type(f))
c = f.read()  # 读取文件
# print(c)
f = open('../1.txt','w')  # 只是添加写的权限，那么如果文件存在，那么就会创建文件
f.write("test write")  # 文件内容是写入数据进去
f.close()
print()
f = open('../1.txt','w') # 当我们以只写的方式打开文件，如果当前文件存在，那么就创建文件，如果文件存在那么就清空文件。 然后在打开文件
f.close()

f = open('../装饰器/z1.py','a')  # 打开文件 追加文件的模式
f.write("print test..........")  # 在文件结尾处增加新的内容
f.close()

# 使用w+的方式打开文件
f = open('../1.txt','w+')  # 当前文件还是会被清空的
c = f.read()
print(c)

f.write('test W+ write')


















