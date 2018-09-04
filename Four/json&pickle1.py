"""
反序列化

"""
import json



f = open("text.txt", "r")
data = json.loads(f.read())  # 反序列化
print(data["age"])






















