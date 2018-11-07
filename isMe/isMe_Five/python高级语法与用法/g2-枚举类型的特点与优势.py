"""
枚举类型的特点与优势

1 如果我们没有这样的一个枚举类，我们如何去表示一个 黄钻 黑钻 绿钻
  答案: 最直接的办法就是使用模块里面的变量来表示这样的一个类型 yellow =1 green =2
       我们第二种方法就是使用字典的形式来表示{"黄钻":"1"} 如果不使用枚举类型 字典可能是一种较为合适表示种类的枚举类型
       第三种方式就是: 类来表示 下面的变量

       第二种与第三种的缺陷就是 1  可以在代码中随意修改这样的数据类型
                            2 没有防止相同值的功能

1 如果是一个类型，那么就不应该轻易被修改的
2 类型一旦被确定是不应该随意修改改变的
3 字典或者说类 运行不同的标签允许有相同的值的
4 没有防止相同标签的一个功能

---------------
在普通的类下面 是没有真正的常量的这一说法的 也就是在普通的类下面是没有真正的类这一说法的
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
    # YELLOW = 1  # 这个也会报错 相同的标签类型
    GREEN = 2
    BLACK = 3
    RED = 4


"""
在普通的类下面 是没有真正的常量的这一说法的 也就是在普通的类下面是没有真正的类这一说法的
虽然下面的看起来是个常量，但是实际上不是一个真正的类型常量因为他是可变的数据类型
"""


class common(object):
    YELOW = 1  # 实际意义上他还是一个变量 看着是
    YELOW = 2

"""

 VIP.YELLOW = 6  # 修改枚举类下面的标签的值就会报错 因为 枚举类下面的标签是不允许被修改的 而且python也有这样的一个保护机制
 
"""
print(VIP.YELLOW.name)
