"""
元字符与普通字符

表达式中应该是需要具体的常量表达式那么这样
    的正则表达式是无意义的，所以我们需要抽象的常量。

"""
import re

a = '23322python(((dddd322423#C00oobeij'
"""
正则表达式
1 re.findall('正则表达式', 所有匹配的字符串) 返回的列表查询的数据
2 \d 代表数字0-9
3 1元字符\d 2普通字符'python' 3我们的正则表达式就是由一些列的元字符与普通字符组成的
4 我们学习正则表达式就是学习各种各样的元字符 - 这个要切记
5 多去找找正则表达式的列表 百度

"""
b = re.findall('\d', a)
print(b)
print("~~~~~~~~~~~~~~~~~~~~~~")
b1 = re.findall('\D', a)  # 保留非数字
print(b1)
