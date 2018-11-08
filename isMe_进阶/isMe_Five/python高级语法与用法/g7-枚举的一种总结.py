"""
枚举的总结
1 IntEnum 枚举的值必须都是int类型不然就会报错的
2 如果想限制每种枚举类型的值不能取相同的值，那么我们应该怎么办
  我们就需要引入@unique这样的一个装饰器这样他就不会成为一个别名那么就会报错了
3 其实枚举在python中实现的是一种单例模式，也就说在枚举类型中，是不能进行实例化的
  这也就是枚举类型相对于其他类型的一个区别，因为对他实例化也是没有任何意义的，因为他就是一种单例模式的

"""
from enum import Enum
from enum import IntEnum, unique


@unique
class VIP(Enum):
    YELLOW = 1
    # GREEN = 'str'  # 这样他就会报错的
    GREEN = 1
    BLACK = 3
    RED = 4
