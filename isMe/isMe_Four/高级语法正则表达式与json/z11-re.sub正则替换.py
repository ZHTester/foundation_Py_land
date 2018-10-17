"""

re.sub 正则替换
1 正则表达式 2 替换的表达式 3 需要搜索的元字符串 4 count = 0 默认情况下是0  5 flages =  匹配模式
2 4 count = 0 默认情况下是0 默认情况下 将无限次的匹配下去
3 count就是你匹配替换的最大次数
4 sub 强大的地方就是第二个正则表达式可以使一个函数
5 把函数当做参数传入到正则表达式里面

"""
import re

language = 'PythonC#GO语言PHPC#ffC#fC#rreC#ssC#'

"""
1 这里直接调用的返回值是一个对象
 这里的返回值
<_sre.SRE_Match object; span=(6, 8), match='C#'>
<_sre.SRE_Match object; span=(15, 17), match='C#'>
<_sre.SRE_Match object; span=(17, 19), match='C#'>
<_sre.SRE_Match object; span=(19, 21), match='C#'>
<_sre.SRE_Match object; span=(21, 23), match='C#'>
<_sre.SRE_Match object; span=(23, 25), match='C#'>
    print(vale) 单存的打印

"""


def convert(vale):
    match = vale.group()
    if match == 'C#':
        return "我是你大爷"
    else:
        return "Java"


# r = re.sub('C#', 'GO', language, 0) # GO 正则表达式可以使一个函数
r = re.sub('C#', 'GO', language, 3)
'''
1 使用函数来表示一个正则表达式，那就是匹配正则表达式就是这个函数的穿入职
'''
r1 = re.sub('C#', convert, language, 2)  # GO 正则表达式可以使一个函数  # b = language.replace('C#', 'GO')  # replace 也是字符串的一个替换功能

print(r)  # print(b)
print(r1)


