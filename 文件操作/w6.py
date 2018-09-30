"""
1 文件对象的属性
  1 file.fileno() 文件描述符号
  2 file.mode  文件的打开权限
  3 file.encoding 文件的编码格式
  4 file.closed() 文件是否关闭

2 标准文件
 1 文件标准输入： sys.stdin:
 2 文件标准输出： sys.stdout;
 3 文件标准错误： sys.stderr


3 文件命令的行的参数
    1 我们执行程序，如果能根据参数不同完成不同的功能，那是多么的美好
    2 sys模块提供了sys.argv 属性，通过该属性可以得到命令行参数
    3 sys.argv 字符串组成的列表

4 文件编码格式
    1 使用普通的方式打开文件: 写入u 非洲，会出现什么问题了
    2unicode 转码为'utf-8 然后写入到文件中
    3 问题来了 我们如何创建一个utf-8或者是其他编码格式的文件了
      使用codes模块提供方法创建制定编码格式文件
      open(fname,mode,encoding,errors,buffering)
            使用制定编码格式打开文件


"""
import sys
import os
import codecs

f = open('../landing.txt','r+')
print(f.fileno())  # 文件的描述符

print(f.mode) # 查看文件的权限
print(f.closed)  # 查看文件的关闭状态 返回的是false那么就是没有关闭的状态
print(f.encoding) # 返回文件的编码格式
# 标准文件
print(type(sys.stdin))
print("****************************************************")
# 文件的编码格式

# print(f.read())
# f.write('123\n')
# f.write(u'成都')
# b ="南非"
# a =b.encode("utf-8")  # 转码
# f.write(a)0
# f.seek(0,os.SEEK_SET)
#
# print(f.readlines())

"""

      使用codes模块提供方法创建制定编码格式文件
      open(fname,mode,encoding,errors,buffering)
            使用制定编码格式打开文件

"""

f = codecs.open("../1.txt",'w','utf-8')
print(f.encoding)


































