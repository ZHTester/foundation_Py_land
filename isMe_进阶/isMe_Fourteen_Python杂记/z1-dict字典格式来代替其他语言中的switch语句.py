"""
1 dict字典来代替其他语言中的switch
2 通过字典的映射，我们是可以达到这样的一个代替switch语句的一种效果
3 key对应的不仅仅可以是个字符串也可以是一个函数
4 方法后面加上括号就能执行这样的一个方法了
5 字典映射是很简单的用法 ~
6

"""


# 传统的方式进行dict的形式替换switch的方式
# day = 6
#
# sitching = {
#     "今天": "周四",
#     "昨天": "周三",
#     "明天": "周五"
# }
#
# # day_name = sitching[day]
# day_name = sitching.get(day, "你输入的数据不存在")  # 在Python中我们也可以使用get方法来进行获取数据的
#
# print(day_name)


# 用函数的方式进行访问的方式进行访问


day = 0


def today():
    return "今天"


def yesterday():
    return "昨天"


def tomorrow():
    return "后天"


def deflut():
    return "啥都没有"


sitching = {0: today, 1: yesterday, 2: tomorrow}


day_name = sitching.get(day,deflut)()
print(day_name)
