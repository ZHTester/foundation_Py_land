""""
模块内置变量


"""

"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__']

1 dir（） 就是返回当前模块的所有变量的方法
2 双下划线是python定义好了的内置变量 '__name__', '__package__'
3 报错的信息包含 堆栈错误信息与具体的错误信息
"""
# a = 1
# b = 2
# c = 3
#
# infos = dir()
# print(infos)



print("name:"+__name__)   #
print("package:"+__package__)
print("doc:"+__doc__)  # 展示的是模块的注释
print("file:"+__file__)  # 指定文件的物理路径
