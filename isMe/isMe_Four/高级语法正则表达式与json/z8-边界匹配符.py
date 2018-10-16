"""
边界匹配符

判断字符的长度 -


"""
import re

# a = '1000001444'
# a = '100000155'
"""
# 加入了 ^与$就可以让我们的表达式完整的匹配正则表达式 判断字符集的长度是否满足
^ 是从正则表达式的字符串开始开始进行匹配
$ 是从正则表达式的结尾开始匹配 第8位结束 如果有大于8位的那么就是为空取值错误了
"""

while True:
    a = str(input("请输入你想要的值"))
    s = re.findall('^\d{4,8}$', a)
    if len(s) == 0:
        print(len(a))
        print('你输入的长度不正确，请重新输入:')
        continue
    else:
        print(len(a))
        print('满足需求')
        print(s, "匹配所得到的字符是不是4-8位")
        break


# aa = '10000000011'
# ss = re.findall('001$', aa)
# print(ss)
