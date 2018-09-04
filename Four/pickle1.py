"""

pickle 序列化


"""''
import pickle


def sayHi(name):
    print('hello', name)


info = {
    "name": "Mac hao",
    "age": 18,
    "func": sayHi  # 函数的内存地址
}

f = open("text.txt", "wb")
print(pickle.dumps(info))  # 序列化

f.write(pickle.dumps(info))

f.close()
