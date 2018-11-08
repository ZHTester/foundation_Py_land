"""
序列解包
链式赋值


1 序列解包元素是需要相等
2
"""
# a = 1
# b = 2
# c = 3
a, b, c = 1, 2, 3  # 精简行
d = 1, 2, 3
print(d)  # 这个打印出来的是一个元组形式  # d是一个tuple
print(a)  # 这个打印出来是一个单数字     #

# a, b, c = d   # 这样的形式就叫做序列解包

"""
1 序列解包元素是需要相等 如果不相等则会报错
ValueError: too many values to unpack (expected 2)

"""
# cc, dd = [1,2,3]
aaa = bbb = ccc = 1
print(aaa, bbb, ccc)
