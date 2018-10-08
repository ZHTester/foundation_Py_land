"""
python中如何返回多个值

"""


def image(skill1, skill2):
    de1 = skill1 * 10
    de2 = skill2 * 20 + 10
    return de1, de2  # 这样的形式就可以返回2个值了


result = image(3,6)
# 这样的接收方式叫做序列解包  - 最好是使用有意义的变量名称来接收变量的结果
result_1, result_2 = image(6,9)  # 我们使用两个变量的形式来接收这样的一个结果
print(result_1)
print(result_2)
print(type(result))  # 返回的结果是一个元组类型的 返回元组类型的集合
print(result)  # 当用return接收到了这样的一个参数的时候如何使用这样的一个结果了？
print(result[0],result[1])  # 这样的取元组的返回变量结果是十分不好的

