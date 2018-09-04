import copy

"""
列表的使用

cpoy

1 列表中是否还能包含列表
2 浅copy copy只是copy第一层
3 深入copy不能乱用因为在大多数的情况下都不需要完全独立的两份列表
4 在切片中0和-1都是可以省略的
"""
# *************************************************
"""
这段代码讲的就是浅复制
"""

# name = ['tomcat1', 'tomcat2', 'tomca3', 'tomcat4','tomcat4',['tom','jom']]
#
# name2 =name.copy()
# print(name)
# print(name2)
#
# name[2] = "北京"
# name[5][0] = '日本'
#
# print(name)
# print(name2)  # 浅copy 只是copy第一层，如果还需要深入的去说，那么我们就需要去学一下内存地址与内存指针的相关内容了 ？ 与引用相关内容了。
#
#
# name = name2  # 这样的话name2内存地址都是不会改变的

# *************************************

"""
这段代码讲的就是深入复制

"""
name3 = ['tomcat1', 'tomcat2', 'tomca3', 'tomcat4', 'tomcat4', ['tom', 'jom']]

name4 = copy.deepcopy(name3)
print(name3)
print(name3)

name3[2] = "北京"
name3[5][0] = '日本'

print(name3)
print(name4)  # 深入copy 这样的话我们就是完全独立出去两份list出去了

name3 = name4  # 这样的话name2内存地址都是不会改变的


"""
列表的循环
"""
for i in name3:
    print(i)

"""
跳着打印相关数据

"""
print(range(1,10,2))
print(name3[0:-1:2])



