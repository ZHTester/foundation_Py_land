"""
元字符与普通字符

"""
import re

a = '23322python(((dddddd322423#C00oobeij'
"""
正则表达式
1 re.findall('正则表达式', 所有匹配的字符串) 返回的列表查询的数据
2 \d 代表数字0-9
3 元字符\d 普通字符 'python' 正则表达式的组合字符 
4 我们学习正则表达式就是学习各种各样的元字符
5 多去找找正则表达式的列表
"""
b = re.findall('\d', a)
print(b)
print("~~~~~~~~~~~~~~~~~~~~~~")
b1 = re.findall('\D', a)  # 保留非数字
print(b1)
