"""

高阶函数

2 高阶函数
 b: 返回值中包含函数名  - 函数是变量那么返回值也可以包含函数名

"""

import  time

def bar():
    time.sleep(5)
    print('in the bar')


def test2(func):
    print(func)
    return func


# print(test2(bar))  # 返回两个 <function bar at 0x101d60ea0> 第二个<function bar at 0x101d60ea0>是test2的返回地址

# t = test2(bar)  # 直接将函数返回结果返回给t
# print(t) # 将函数的返回值t赋值并且当做变量打印出来
# t()  # 直接使用t(）来调用函数
bar = test2(bar)  # 将原有的bar覆盖了 test2将bar加上了新功能
bar()   # 函数的调用方式在其他函数修饰的情况下不会发生改变了












































