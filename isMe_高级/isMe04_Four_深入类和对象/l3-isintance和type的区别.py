"""
isintance_type

对象的包含关系判断  - is -  判断对象是否相等

"""


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))  # 这个是继承链上的关系-判断我们的数据类型
print("-------------------------------")
print(type(b))
print("-------------------------------")
print(id(B))
print(id(b))
print(type(b) is B)  # 内存地址的指向-is也就是判断对象是否相同
print(type(b) is A)  # 两者的id是不相等的 所以就是false


