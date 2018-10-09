"""
关键字可变参数
任意个数的关键字参数 

"""

"""
可变参数的一个运用场景 .....
"""
def squsumm(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)


"""
在没有解码的过程中那么就会报错 * 
    sum += i * i
TypeError: can't multiply sequence by non-int of type 'list'
"""
squsumm(*[1, 2])
