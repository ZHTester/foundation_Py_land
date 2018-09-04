"""
字符串操作

"""

name = 'my {name} is  im {age} is'

a = name.capitalize()  # 首字母大写
print(a)

b = name.count("i")  # 统计相关字母的大小
print(b)

print(name.center(50, '-'))  # 补全字符串的的操作

print(name.endswith("beij"))  # 以什么结尾判断真或者假  比如说判断一个邮件地址以什么结尾

print(name[name.find("name"):])  # 把找到字符的索引返回出来 name返回的3那么字符串也是可以切片的

print(name.format_map({'name': "guangzhou", 'age': 33}))

print(name.format(name="shangxin", age=33))

print("1".isidentifier())  # 判断是不是一个合法的标识符号

print("a".islower())  # 判断是不是小写

print('1'.isnumeric())  # 判断是不是数字

print(" ".isspace())  # 判断他是不是一个空格

print("My name is ".istitle())  # 判断是不是一个title

print("+".join(['1','2','4']))  #

print(name.ljust(50, "*"))  # 后面补全

print(name.rjust(50, "*"))  # 前面补全

print("FFFF".lower())  # 把小写变大写

print("beijing".upper()) # 把大写变小写

print("chengdu\n  ".lstrip())  # 从左边去掉空格并且回车

print("riben".rstrip())  # 从右边去掉空格

print("  beijingshanghai ".strip())  # 双向去掉空格

print("zhangsan".replace("a","A",1))  # 只需要替换一个值

print("beij shanghai".rfind("a"))  # 找到最右边的那个值的返回

print("shanghai".split('h'))  # 把字符串按照空格分成列表  分隔符的概念

print("1+2+3+4+5=6".split('+'))

print("Zhang Jia jie".swapcase())  # 大写变小写 小写变大写

print('lex li '.title())  # 把 字符串变为tile格式

print('hao hao hao '.zfill(50))  # 把字符长度增加成相关的长度

print("----------")




