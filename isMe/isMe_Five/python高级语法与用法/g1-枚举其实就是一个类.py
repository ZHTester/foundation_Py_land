"""
枚举其实就是一个类
1 如何去描述显示世界中的对象
2 使用各种各样的类型的方式 是枚举
3 在python2中是不存在枚举的这样的一个类型的，但是在python3中是存在枚举这样的一种类型也就是用枚举表示类型

枚举类型

1 但是了在python中枚举的本质还是一个类
2 所有的枚举类型都是Enum的子类
3 python中的枚举就是在类下面定义了一组一组的常量

枚举的可读性: VIP.yellow 这样就可以表示一个枚举类
枚举的标识名字最好全部都是使用大写来表示

1 枚举本身还是个类，但是和我们普通的类还是有区别的

"""
from enum import Enum


class VIP(Enum):  # 这样就是枚举类
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


"""
枚举类下面的变量类型打印出来的就是 VIP.YELLOW 本身，并不是真实的1 
1 打印出VIP.YELLOW 才是枚举的真正意义所在，其实我们在看代码的时候，并不关系yellow的实际数值是1
  数字的1还是2也好，对于我们写代码也好或者说是读代码也好，我要的是数据的类型，我们看到yellow这个字
  我们就知道是黄钻类型，对于普通的应用来说，我们知道这样数据所代表的类型意义就可以了，所以说print(VIP.YELLOW)
  就是VIP.YELLOW 这才是枚举的意义，如果说print(VIP.YELLOW）打印的是1的话，那么枚举的意义就不存在了
  
虽然对于每种枚举的类型来说，都有一个名字和具体的取值，但是我们通常需要关心的是这样的一个名字，而不是他的取值 
因为名字对于我们来说名字才是有意义的，数字并没有意义了，如果说我们显示的数据，那么和普通的类调用变量现实的方式
是一样样的，那么枚举的意义就不复存在了，枚举的意义重在标签，而不是在于他的数值 ，这样的值你可以定义成不同的数据类型
，但是了每个数据类型的值是需要不一样的

"""
print(VIP.YELLOW.name)
print(VIP.YELLOW.value)
