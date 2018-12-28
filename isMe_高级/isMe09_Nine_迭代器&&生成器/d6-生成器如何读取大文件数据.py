# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/28  13:41'
"""
***如何读取大文件的数据***

生成器实现协程的一个重要的点  

"""


def myreadlines(f, newline):
    buf = ""  # 这个变量的名称就是可以理解成缓存东西
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk


with open("input") as f:
    for line in myreadlines(f, "{|}"):
        print(line)





