"""
lambda表达式与map

x 和 y的数量不相等那么那么他只是取值最小的值 取决于较小的数量的值

"""

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 4, 9, 16]


r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))





