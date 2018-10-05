"""
逻辑运算符
1 逻辑运算符主要是操作的基本类型是布尔类型的,他的返回类型也是布尔类型的
2 and(且) 也就是返回的基本数据类型都是true那么返回的结果也是true
3 or(或) 一真 这返回真 如果两个都是false那么就返回false
4 not(非)
5 字符串 数字和布尔类型是有一个转换的关系的
6 我们很多时候是对非布尔类型的数据做逻辑原酸的
7  and 和 or的返回规律



"""

"""
and

"""
print(1 and 1)
print('a' and 'b')
print('a' or 'c')
print(not 'a')

"""
1 int float  0被认为是false 非0这认为是true 0.1也就是true
2 字符串 空字符串被认为是false 非空则认为是true
3 空列表 tuple set dict 我们将认为是false  非空则认为是true
4 
"""
print(not 0.1)
print(not '0')

print(not [])
print(not [1,23])

print([1] or [])  # 非布尔类型有一定的转换关系转换成bool 但是了反过来也是这样的概念



"""
and 返回的顺序
一假必假  
2真必真 
计算的返回数据的方式就是哪个方便返回哪个数据

"""
print(0 and 1)
print(1 and 0)
print(2 and 1)  # 返回的是1
print(2 and 3)  # 返回的数据类型是3

"""
and 返回的顺序 
一真必真 
一假必假 


"""
print("-------------")
print(0 or 1)
print(1 or 0)
print(2 or 1)  # 返回的是2  计算都是可以偷懒的 那么读取了第一个数据那么就返回第一个数据
print(2 or 3)  # 返回的数据类型是2






























