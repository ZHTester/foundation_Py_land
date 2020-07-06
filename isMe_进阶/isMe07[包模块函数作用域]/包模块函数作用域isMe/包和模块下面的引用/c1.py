# import isMe.isMe_One.包模块函数作用域isMe.模块下面的引用.c2  as mokui  # 命名空间

# from .c2 import a
from .c2 import *
from .c3 import *

"""
from name模块 import * 其中星号是代表所有，但是我们也是导入我们指定的 函数 变量或者其他
当我们导入模块下的时候，一个包下的模块我们就会先执行这个_init_模块文件 
1 这里就执行__init__.py 
2 __init__ 可以做批量导入的工作



"""
# print(mokui.a)
print(a)
print(b)
print(c3.aa)  # 这里是执行了__init__的文件

# print(c)  # c是不允许被导入的
