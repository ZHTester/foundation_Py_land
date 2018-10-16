"""
search 与match 函数

1 match 是要从字符串的的开始进行匹配 如果没找到相应的结果那么就返回为空None

2 s = 'A3355599988842DH'

3 seacher 将搜索整个字符串 并不是从头开始的 一旦找到结果就会返回结果

4 findall 与 seacher match 就是搜索到了数据就立马返回，不会再去继续搜索了


"""
import re
s = '3355599988842DH'

r = re.match('\d', s)
"""
span 将返回我们匹配的字符串在 元字符中的位置
"""
# print(r.span())   # 这里返回的是空因为match是要从开始进行匹配的 match也是返回的一个对象


r1 = re.search('\d',s)
print(r1.group(), "*****************")  # 返回的是数组列表 search返回的是一个对象

r2 = re.findall('\d',s)
print(r2, "*****************")













