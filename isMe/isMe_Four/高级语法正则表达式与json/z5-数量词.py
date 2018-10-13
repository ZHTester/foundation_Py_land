"""
1 数量词
2 [a-z]{3,6} 数量词的分割也就是使用非字符来表达的
3 


"""
import re
a = 'python1\t11\n1&javaphp___99php77'

r = re.findall('[a-z]{3,6}', a)  # \d 代表数字的概括字符集

print(r)
