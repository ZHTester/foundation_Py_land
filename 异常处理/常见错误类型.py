"""
python 常见错误

1 a: NameError 变量为定义那么就会报名称错误
2 if True :sytaxError 语法错误
3 f = open('1.txt') : IOError IO流的错误
4 10/0: ZeroDivisionError 报0错误
5 a = int('dd') ：ValueError 传入值的错误
6 KeyboardInterrupt 中断错误 执行过程中的错误


"""
# a   # 变量名称错误


# if a  # 语法错误

# f = open('test.txt') IO流错误

# print(10/0) 报0错误

# a = int('a100') 值错误
# print(a)

import time
for i in range(10):
    time.sleep(2)




