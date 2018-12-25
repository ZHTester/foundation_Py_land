"""
1 列表推导式  也叫列表生成式 - 通过一行代码生成列表
2 生成器表达式
3 字典推导式
4 列表生成式的性能是要高于列表本身的
"""
# 列表推导式 或者说列表推导式
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)
print("*****************************")


def handle(item):
    return item * item


odd_listDemo = [handle(i) for i in range(21) if i % 2 == 1]
print(odd_listDemo)
print("*******************************")


# 生成器表达式  生成器表达式是可以转换成list的  生成器也是可迭代的对象
odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_gen))
print(odd_gen)
odd_listG = list(odd_gen)
print(odd_list)
print("********************************")

# 字典推导式
my_dict = {"landig": 22, "dingding": 33}
resversi_dict = {value: key for key, value in my_dict.items()}
print(resversi_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)




