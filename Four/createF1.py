"""

生成器 在调用的时候才会存在

"""
a = (i*2 for i in range(1000))


'''通过循环调用生成器'''
for i in a:
    print(i)

# print(a.__next__())



