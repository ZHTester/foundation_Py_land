"""

json序列化
 字典的数据类型 存储和到了内存中，
 这样的一个过程叫做序列化
 json 只能处理简单的语法 字典 元组 
 json是不同语言进行交互
 
 
"""''
import json


def sayHi(name):
    print('hello', name)


info = {
    "name": "Mac hao",
    "age": 18,
    "func": sayHi  # 函数的内存地址
}


f = open("text.txt", "w")
print(json.dumps(info))  # 序列化

f.write(json.dumps(info))

f.close()
