"""
1 python 中一切都是可以继承的
2 不建议集成dict和list 但是在python当中用c语言实现的这些方法，内置方法，我们是非常不建议去继承这样的方法的。
{# 这里就会打印出了 1 也就类的本身是没有去调用覆盖的方法的 也就是不能完全覆盖dict的子类}

3 defaultdict ----- > 就是dict的子类

其中这里的missing方法就是重写了UserDict中的missing方法
    def __missing__(self, key): # real signature unknown; restored from __doc__

        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory() 如果找不到对应的类那么就会去找这样的类型方法
          return value

        pass

"""
#
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value * 2)
#
#
# my_dict = Mydict(one=1)  # 这里就会打印出了 1 也就类的本身是没有去调用覆盖的方法的 也就是不能完全覆盖dict的子类
# my_dict["one"] = 1  # 这里就会打印出来2 也就是调用了dict本身的方法
# print(my_dict)


from collections import UserDict
from collections import defaultdict

"""
继承了UserDict 也就是实现了全覆盖的方法，如果说确实想全覆盖这样的dict中的方法
"""


class My_dict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = My_dict(one=1)  # 这里继承了UserDict那么也就是实现了全覆盖dict原有的方法
print(my_dict)
