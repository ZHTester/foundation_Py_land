"""
把函数作为参数传递给sub

函数调用函数  函数作为参数传递个函数

"""
import re

s = 'A3355599988842DH'


def convert(value):
    matchd = value.group()
    if int(matchd) >= 6:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, s)

print(r)
