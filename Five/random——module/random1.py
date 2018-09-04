# import random

# print(random.random())
# print(random.randint(1, 2))
# print(random.randrange(1, 10))
import random

print(random.choice('hello'))
print(random.choice('hello', 3))
# 随机整数
print(random.random(0, 99))
# 随机选取0到100区间的偶数
print(random.randrange(0, 101, 2))
# 随机浮点数
print(random.random())  # 不制定区间就是 0-1
print(random.uniform(1, 10))

# 随机字符
print(random.choice('sdfsdfsdfsdf'))

# 多个字符中选取特定数量的字符
print(random.sample('werwerwerw', 4))  # [f, h, d]

# 随机选取字符串
print(random.choice(['apple', 'pear', 'peach', 'orange', 'lemon']))  # apple

# 洗牌
iteams = [1, 2, 3, 4, 5, 6]
print(iteams)  # [1, 2, 3, 4, 5, 6, 7]
random.shuffle(iteams)
print(iteams)  # [1, 4, 7, 2, 5, 3, 6]


