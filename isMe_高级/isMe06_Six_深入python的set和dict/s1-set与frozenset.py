"""
1 set 可变集合(无序的集合，不重复的集合) 和 fronzenset 不可变集合，集合最大的特点就是不重复，去重的时候使用最好。 去重的时候是最好使用的一种情况
2 set(iterable) -> new set object  这里就是一个可迭代的对象 也就是集合 - set
3 集合中常见的运算 -  & /  也就是数学运算  实际上这里也是实现了一堆的魔法函数
4 dict 也是常见的使用数据结构类型
5 set的性能是十分的高的, 他们背后都是实现的hash的计算方式，所以set在我们去重复的时候是十分的有效的
6 如何判断一个元素是否在set当中，我们可以是用
    if  'c' in resset:  #set 是实现了

    def __contains__(self, *args, **kwargs):魔法函数
        print(c)
    else:
        print("我没有在这个数组当中")


7 def issubset(self, *args, **kwargs): # real signature unknown
7.1 这个魔法函数实现了判断一个set是否是另外一个set的一部分 或者说
7.2 另一个集合是否包含这个集合。

    这个就是在set中的数学运算符，如何运算的魔法函数中的使用
    def __ior__(self, *args, **kwargs): # real signature unknown
        Return self|=value
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
         Return self-=value.
        pass

8 frozenset 与 set  其实很多方法是一样的 ~但是这两者最大的区别就是 一个是可变的一个是不可变的

"""
s = set('abcderff')  # 无序的集合 不重复性
print(s)
s = {'a', 'b', 'c'}
# s.add('c')
print(s)  # 这样打印出来的数据无序性就体现出来了

# ----- frozenset 不可变的数据类型
# 这里是没有add方法的所以说 frozenset 一旦设置完成后就无法修改了
# -也就是他唯一的好处就是,他就可以作为dict的key- 因为对于dict中的key是恒定的值，所以这点是很重要的。
# s = frozenset("adbde")
# s.add('c')
# print(s)

# ------向set中添加数据 update
anther_set = set("cef")
s.update(anther_set)
print("123", s)

# ------difference 存在a中的数据同时不存在b 差集
anther_set = set("cef")
res_set = s.difference(anther_set)  # s.difference 这里是做了一个返回值的，不是实际上把s做了修改的 实际上是反悔了一个新的s
print(res_set)

# ----issubset 这个就是返回 另一个集合是否包含这个集合
o = s.issubset(res_set)
print(o)
