"""
for循环语句
1 主要用来遍历循环 序列或者集合 字典 凡是有序列概念的情况下，我们都是可以采用for循环来操作的
2 代码块还适合加上代码块的嵌套代码块来使用



"""

"""
内层循环与外程循环的一个概念，跳出了当前的循环，那么下一个数组的循环还是将继续


"""
a = [['西瓜', '蛋糕', '梨子', '葡萄'], (1, 2, 3, 4, 5)]
for aa in a:  # aa 代表当前循环列表里面取出的值
    for y in aa:
        if y == '蛋糕':
            break
        print(y)
else:
    print("执行完成.....")

"""
当x = 2的时候就不打印了
break
"""
aa = [1, 2, 3, 4]
for x in aa:
    if x == 2:
        break
    print("%s-----------" % x)

"""
当x = 3 不打印2 
continue 继续执行

如果不是正常执行完成的语句，那么 else中的语句是不会执行的 break
但是你使用的continue 那么是会正常执行else中的语句的
"""
bb = [1, 2, 3, 4]
for x in bb:
    if x == 2:
        break
    print(x)
else:
    print("你说我执行完成了啊？")
