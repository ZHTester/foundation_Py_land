"""
生成器
 1 任何包含yied语句的函数都可以称之为生成器，除了与名字不同之外，他的行为和普通的函数也有很大的区别
 这就在于他不是像return那样的返回值，而是每次都产生多个值，每次产生一个值(使用yield语句)，函数就会被冻结
 也就是函数在那点等待被重新唤醒，函数被重新换新后就停止的那点开始执行



 
"""

# nested = [[1, 2], [3, 4], [5, 6]]
# print(nested)


def flatten(nested):
    for sublibt in nested:
        for element in sublibt:
            yield element


nested = [[1, 2], [3, 4], [5, 6]]
# print(nested)
for num in flatten(nested):
    print(num)

# 以 list展示
a = list(flatten(nested))
print(a)


