"""
边界匹配符

判断字符的长度 -


"""
import re

# a = '1000001444'
a = '1000001'
"""
# 加入了 ^与$就可以让我们的表达式完整的匹配正则表达式 判断字符集的长度是否满足
^ 是从正则表达式的字符串开始开始进行匹配
$ 是从正则表达式的结尾开始匹配 第8位结束 如果有大于8位的那么就是为空取值错误了
"""
s = re.findall('^\d{4,8}$',a)
print(s)

aa = '10000000011'
ss = re.findall('001$',aa)
print(ss)