"""
dict 其实就是Mapping的一个子类
1 那么dict的 abc抽象基类就是 ----> from collections.abc import Mapping <-----Mapping
  "Mapping"  ----- 不可变的类型
  "MutableMapping" ------> 可修改的类型  -----> dict 其实是属于 MutableMapping
  其中 ----> MutableMapping 继承的是 Mapping
2 其中list和dict 很多的操作方法是差不多的 原因就是  序列类 与  Mapping 都是继承了 ---->
                                            class Collection(Sized, Iterable, Container)
3 MutableMapping.register(dict)  --------------> 这个时候     dict就会被注册到 MutableMapping类中 也就是 从属关系
"""
from collections.abc import Mapping,MutableMapping
dict_name = {}
"""
dict_name 其实并没有继承这个 MutableMapping 这个类 
其实是实现了MutableMapping这个类下面的方法或者说一些魔法函数  所以dict_name 这个变量

"""
print(isinstance(dict_name, MutableMapping))













