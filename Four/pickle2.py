"""
pickle 反序列化

只需要函数名称一样即可 但是函数体不一样也是可以的

pickle只能在python本语言中使用

"""
import pickle
#  函数序列化


def sayHi(name):
    print('hello', name)


f = open("text.txt", "br")

data = pickle.loads(f.read())  # 反序列化
print(data["func"]('chengdu'))

