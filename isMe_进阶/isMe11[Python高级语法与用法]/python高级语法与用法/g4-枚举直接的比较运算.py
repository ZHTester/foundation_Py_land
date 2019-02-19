"""
枚举直接的比较运算

1 两个枚举之间是可以进行一个等值比较的
2 枚举类型不能支持大小比较的但是可以做等值比较的
3 枚举类型是可以做is类型的逻辑变量比较的
4 两个大的不同的类型下相同的枚举类型进行比较是不行的 因为大的类型是不相同的那么及时是枚举类型相同那么就没用

"""

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common:
    YELLOW = 1


Resule = VIP.GREEN == VIP.YELLOW  # 等值比较
Resulet = VIP.GREEN == 2  # 实际上是相等的但是了在python中是不允许这样做比较的
r = VIP.GREEN is VIP.GREEN  # 这里是做的is比较的
r1 = VIP.GREEN is VIP1.GREEN # 不同类型下的比较 那么就是false

print(Resule)
print(Resulet)
print(r)
print(r1)

