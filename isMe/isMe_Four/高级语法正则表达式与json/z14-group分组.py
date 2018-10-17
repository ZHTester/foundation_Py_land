"""
1 group 分组

1 group 函数的实质是可以传入一个参数的
2 group本质的意义就是来获取分组匹配的
3 group(0) 默认就是完整的匹配
4 分组是可以含有多个分组的

"""
import re
s = 'life is shot i use python i love python'

# r = re.search('(life)(.*)(python)', s)  # 分组匹配

r = re.findall('life(.*)python(.*)', s)  # 分组匹配 这就出现了2个分组
r1 = re.search('life(.*)python(.*)python', s)  # 分组匹配 这就出现了2个分组

print(r)  # 默认的参数就是第0组
print('~~~~~~~~~~~~~~~~~~~~~~~~~')
print(r1.group(0,1,2)) # 返回的是元组形式
print('~~~~~~~~~~~~~~~~~~~~~~~~~')
print(r1.group(0))
print(r1.group(1))
print(r1.group(2))
print('~~~~~~~~~~~~~~~~~~~~~~~~~')
print(r1.groups())




