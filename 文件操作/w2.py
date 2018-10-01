"""
文件的读取方式

2 python读取的方式
read([size]):读取文件(读取size个字节，默认读取全部) 会占用很大的内存空间
redline([size]) 读取一行
readlines([size]) 读取文件，返回每一行所组成的列表 访问列表的形式访问文件
iter： 使用迭代器读取文件

readline(size) len(line) >size  return size
               len(line) >size  return len(line)



"""
#  readline
ff = open('1.txt')
print(ff.readline())  # 默认读取一行数据
# print(ff.readline(5))  # 设置读取文件大小 size byte
print('*************************readline***************************************')
# -------------------------------
# # readlines 读取完文件的大小  6666读取的是字节 每次只是读取缓存想近的数据
# list_c = f.readlines(6666)
# print(len(list_c))
# # f.close()
list_c = ff.readlines()  # 读取所有数据
print(len(list_c)) # 打印出list的长度
print(list_c[-1])
ff.close()

# --------使用迭代器的方式来读取文件--------------

# iter_f = iter(f)
# lines = 0  # 记录行数
# for line in iter_f:
#     lines +=1  # 每记录一行就加1
#
# print(lines)  # 在不消耗大量内存的时候，那么就读取到文件了
