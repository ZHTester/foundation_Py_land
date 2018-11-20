"""
序列类型中的协议 :
1 from collections import abc   和我们容器序列相关的协议都是存放在collections下面的 abc模块下的
2 "Sequence",---> 不可变的序列类型 "MutableSequence", ------> 可变的序列类型 这两个是序列相关的抽象基类
   内置的抽象基类可以帮助我们更加快速的理解python中内置的数据结构，常用的数据类型是什么样子的
   其中Sequence是比MutableSequence 更加基础的基类 也就是子类
3 "Sequence",---> 不可变的序列类型  这些魔法函数的构成了我们不可变的数据类型协议，
   所以我们的不可变的序列类型都必须满足这样的接口,或者说这样的特性，他才能构成我们不可变的序列类型数据。
class Sequence(Reversible（数据的反转 abc---cba）, Collection):
Collection   -----> class Collection(Sized, Iterable, Container): ----> size 实现len方法计算我们Collection的长度
                                                                        iterable 迭代器 我们就可以进行for循环 也就是可迭代的
                                                                        Container 我们就可以使用if in

4  MutableSequence -------> 可变的序列数据类型
**2** 可变数据类型与不可变的数据类型最大的区别就是在于 添加值与删除值 __setitem__（添加值） &&  __delitem__（删除值）
class MutableSequence(Sequence):

    @abstractmethod 抽象方法
    def __setitem__(self, index, value):
        raise IndexError

    @abstractmethod
    def __delitem__(self, index):
        raise IndexError

而且 可变的序列数据类型还含有很多函数 -----> 具体查看源码
    def append(self, value):
        'S.append(value) -- append value to the end of the sequence'
        self.insert(len(self), value)

    def clear(self):
        'S.clear() -> None -- remove all items from S'
        try:
            while True:
                self.pop()
        except IndexError:
            pass

    def reverse(self):
        'S.reverse() -- reverse *IN PLACE*'
        n = len(self)
        for i in range(n//2):
            self[i], self[n-i-1] = self[n-i-1], self[i]

    def extend(self, values):
        'S.extend(iterable) -- extend sequence by appending elements from the iterable'
        for v in values:
            self.append(v)


1 这些整个的魔法函数以及方法就构成了我们序列类型的协议
2
"""
from collections import abc