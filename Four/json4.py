"""

反序列化

"""
"""
pickle 反序列化

只需要函数名称一样即可 但是函数体不一样也是可以的

pickle只能在python本语言中使用

load只能load一次不能load多次
所以dump只能一次一次的dump

"""
import json
#  函数序列化




f = open("text.txt", "r")

# data = pickle.loads(f.read())  # 反序列化 ==  data = pickle.load(f)
data = json.load(f)
print(data)

