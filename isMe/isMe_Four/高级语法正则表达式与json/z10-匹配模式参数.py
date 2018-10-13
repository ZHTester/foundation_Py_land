"""
匹配模式参数
findall 第三个参数就是一个匹配模式 flag= 匹配模式


"""
import re

a = "PythonC#\nJavaPHP"

"""
1 有什么办法来忽略字母的大小写了咋正则表达式中的findall就是模式能起的邹勇
2 re.I 匹配模式参数 就是可以忽略大小写 如果没有加匹配模式则不行
3 匹配模式 多个我们就是使用 | 来进行分割 加载的 re.I |
4 c#.{1} 首先匹配C# 这个字符然后在匹配任意一个字符
5 re.S 改变点号的行为能匹配换行符
"""
r = re.findall('c#', a, re.I)  # 不区分大小写

r1 = re.findall('c#.{1}',a,re.I)

r2 = re.findall('c#.{1}',a,re.I | re.S)

print(r2)
print(r1)  # 这里得到的是一个空的列表 因为不能匹配反斜杠的匹配

print(r)
