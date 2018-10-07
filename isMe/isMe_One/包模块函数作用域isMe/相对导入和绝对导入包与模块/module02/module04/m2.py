# from .m3 import m
# from ..m1 import m
from ...m5 import m # 在这里就会出现一个错误，表示试图引用超过顶级包的包
"""
表示试图引用超过顶级包的包
ValueError: attempted relative import beyond top-level package

"""
"""
m2 的顶级宝就是 module2

"""
m = 2
print(__package__)
