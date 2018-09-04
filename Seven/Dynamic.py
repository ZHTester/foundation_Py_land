"""
动态导入模块

"""
mod = __import__('lib.aa') # aa
obj = mod.aa.C
print(obj.name)  # 调用的是lib





















