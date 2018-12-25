# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/25  17:00'
"""
python中异步IO与协程中的关键点

**** 什么是迭代器什么是迭代协议，其中迭代器中的内容也就是迭代协议中的类容。
1: 迭代器是访问集合内元素的一种方式, 一般的作用就是用来遍历数据,比如说for循环能进行遍历操作,实际上背后是是迭代器起了一定的作用的。 
2: 迭代器和以下标的访问方式是不一样的,就是迭代器是不能返回的,也就是说迭代器只能是一条一条的产生数据，也就是不能单个单个的返回数据。 
   迭代器提供了一种惰性的访问方式，也就是他可以让我们在访问数据的时候，才去计算数据，从而获取到数据，也就是说这个是和我们的list是
   不一样的.
3: [] list 凡事可迭代的对象，都是实现了可迭代协议的，所以说我们可以对他们进行for循环的操作，其中迭代协议也就是这个__iter__这样的
   魔法函数所决定的

4 from collections.abc import Iterable,Iterator 其中Iterable 可迭代对象就是实现了def __iter__(self): 迭代魔法函数,。
5 其中 Iterator 也就是迭代器对象  class Iterator(Iterable):这个迭代器对象也就是继承了Iterable中也就是实现了  这里就拿到了这个迭代器(__iter__)
    @abstractmethod
    def __next__(self):   # 这个魔法函数也就是返回下个 实际上访问数据的就是用的这个next魔法函数, 其实迭代器的核心还是在这个next方法中
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration
    
    def __iter__(self):  # 这里其实已经重载了这个(Iterable)中的迭代器 也就是实现了这里面的魔法函数了 
        return self
6 可迭代对象和我们的迭代器是不一样的，可迭代的对象就是实现了迭代器这个魔法函数, 可迭代也就是只需要实现这个Iterable就叫可迭代，
  但是如果想实现一个迭代器，那么就必须实现next方法也就是Iterator对象，所list只是一个可迭代对象并不是一个迭代器 

7 迭代协议(含有2个概念，第一就是可迭代，第二个就是Iterator)和迭代器的区别  
        
"""
from collections.abc import Iterable, Iterator

a = []
print(isinstance(a, Iterable))  # 也就是说明序列 变为可迭代对象
print(isinstance(a, Iterator))  # 也就是说明序列 是可迭代对象，但并不是迭代器
