"""
三元表达式 其实就是一个表达式版本的if else

1 三元表达式在lambad中使用的是比较多的
x>y ? x:y 在其他语言中是这样表达三元表达式
---三元表达式十分易于编写一个lambda表达式的---

2 python版本的三元表达式:

条件为真时返回的结果 if 条件判断  else 条件为假时的返回结果

"""
x = 1
y = 8
r = x if x < y else y
print(r)








