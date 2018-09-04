"""
序列化2

"""

import pickle


def sayHi(name):
    print('hello', name)


info = {
    "name": "Mac hao",
    "age": 18,
    "func": sayHi  # 函数的内存地址
}


f = open("text.txt", "wb")
# print(pickle.dumps(info))  # 序列化  ==  pickle.dump(info, f)
pickle.dump(info, f)
f.close()

