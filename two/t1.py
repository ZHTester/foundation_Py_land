"""
列表操作 相关方法的使用


"""


name = ['tomcat1', 'tomcat2', 'tomca3', 'tomcat4','tomcat4']
print(name.count('tomcat4'))   # 统计tomcat4 有多少个
name.append('tomcat5')
name.insert(1,'tomcat6')   # 放入相关的位置 下表位置
# 一个列表中有相同的值，那么我现在如何统计有多少个相同的值了

name[2] = 'tomcat8'   # 修改

name.remove('tomcat4')  # 删除方法
del name[1]  # 删除方法

print(name.index('tomcat8'))   # index 其实就是索引的意思 这个方法就是查找出一个列表中 相关数据的位置
# print(name.index('landig'))  # 我们看一下 这里是找不到这个名字的，我想问一下这样打印会出现什么样的情况了  ？？？？？
print(name)

print(name[1])     # 取值 tomca1
print(name[1:3])   # 取值 tomcat2 与 tomca3  开始的位置包括，结束的位置不包括 有头没尾巴 ~ 切片
print(name[0:3])
print(len(name))
print(name[-1])
print(name[-2:])   # 取出的值 是tomcat3 和 tomcat4
print(name[:3])    # 打印出来的值是啥？


print(name)
name.reverse()   # 将现有的list数据列表顺序完全翻转了
print(name)

# name.clear()   # 清空
# print(name)

name2 = [1,2,3,4,5]
name.extend(name2)  # 合并
print(name)





















