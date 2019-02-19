"""
reduce 也就是在做一个连续的计算，也就是说reduce会连续调用我们的lambda表达式

第一次执行的时候reduce 中x取值1 y取值为2 一次连续运算  当x遍历完成后 reduce函数就调用完成了
1+2=3
3+3=6  以上就是求和的reduce的方法
其中10 就是初始值的相加
"""
from functools import reduce

list_x = [1, 2,3]
# list_y = [1, 4, 9, 16]

r = reduce(lambda x, y: x + y, list_x,10)
print(r)
