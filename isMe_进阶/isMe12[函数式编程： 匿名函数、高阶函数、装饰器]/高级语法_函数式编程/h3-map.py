"""
map(class类)的时候 函数式编程
1 map类适用于的场景 -

map 也就是会全部去取值list中的值，然后每次执行square函数
map 就是映射
map 也就是相当于执行了一次for循环 - 这点要注意划分
"""

list_x = [1, 2, 3, 4, 5, 6, 7]


def square(x):
    return x * x * x


r = map(square, list_x)

print(list(r))

