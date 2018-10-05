"""
 身份运算符 is not is

1 身份运算符返回的结果也是我们是熟悉的boole类型的返回值
2 如果两个变量的取值想的，那么is 的返回结果 就是true

3 身份运算符与关系运算符的区别  is ==
4 关系运算符比较的 值是否相等， 身份运算符比较的是两个变量 身份是否相等也就是比较内存地址是否相等id()
4 is 是表示一个变量的身份是否和另外一个变量的身份地址是否相同
5 not is 是表示一个变量的身份地址是都和另外一个地址相同

"""

a = 1
b = 2
c = 1
print(a is b)
print(a is c)

print("-------------------")
# 3 身份运算符与关系运算符的区别  is ==
cc =1
bb = 1.0
print(cc is bb)
print(cc == bb)
print("------------")
# list 是无须的
aa = {1,2,3}
bb = {2,1,3}
print(aa == bb)
print(aa is bb)

print("-----------")
"""
# 元组是有序的

"""
aaa = (1,2,3)
bbb = (2,1,3)
print(aaa == bbb)
print(aaa is bbb)
