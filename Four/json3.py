"""
序列化


"""
"""
序列化2

"""

import json

def sayHi(name):
    print('hello', name)


info = {
    "name": "Mac hao",
    "age": 18,
    # "func": sayHi  # 函数的内存地址
}

# 储存了2个字典进去
f = open("text.txt", "w")
f.write(json.dumps(info))
info['age'] = 21
f.write(json.dumps(info))

f.close()

