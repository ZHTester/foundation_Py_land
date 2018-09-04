"""

shutil 模块就是copy文件使用的

高级的 文件、文件夹、压缩包 处理模块


"""
import shutil

f1 = open('__init__.py')

f2 = open('initcopy111.py', 'w')

shutil.copyfileobj(f1, f2)

print('copy 完成')



