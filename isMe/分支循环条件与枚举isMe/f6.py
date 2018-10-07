"""
循环语句 一般就是 while循环和 for循环

while 语句十分容易造成死循环

递归循环是十分喜欢使用while语句的 ，但是一般解决循环语句的时候，我们都是使用的是for循环


"""

# CONTENT = True
#
# while CONTENT:  # 如果while表达式依然我True 那么将实现无限死循环
#     print("循环")  # 容易造成死循环

content = 1
while content <= 100:
    content += 1
    print(content)
else:
    print("我们结束了 ......")

