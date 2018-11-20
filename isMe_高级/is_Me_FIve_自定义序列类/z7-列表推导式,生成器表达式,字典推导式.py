"""
列表推导式  也叫列表生成式
生成器表达式
字典推导式

"""
# 列表推导式 或者说列表推导式
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)


def handle(item):
    return item * item


odd_listDemo = [handle(i) for i in range(21) if i % 2 == 1]
print(odd_listDemo)

# 生成器表达式  生成器表达式是可以转换成list的  生成器也是可迭代的对象
odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_gen))
print(odd_gen)
odd_listG = list(odd_gen)
print(odd_list)

# 字典推导式
my_dict = {"landig": 22, "dingding": 33}
resversi_dict = {value: key for key, value in my_dict.items()}
print(resversi_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)




