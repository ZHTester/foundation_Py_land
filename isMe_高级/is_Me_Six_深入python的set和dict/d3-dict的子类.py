"""
1 python 中一切都是可以继承的
2 不建议集成dict和list
3 defaultdict ----- > 就是dict的子类

其中这里的missing方法就是重写了UserDict中的missing方法
    def __missing__(self, key): # real signature unknown; restored from __doc__

        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory() 如果找不到对应的类那么就会去找这样的类型方法
          return value

        pass

"""
from collections import UserDict
from collections import defaultdict















