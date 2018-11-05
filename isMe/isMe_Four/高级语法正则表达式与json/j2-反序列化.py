"""
1 我们将我么python的数据类型转换成json字符串的形式我们叫做反序列化 也就是
python数据格式类型转换成str json格式的数据类型

2 不能把序列化后转换成存放在数据库中

3 数据交换的格式

"""
import json

a = [{'name': 'jj'}, {'name': 'jj'}, {'name': 'jj'}]
s = json.dumps(a)
print(s)
print(type(s))
