"""
1 认识正则表达式
1 正则表达式是一个特殊的字符串序列，一个字符串是否使我们设定的这样的字符序列相匹配
  快速检测文本，实现一些文本的替代操作。

1 优先的使用python内置的函数来进行数据的判断，当我们所使用的python函数不能满足我们的时候，我们就需要去
考虑正则表达式的方式去编写饿
2 re正则表达式
3 正则表达式最主要的是规则

"""
import re
a = 'java|python|c#|beij'
# print(a.index('python') > -1)  # 代表这个表达式存在python
# print('python' in a)
"""
正则表达式
1 re.findall('正则表达式', 所有匹配的字符串) 返回的列表查询的数据

"""
s = 'python'
b = re.findall(s, a)

if len(b) > 0:
    print("字符串中包含了%s" % s)
else:
    print('字符串包含这个数据类型')


