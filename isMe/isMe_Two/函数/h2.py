"""
如何定义一个函数

1 在一个函数体里面
  参数列表可以没有
  我们可以使用return来返回函数的value
  如果def函数中没有return语句那么，函数就认为是返回的None的空值


1 函数的调用顺序需要知道
2 学好参数是学好函数的基础
3 一旦函数碰到return语句后，那么return后面的语句是不会被执行的
4 动态性遇到对返回结果的类型是没有一个限制的 可以是一个list 可以是一个元组 也可以是一个str
5 

"""

"""
这样的编写方法就会导致无限递归报错

  [Previous line repeated 995 more times]  # 递归超过了995次
RecursionError: maximum recursion depth exceeded
"""
import sys

sys.setrecursionlimit(1000)  # 手动设置递归的次数限制


def printl(code):
    print(code)
    return "遇到return中不会被执行的"
    print("123")  # 遇到return不会被执行的


def add(a, b):
    return a + b


a = add(1, 2)


b = printl("python")


"""
1 首先运行到 a = add(1,2) 那么将没被打印   
2 在运行到 b = printl("python") 这里的函数就会返回 print(code)那么就会返回 python
3 然后在执行 print(a,b) 首先会执行add 返回的a 3 后面那个打印函数是没有return 则就会返回none 
"""
print(a, b)
