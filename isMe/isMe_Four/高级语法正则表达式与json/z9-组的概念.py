"""
组的概念

1 python 中用括号括起来就是代表一个组的概念
2 (python){3} 这样就是代表匹配python3次
3 python{3} 这样的表达式就是代表匹配n三次
4 在python中是存在很多组的概念的
5 中括号中没个匹配符的关系是或的关系  括号的关系是组的关系
"""
import re

a = 'PythonPythonPythonPythonPythonPythonnnn'

r = re.findall('(Python){3}', a)  # 组匹配三次
r1 = re.findall('Python{3}', a)  # 这样的编写方式就是代表匹配n三次的python pythonn pythonnn
print(r)
print('***************')
print(r1)
