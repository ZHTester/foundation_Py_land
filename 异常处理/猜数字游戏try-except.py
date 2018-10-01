"""
1 猜数字游戏

需求: 猜数字游戏
     1 开始游戏产生一个1-100的随机数
     2 用户输入，游戏工具输入值提示大或者小
     3 用户根据提示继续输入，直到猜中为止
     4 如果用户输入错误，程序可以处理异常



"""
import random
num = random.randint(0, 100)
print(num)

while True:
    try:
        guess = int(input("请输入 1-100"))
    except ValueError as e:
        print('请输入 1-100 的值')
        continue
    if guess >num:
        print("guess Bigger:",guess)
    elif guess < num:
        print("guess Smaller:",guess)
    else:
        print("guess Ok, Game Over")
        break
    print("\n")

