"""
为什么要将文件关闭了
1 将写缓存同步到磁盘中
2 linux系统中每个进程打开文件的个数是有限的
3 如果打开文件数到了系统限制，在打开文件就会失败了


"""