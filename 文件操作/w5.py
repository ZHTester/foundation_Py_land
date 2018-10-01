"""
python读写文件的问题

1 写入文件后，必须打开才能读取写入的内容
2 读取文件后，无法重新再次读取读过的内容

文件指针，来定位文件的内容 。。。。。。。。。。。。
如何自由的移动文件指针
1 seek(offset[,whence]): 移动文件指针：
2 offset：偏移量，可以为负数；
  whence：移动相对位置

python文件指针定位方式:
1 os.SEEKSET: 相对文件的起始位置 0
2 os.SEEK_CUR: 相对文件的当前位置 1
3 os.SEEK_END: 相对文件结尾的位置 2

文件指针
如果文件的偏移大于了文件的长度那么会发生什么样的情况了？

"""
import os

# r+ 是以读写的方式来打开一个文件的
f = open('2.txt', 'r+')
print(f.tell())  # 显示文件的偏移量 没读取文件那么偏移量就是0
print(f.read(3))
print(f.tell())  # 第3个位置 读取了3个字节出来
f.seek(0, os.SEEK_SET)  # 将位置指会到0的位置了
print(f.tell())
f.seek(0, os.SEEK_END)
print(f.readlines(5))
print(f.tell())
f.seek(0, os.SEEK_CUR)
print(f.tell())
