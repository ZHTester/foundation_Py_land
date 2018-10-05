"""
如何判断变量的值，身份与类型
1 值== 身份is 类型isinstance - 这就是对象的三个特征 python一切皆对象
2 类型不推荐使用 关系运算符的意思就是说，is OR == 是不能判断类型的子类，但是isinstance是可以的

"""
a = 1
print(type(a) is str)
print(isinstance(a,str))

"""
判断这三种类型是否存在于a当中

"""
print(isinstance(a,(int,float)))