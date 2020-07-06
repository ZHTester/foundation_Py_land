# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/27  13:40'

"""
python中是如何实现生成器的 ..... 也就是yield的原理
1: python中的函数的工作流程 
   1 python.exe 解释器 - c语言编写的，解释会使用一个pyEval_EvalFramEx()[这本身就是一个C语言的函数]去执行我们的python文件的函数，
   所以我们需要知道的就是python的代码是运行在C程序之上的。 
   2 当c语言的函数去运行python中的函数的时候，首先就是回去创建一个栈, 帧(实际上也就是函数)，实际上栈, 帧，也是一个对象，这就体现了一切
     皆对象的一个理念了，然后了c函数会将我们python中的代码，也变成字节码对象，也就是当foo调用我们的子函数(bar)的时候，他又会去创建一个
     栈, 帧，然后将函数的控制权交个栈, 帧上下文中去运行这样的一个字节码。 
   3 关键点在于所有的栈, 帧 对象都是分配在堆内存上。 他不是放在栈的内存中，而是放在堆内存中。那么这就决定了栈, 帧可以独立于调用者存在.也就是一个递归过程
   
   ---------------------
   1 生成器的一个调用过程也就是利用函数当中的栈, 关键点在于所有的栈, 帧 对象都是分配在堆内存上。 他不是放在栈的内存中，所以我们的生成器才有实现的可能。 
   
-------------------具体可以查看该博客进行学习生成器实现的原理--------------
https://www.cnblogs.com/traditional/p/9221680.html


--------     
   


"""
import dis
import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()  # 这里也就是将bar()的fram赋值给了全局变量


def gen_func():
    yield 1
    name = "landing"
    yield 2
    name = "landing1"
    return "beijing"  # python解释之前，也进行预编译，在编译的过程中，发现有yield，就已经被标记为生成器了


# 可以看到，结果中有两个yield，因为我们的函数中有两个yield
# 最后的LOAD_CONST后面的('i love satori')，表示我们的返回值
# 最后RETURN_VALUE

gen = gen_func()
print(dis.dis(gen))

# 生成器对象中会生成对象 对象中会产生两个方法记录最后一次调用和最近一次的调用
# 前面的图也解释了，gi_frame的f_lasti(这个也就是控制了函数的暂停)会记录最近的一次执行状态，
# gi_locals(这个也就是控制了函数的继续操作)会记录当前的局部变量 这也就是协程中实现暂停与继续实现下去的基础。
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

# print(dis.dis(foo))
# foo()
# print(frame.f_code.co_name)  # 这里就是看栈, 帧 里面到底有什么对象东西 这样就是指向了bar的栈, 帧 对象中

# caller_frame = frame.f_back
# print(caller_frame.f_code.co_name)

