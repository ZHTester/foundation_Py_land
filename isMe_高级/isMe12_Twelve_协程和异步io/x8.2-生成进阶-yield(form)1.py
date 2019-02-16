# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/14  16:56'
"""
原本子函数返回给了调用方g1，然后在返回给main，但是现在通过yield from man函数就直接和子函数建立了连接通道了
建立连接通道

"""
final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！！.")


def main():
    data_sets = {
        "bobby牌面膜": [1200, 1500, 3000],
        "bobby牌手机": [28, 55, 98, 108],
        "bobby牌大衣": [280, 560, 778, 70],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None)  # 预激middle协程
        for value in data_set:
            m.send(value)  # 给协程传递每一组的值
        m.send(None)
    print("final_result:", final_result)


if __name__ == '__main__':
    main()

# def sales_sum(pro_name):
#     total = 0
#     nums = []
#     while True:
#         x = yield
#         print(pro_name+"销量: ", x)
#         if not x:
#             break
#         total += x
#         nums.append(x)
#     return total, nums
#
#
# if __name__ == "__main__":
#     my_gen = sales_sum("bobby牌手机")
#     my_gen.send(None)
#     my_gen.send(1200)
#     my_gen.send(1500)
#     my_gen.send(3000)
#     try:
#         my_gen.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(result)
