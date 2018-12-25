# ecoding=utf-8
"""

1 from collections import abc   和我们容器序列相关类都是存放在collections下面的 abc模块类下面 __all__ 下面
__all__ = ["Awaitable", "Coroutine",
           "AsyncIterable", "AsyncIterator", "AsyncGenerator",
           "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
           "Sized", "Container", "Callable", "Collection",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           "ByteString",
           ]
2 其中 "Sequence"(不可变抽象基类), "MutableSequence(可变的抽象基类)", 都是序列容器中的抽象基类 。
3 MutableSequence 是在 Sequence 的基础上添加了一些方法 所以说Sequence是更加基础的抽象基类
4 class Sequence(Reversible, Collection): 实际上是继承了Reversible, Collection 这两个类，让后了Reversible
  实际上是实现了数据的反转，而Collection 是继承了 class Collection(
  Sized(实现了len方法，这样我们就可以去计算这样的一个长度),
  Iterable(实现了__iter__这样的抽象基类，这么继承了这样的方法，我们就能实现继承这个抽象基类的for循环方法了),
  Container(实现了这个def __contains__(self, x):抽象基类，这样我们就能对序列进行 if in not in的判断了)):

5 MutableSequence 可变的序列，其中与Sequence的区别就是多了setitem 与 delitem 可以添加值与删除值，这样就是构成了我们的
  可变序列的基本因素。
     @abstractmethod
    def __setitem__(self, index, value):
        raise IndexError

    @abstractmethod
    def __delitem__(self, index):
        raise IndexError

6 抽象基类也就构成了python中序列协议  实现抽闲基类中的方法，就具备了这样的协议中的特性
"""
from collections import abc

