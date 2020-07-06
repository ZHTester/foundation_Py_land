"""
枚举类型枚举名称与枚举值
如何通过枚举下面的标签值，来获取枚举下面的数值了

"""
from enum import Enum

a = {"黄钻": 3, "紫钻": 2}

a["紫钻"] = 3
print(a)

"""
枚举的第一个好处就是数据的不可变性 
枚举不能有相同的标签 也就是不能重复的使用标签
如果试图的修改枚举下面的标签 那么就会报错，因为枚举的类型的标签是不允许被修改的

"""


class VIP(Enum):  # 这样就是枚举类
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class common:
    YELOW = 1  # 实际意义上他还是一个变量 看着是

"""

枚举类型的访问方式就是通过value来访问 VIP.GREEN.value  获取枚举的值 
通过.name属性来得到标签的名称的

1 枚举的名称和枚举的本身并不是一个东西
枚举类型  枚举的名字  枚举的值的什么区别了  这个就需要百度一下了

"""
print(VIP.GREEN.value)  # 访问标签属性下面的值  枚举值
print(VIP.YELLOW.name)  # 访问标签的属性名称 这个得到的是一个str类型 枚举名称
print(VIP.YELLOW)  # 这个直接得到的值是一个Enum的类型  打印的也就是enum数据类型 美爵类型
print(VIP['GREEN'])  # 这样的打印就是会直接打印出枚举类型

print('----------对于一个枚举来书是可以进行遍历的-----------')

for v in VIP:
    print(v)


















