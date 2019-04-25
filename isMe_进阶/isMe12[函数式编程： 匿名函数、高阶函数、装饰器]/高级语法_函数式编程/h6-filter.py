"""
filter 可以帮我们过滤点我们不需要的元素
       也可以说帮我们过滤掉一些不符合我们定义规则的元素

filter 表达式中的lambda表达式中 要求必须是True或者是Flase 因为filter本身就是需要判断是否为真
filter 只要判断有真假就可以 如果返回是false那么就会被剔除的

"""
list_x = [1, 0, 1, 0, 1, 0, 1]
r = filter(lambda x: True if x == 1 else False, list_x)
print(list(r))




