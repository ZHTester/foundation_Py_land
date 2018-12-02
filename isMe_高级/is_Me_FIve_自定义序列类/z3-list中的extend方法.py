# coding=utf-8
"""
序列的+、+=和extend的区别

其实+= 就是通过 __iadd__ 魔法函数实现的
    def __iadd__(self, values):
        self.extend(values)
        return self

    def extend(self, values):
    'S.extend(iterable((序列类型都是可迭代的序列类型)迭代类型的数据类型并不要求必须是一个list))
    -- extend sequence by appending elements from the iterable'
    for v in values:
        self.append(v)

    其中 extend 方法 就会将我们的数据 for循环然后在加入到list中去
"""
from collections import abc

# + 的方法 也就是list的连接 也就是内存地址的指向,不会产生一个新的对象, 在原有的对象上进行引用.
# c = a + 必须为list序列类型 +号也就是数据的连接
a = [1, 2]
c = a + [3, 4]
print(c)
print("**************************")

# += 也就是就地加 不会产生新的list
# a += 这边的数据类型可以为任意的序列类型 list tuple str set
a += [3, 4]
print(a)

# [1, 2, 3, 4, 0, 1, 2] extends 没有返回值返回原有的值
# append是有返回值的  这里是将数组变为一个迭代对象
a.extend(range(3))
print(a)
#
#
a.append([1, 23, 4])  # 将数组变为一个值而不是去迭代
a.append((1, 23, 4))  # 将数组变为一个值而不是去迭代
print(a)

d = [1,2,3,4,5]
d.insert(3, "插入的数据")
print(d)
