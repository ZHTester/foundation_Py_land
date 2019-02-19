"""
任意个数的关键字参数

关键字可变参数列表 ~


"""


def city_tem(**param):
    print(param)
    for key,value in param.items(): # 可变参数的遍历
        print(key,":",value)



a = {"bj":"33","gg":"44"}
# city_tem(bj="33", hh='44', jj="55")  # 这样就会转换成一个字典形式的数据类型
city_tem(**a) # 简化函数的调用
city_tem()  # 什么都不传入的结果就是for循环是进不去的  得到就是一个空的字典
