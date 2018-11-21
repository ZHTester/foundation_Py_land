# coding=utf8
"""
1 序列是python中一种很重要的序列协议 ，python是基于协议来进行编程的  序列类型都是可迭代的对象
2 其中序列类 包含了 :
容器序列  ---->  通过数据存储的类型来区分
list、tuple、deque  ---------> 容器序列也就是我们可以再序列中放入任意数据的数据
扁平序列
str、bytes、bytearray、array.array
-------------------------------------------------
可变序列  ----> 通过序列是否可变来区分
list， deque，bytearray、array  ------>  数据一旦创建是可以改变的 内存地址引用
不可变
str、tuple、bytes, set ------> 数据一旦创建是可以改变的，值引用，如果创建了新的值，那么不会引用旧的值，会引用新的值~

"""
# 容器也就是可以添加任意数据进行的 序列数据类型
my_list = []
my_list.append(1)
my_list.append("2")

print(my_list)
