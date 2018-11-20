# coding=utf-8
"""
序列的+、+=和extend的区别

其实+= 就是通过 __iadd__ 魔法函数实现的
    def __iadd__(self, values):
        self.extend(values)
        return self

    def extend(self, values):
    'S.extend(iterable) -- extend sequence by appending elements from the iterable'
    for v in values:
        self.append(v)

    其中 extend 方法 就会将我们的数据 for循环然后在加入到list中去
"""
from collections import abc

# + 的方法 也就是list的连接 也就是内存地址的指向
# c = a + 必须为list序列类型
a = [1, 2]
c = a + [3, 4]
# print(c)

# += 也就是就地加
# a += 这边的数据类型可以为任意的数据类型
a += [3, 4]
print(a)

# [1, 2, 3, 4, 0, 1, 2] extends 没有返回值  append是有返回值的  这里是将数组变为一个迭代对象
# a.extend(range(3))
# print(a)


a.append([1, 23, 4])  # 将数组变为一个值而不是去迭代
a.append((1, 23, 4))  # 将数组变为一个值而不是去迭代
print(a)
