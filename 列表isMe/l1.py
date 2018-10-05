"""
列表 list
1 俄罗斯方法每个图形就是一个组
2 在python中表示组的方式有很多种

属性:
    list的数据类型可以使多种多样的 字符串 int 布尔类型 嵌套列表

3 通过索引去访问一个list那么得到的是一个字符串，通过列表去取出来的数据是列表类型的
4 字符串的截取方法和列表是一样的

"""

a = [1,2,3,4,5,6]  # 这就是一个列表 list
print(type(a))

b = [1,2,'chengdu',True]
print(type(b))

c =[[1,2,3],[1,2,3],[1,2,3]]
print(c)

d = ['北京','日本','上海','东京']
print(d[3])
print(d[1:3])
print(d[-1:])

# 列表的+
e = a+b
print(e)
f = a*2
print(f)






