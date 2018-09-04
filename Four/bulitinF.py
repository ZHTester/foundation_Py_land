"""

内置方法

"""
# all() 方法解释 如果这个可迭代的对象里面所有元素都为True那么就返回True
a = all([0, -55, 5])
print(a)

# any  这个列表或者这个可迭代的数据里面任意的一个数据为True那么就返回True，如果这个列表是空那么也就是返回flase
b = any([0, -55, 5])
print(b)

# ascii() 返回一个字符串的包含一个print包对对象的表现形式打印出来
c = ascii([1, 2, '成都'])
print(c)

# bin()  10进制转换成2进制
print(bin(255))

# bytearry 可修改的2进制格式
# 字节的数组 字符串是不能修改 如果要修改字符串必须生成一个新的
d = bytes('abcder', encoding='utf-8')
e = bytearray('abcder', encoding='utf-8')
print(d.capitalize())
print(e[0])  # 打印accis码


# callable() 验证是否可以调用
def ss():
    pass


print(callable(ss()))

# chr() 返回这个字符串的表现形式
print(chr(98))

# classmethod 类方法装饰器


# eval() 把一个字符串变成一个字典

# filter() 一组数据过滤出你想要的数据

rs = filter(lambda n: n > 5, range(10))
for i in rs:
    print(list([i]))

# map() 方法使用

import functools

# ress = functools.reduce(lambda x, y: x+y, range(10))  # 从0+9
ress = functools.reduce(lambda x, y: x * y, range(1, 10))  # 从0*10
print(ress)

# frozenset 冻结不可变的集合  集合默认是可以修改的
a = frozenset([1, 2, 3, 5, 5, 666, 77, 88, 66])  # 这就是不可变的状态

# hex() 把一个数字转换成16进制
print(hex(16))

# locals()  只是打印局部变量函数
def test():
    locals_var = 333
    print(locals())
test()
# print(globals().get('locals()_var'))



























