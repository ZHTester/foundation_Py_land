"""
值类型与引用类型
1 int类型称之为值类型 list类型称之为引用类型
2 引用类型当变量值修改后未生成新的数据还是原有的引用
3 值类型是在边边改变数据后生成了新的数据类型
4 引用类型是可变的，值类型是不可变的-生成新的数据类型-只能重新生成新的数据类型
5 int str tuple set dict 是值类型是不可变改变的数据类型
6 list  是引用类型是可改变的数据类型
7 id就是显示变量在内存中的地址


"""

print("-------变量--------")
a2 = 1
b = a2
a = 3
print(a2)
print("------------list--------")
a1 = [1, 2, 3, 4, 5, 6]
print(id(a1))
b1 = a1
a1[0] = '1'
print(id(a1))
print(b1)

"""
字符串的内存地址
字符串会产生新的字符串

"""
print("--------string")
r = "hello word"
print(id(r))
r = r + "chengdu"
print(id(r))

# r[0] = 'uu'  字符串是不可改变的类型
# print(r)
print("----------------不可变的数据类型 int str tuple --------------------")
w = "www"
s = w
w = "wwee"
print(s)

ww = (1, 2, 3, 4, 5, 6)
ss = ww
ww = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(ss)

print("----------------可变的数据类型 list dict set -------------------")
ds = {1, 2, 3, 4, 5, 6, 7}
print(id(ds))
df = ds
ds = {2, 3, 4, 5, 6, 7, 8, 9, 0}
print(id(ds))
print(df)

rt = {"2": "33"}
print(id(rt))
ty = rt
rt = {"e": "ee", "3333": "4444"}
print(id(rt))
print(ty)
