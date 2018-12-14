# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/14  11:24'
"""
列表 元组  集合 
1 可迭代对象  迭代器
2 什么是可迭代对象，凡是可被for in循环的数据结构类型，都是可被迭代的对象 
3 什么是迭代器，迭代器是一个对象---> class ，默认情况下能被for in来循环遍历吗
4 由于迭代器可以呗for in循环的，所以迭代器就是一个迭代对象  
5 可迭代的对象不一定就是一个迭代器
---实现了这两个魔法方法，我们就能将一个class对象变为一个迭代器 同时就可以被 for in循环遍历---
    def __iter__(self):
        pass
    
    def __next__(self):
        pass
---
6 对于迭代器我们可以使用next, 但是对于迭代对象，我们是不可以使用next这样的方法的
"""


class Book:
    pass


class BookCollection:  # 一组数据
    def __init__(self, ):
        self.data = ["<明天>", "<还会>", "<更加好>"]
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 当我们所要迭代的对象超出了所需要索引的范围,这里我们就需要做一个判断了,这里我们就需要返回一个 StopIteration
        if self.cur >= len(self.data):
            raise StopIteration
        r = self.data[self.cur]
        self.cur += 1
        return r


book = BookCollection()
book1 = BookCollection()
# # 这样的方法是针对迭代器的
# print(next(book))
# print(next(book))
# print(next(book))

for books in book:
    print(books)

# 第二次是不会打印的，因为迭代器只会打印一次，这就是迭代器的特性，一次性
# 如果说我们想第二次打印这样的迭代器，那么就需要实例化第二个对象
for books in book1:
    print(books)
