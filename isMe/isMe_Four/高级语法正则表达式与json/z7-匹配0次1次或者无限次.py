"""
匹配0次1次或者无限次
1 数量词的作用 {3-6} 每次匹配3-6个字符集
2 * 是对前面的字符匹配0次或者无限多次
3 + 是对前面的字符匹配1次或者无限多次
4 ？ 是匹配0次或者1次  出去重复  这里的？是作为数量词来做出的
5


"""

import re
a = 'pytho0python1pythonn2pythonnn3pythonnnnn4'

r = re.findall('[a-z]{3,6}', a)  # \d 代表数字的概括字符集  贪婪模式

r1 = re.findall('[a-z]{3,6}?', a)  # \d 代表数字的概括字符集  非贪婪模式 一旦找到了3个字符集就不会再去找第4-6个

"""
第一个pytho 没有n 是匹配了0次 
第二个python 有一个n 也就是匹配了一次 
第三个pythonnn 有两个n  也就是匹配了n次
"""
r2 = re.findall('python*', a)  # * 是对前面的字符匹配0次或者无限多次


"""
第一个pytho 没有n 不匹配
第二个python 有一个n 也就是匹配了一次 
第三个pythonnn 有两个n  也就是匹配了n次
"""
r3 = re.findall('python+', a)  # + 是对前面的字符匹配1次或者无限多次


"""
第一个pytho 没有n 不匹配
第二个python 有一个n 也就是匹配了一次 
第三个pythonnn 有两个n  也就是匹配了n次
"""
r4 = re.findall('python?', a)  # ? 是对前面的字符匹配0次或者1次  这里会打印出5个python


print(r4)
print(r3)
print(r2)
print(r)
print(r1)









