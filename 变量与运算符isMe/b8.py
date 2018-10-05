"""
1 成员运算符  序列可以适用 元组 集合 字符串  列表
2 一个元素是否在一组元素中 这就是成员运算符的作用
3 成员类型的返回值依然使我们熟悉的布尔类型
4 in 是判断在 not in 是判断是否不在
5 字典成员运算符  字典的成员元算是针对 字典中的key value中的key来操作的 判断的是key 不是value


"""

a = 2
b = [1, 2, 3, 4, 5, 6]

print(a in b)

c = 88
print(c not in b)

cc = {'c': 1}
b = 1
print(b in cc)
b = 'c'
print(b in cc)
