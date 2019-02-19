# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/14  10:35'
"""
__bool__&&__len__ 对对象True与False的影响 也就是布尔取值  
如果说自定义的类型中没有 __bool__&&__len__ 取值类型，那么则会打印出True
__bool__&&__len__  如果同时有这两种方法，那么我们就只会调用bool方法 而不会去调用len

"""


class Test:
    # pass  # 这样就会默认打印True

    def __bool__(self):  # 如果说 既含有__len__ 与 __bool__ ,那么真正控制对象的True与False的时候，就是由__bool__所决定的
        print("bool caled")
        return False

    def __len__(self):  # 如果是单一的这种魔法函数，那么这样的取值方法都是由len所决定对象的bool值
        print("len caled")
        return 0
        # return True  # 返回bool的值是可以的，返回除开bool值与整型的时候他就会报错啦


# print(len(Test()))  # 这样就是调用函数内部的值 ---- def __len__(self):
print(bool(Test()))
