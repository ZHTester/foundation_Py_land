"""
with as 语法

with context [as var]
 with_suit

1 with 语句来代替try-except_finall语句，使得代码更加简洁
2 context 表达式返回的是一个对象
3 var 用来保存context返回对象，单个返回值或者是元组
4 with_suit 就是使用var变量来对context返回对象的操作

实例1
with open(1.txt) as f:
    for line in f.readlines():
        print line
1 打开1.txt文件
2 f变量接收文件返回的对象
3 with中代码执行完成后，关闭文件

witch语句其实就是一套上下文的管理：
    1 上下文管理协议包含的方法: __enter__() 和 __exit__() 支持该协议的对象要实现这两个方法
    2 上下文管理器：定义执行with语句时候，要建立的运行时上下文，负者执行with语句块上下文中的进入与退出的操作
    3 进入上下文管理器：调用管理器_enter()方法，，如果没有设置as var变量就接受_enter_方法返回值
    4 退出上下文管理器：调用管理器__exit__方法
    

"""

try:
    f = open('1.txt','w')
    f.write('12333333')
    f.readlines(2)
except IOError as e:
    print("catch IOError",e)
except ValueError as e:
    print('catch ValueError',e)
finally:
    print("catch ValueError", f.close())

"""
with as 操作如果文件出错了，那么文件就不会关闭，等到python解释器处理
"""

with open('2.txt','w+') as f1:
    f1.write('12333333')
    print("print read with as")
    f1.read()












