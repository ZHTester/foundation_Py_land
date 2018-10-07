"""
Traceback (most recent call last):
  File "/Users/zhanghao/pythonScript/foundation_Py/isMe/isMe_One/
  包模块函数作用域isMe/b3.py", line 4, in <module>
    print("package:"+__package__)
TypeError: must be str, not NoneType
"""

import isMe.isMe_One.包模块函数作用域isMe.b2

'''
1 python  是更加容易理解的语言
2 b3 是正常打python模块的入口执行 所以name = __main__
3 b2 这是我们正常的导入模块执行所以 name= 正确的路径名称
***1***如果一个模块被当做是一个引用程序的入口那么他的name变量打印出来的值就是__main__ 而不是程序的本身模块路径 
这就是入口文件，还有就是他的顶级是没有pakage是没有顶级文件的，那么就是notype
4 入口文件与导入文件的内置变量的一个区别一定要清楚
5 file和python执行的命令是有关系的，而不是一层不变的 
6 入口文件和普通文件的取舍
'''
print('~~~~~~~~~~~~~~~b3~~~~~~~~~~~~~~~')
print("name:"+__name__)   #
print("package:"+(__package__ or " 当前模块不输入任何包 ！！！"))
print("doc:"+__doc__)  # 展示的是模块的注释
print("file:"+__file__)  # 指定文件的物理路径

