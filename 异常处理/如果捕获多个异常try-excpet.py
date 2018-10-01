"""
如何捕获多个异常

case1

try:
    try_suite
except Exception1[e]
       except_block1
except Exception2[2]
       except_block2
except ExceptionN[e]
       except_blockN

使用多个Except可以处理多个异常类




case2
try：
    try_suit
except Exception1[e]
    exception_block1
else:
    none_exception

如果没有异常，我们就执行else语句中的代码


"""
f = open('1.txt', 'w')  # 没有就创建一个文件，如果有的话那么就清空文件
f.write("")
f.close()


try:
    f = open('2.txt')
    line = f.read(2)
    num = int(line)
    print("read num=%d" % num)
except IOError as e:
    print("catch IOError",e)
except ValueError as e:
    print("catc ValueError",e)
else:
    print("没有异常哦.........")







