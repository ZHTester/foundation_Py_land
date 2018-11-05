"""
枚举需要注意的事项
1 标签名不能是一样的
2 不同标签名称可以含有相同的值 也就是数值
3 枚举的遍历 ---- 其中如果含有了枚举的别名那么别名的值是不会被打印出来的
  因为枚举的别名本身就不是一个真正的枚举类型

"""
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    # YELLOW = 1
    GREEN = 1  # 这样它就会成为Yellow的别名并不是一个真正意义上的
    BLACK = 3
    RED = 4


class Common:
    YELLOW = 1


"""
# 这里打印出来的却是yellow 也就是说Green是Yellow的别名 
  其实也就是相同的值 这样的Green本身不能代表一个独立的枚举类型

"""
print(VIP.GREEN)
print('-------遍历是不会打印出别名的枚举类型----------')
for v in VIP:
    print(v)
print('-------通过使用members_items()这样的形式就会打印出每种枚举类型---------')
"""
这样的形式打印出来的数据就是以元组的形式打印出来的
其中第一个数据就是枚举名称 第二就是标签名称+枚举值的一种现世符昂视
"""
for vv in VIP.__members__.items():
    print(vv)

print('-----------枚举值的显示--------------')
"""
直接打印出枚举的名称
"""
for vvv in VIP.__members__:
    print(vvv)

