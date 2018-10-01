"""
文件的写入方式

3 python写文件
write(str) 将字符串写入文件
writeline - 一次性能写入多行文件 参数可迭代的对象 可以是个字符串，也可以是个字符串所组成的元组 也可以使一个字符串组成的迭代器，也可以使一个迭代器所组成的列表

4 python磁盘机制
 1 主动调用close或者flush方法 写缓存同步到磁盘
2 写入数据量大于或者等于写缓存，写缓存同步到磁盘中
"""
f = open('2.txt', 'w')  # 没有就创建一个文件，如果有的话那么就清空文件
f.write('test111 write\n')  # 写入数据到一个文件中
f.write('123456789\n') # 参数必须是由字符串组成的序列
# f.close()

f.write('test wrte')
f.flush()
# f.close()

"""
如果文件写入过大，那么就存在缓存中

"""
for i in range(1000000):
    f.write('test' + str(i) + '\n')
