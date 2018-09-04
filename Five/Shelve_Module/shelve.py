"""

shelve模块是一个简单的key,value 将内存数据通过文件持久化的模块，
可以持久化任何pickle可支持的python数据格式

"""
import shelve
import datetime

d = shelve.open('shelve_test')  # 打开一个文件
# 读取文件
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))


# 持续化列表
info = {'age': 22, 'job': 'it'}
name = ["alex", "rain", "test"]

d["name"] = name  # 持久化列表
d["info"] = info  # 持续化列表 dict
d['date'] = datetime.datetime.now()

d.close()
