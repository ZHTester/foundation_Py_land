"""
isintance_type

"""


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))  # 这个是继承链上的关系 判断我们的数据类型
print("--------")
print(type(b))
print("--------")
print(id(B))
print(id(b))
print(type(b) is B)  # 内存地址的指向


