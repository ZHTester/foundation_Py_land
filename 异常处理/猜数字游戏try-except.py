"""
1 猜数字游戏

需求: 猜数字游戏
     1 开始游戏产生一个1-100的随机数
     2 用户输入，游戏工具输入值提示大或者小
     3 用户根据提示继续输入，直到猜中为止
     4 如果用户输入错误，程序可以处理异常

"""
import random

#
# num = random.randint(0, 100)
# print(num)

# while True:
#     try:
#         guess = int(input("请输入 1-100"))
#     except ValueError as e:
#         print('请输入 1-100 的值')
#         continue
#     if guess > num:
#         print("数字大了,在猜.........:", guess)
#     elif guess < num:
#         print("数字小了，在来...............:", guess)
#     else:
#         print("你真棒，猜中了，游戏结束")
#         break
#     print("\n")


num = random.randint(1, 50)

while True:
    try:
        cai = int(input("游戏开始...(1-50)"))
    except Exception as e:
        print('请输入 1-100 的值')
        continue
    if cai > num:
        print("你猜的数字大了请重来 %s" % cai)
    elif cai < num:
        print("你猜的数字小了请重来 %s" % cai)
    else:
        print("你真的十分的棒哦 ！ 游戏结束")
        break
    print("\n")
