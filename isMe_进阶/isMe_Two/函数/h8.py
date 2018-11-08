"""
可变参数
1 尽量保证函数的形参列表的数据类型的简单性
2 函数的设计越复杂就不是一个好的函数和

"""


def demo(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)


demo("a", 1, 2, 3)  # 这样打印出来的值就是 a,1,(1,2) 直接修改了param2的默认值

print("~~~~~~~~~~~~~~~~~~~~~~~~")


def demo2(param1, *param, param2=2):
    print(param1)
    print(param)
    print(param2)


demo2("a", 1, 2, 3)  # 这样打印出来的值就是 a , (1, 2, 3) , 2 计算机还是会默认认为param2是他的默认值
demo2("a", 1, 23, 4, param2="aaa")
