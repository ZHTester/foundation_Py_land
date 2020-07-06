# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/28  13:41'
"""
生成器在UserList中的应用 
1 这个UserList也就是用python语言编写的List, 而这个List本身也就使用C语言来编写的  
2 class Sequence(Reversible, Collection): 中的也就是实现了iter(迭代器)
    def __iter__(self):
        i = 0  这个也就是list中的迭代生成对象计数器
        try:
            while True:
                v = self[i]
                yield v   # 这样的方式就是实现了list循环遍历的一个过程了 也就是生成器的一个用法
                i += 1
        except IndexError:
            return


"""
from collections import UserList





































