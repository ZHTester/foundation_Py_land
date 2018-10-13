"""
字符集

1 字符集使用中括号来代表我们想要概括的字符集 []
2 a[cfh]c  其中a是开始  c是结尾  来确定中间的字符集是什么

3 字符集出现在中括号里面那么就是一个或的关系 也就是满足一个或者多个都可以


"""
import re
s = 'abc, acc, adc, aec, afc, ahc'
c = re.findall('a[cfh]c', s)

h = re.findall('a[^cfh]c', s)  # ^ 非就是匹配字符的反面 取反的操作

i = re.findall('a[c-f]c', s) # 匹配c到f的字符集
print(c)
print("************************")
print(h)
print("************************")
print(i)























