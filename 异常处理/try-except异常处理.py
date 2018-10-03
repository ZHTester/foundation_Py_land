"""
python try--except 异常处理

try-except 异常处理基本语法
    try:
       try_suite
    :except Exception[e]: # 设置异常的类型
    :exception_block #处理我们捕获异常后面的处理逻辑

1 try 用来捕获try_suite中的错误，并且将错误交给except处理
2 except用来处理异常，如果处理异常和设置捕获异常是一致的，那么我们就会使用exception_block处理异常
  如果捕获的异常不是我们设置的异常，那么他就会被系统所处理

try-except 捕获异常分析

case1
try:
    undef
except:
    print "catch an except"

,
case2
try
    if undef
except:
    print"catch an except"


case1 可以捕获异常 因为是运行时错误
case2 不能捕获异常，因为是语法错误，运行前错误


case3 可以捕获异常，因为设置的捕获NameError异常
try:
    undef
except IOError as e:
    print("catch error", e)

case4 不能捕获异常，是因为IOError，不会处理NameError 会往上面抛，就会抛给python解释器，
      解释器就会处理这个NameError，python解释器处理这个NameError就是终止这个程序的执行
try:
    undef
except NameError as e:
    print("catch error", e)

try-except 用例:

需求: 猜数字游戏
     1 开始游戏产生一个1-100的随机数
     2 用户输入，游戏工具输入值提示大或者小
     3 用户根据提示继续输入，直到猜中为止
     4 如果用户输入错误，程序可以处理异常

如果错误没有被捕获，他就会一直往上抛，最后被python解释器捕获，打印一个错误信息，然后程序退出

"""
# 异常处理 -1-
# a = 2
# try:
#     a  # a没定义它就会报错 NameError
# except NameError as e:
#     print('catch Error', e)
#
# print('exec over')


# 异常捕获 -2- 运行后错误 才能捕获异常
# try:
#     undef
# except:
#     print("catch an except")

# 异常捕获 -3- 运行前错误
# try:
#     if undef
# except:
#     print("catch an except")

# case3 抛出正确的异常错误
# try:
#     undef
# except NameError as e:
#     print("catch error", e)

# case4

# try:
#     undef
# except IOError as e:
#     print("catch error", e)
