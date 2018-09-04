"""
创建对象
 传统的创建方式但是在使用名称的时候是不容易创建的，这个时候我们就需要变相成为字典方便调用
"""
# # role 1
# name = 'Alex'
# role = 'terrorist'
# weapon = 'AK47'
# life_value = 100
# money = 10000
#
# # rolw 2
# name2 = 'Jack'
# role2 = 'police'
# weapon2 = 'B22'
# life_value2 = 100
# money2 = 10000
#
# # role 3
# name3 = 'Rain'
# role3 = 'terrorist'
# weapon3 = 'C33'
# life_value3 = 100
# money3 = 10000
#
# # rolw 4
# name4 = 'Eric'
# role4 = 'police'
# weapon4 = 'B51'
# life_value4 = 100
# money4 = 10000
"""
修改成自字典的形式 键值对的形式方便调用

"""
# roles = {
#     1: {'name': 'Alex',
#         'role': 'terrorist',
#         'weapon': 'AK47',
#         'life_value': 100,
#         'money': 15000,
#         },
#     2: {'name': 'Jack',
#         'role': 'police',
#         'weapon': 'B22',
#         'life_value': 100,
#         'money': 15000,
#         },
#     3: {'name': 'Rain',
#         'role': 'terrorist',
#         'weapon': 'C33',
#         'life_value': 100,
#         'money': 15000,
#         },
#     4: {'name': 'Eirc',
#         'role': 'police',
#         'weapon': 'B51',
#         'life_value': 100,
#         'money': 15000,
#         },
# }
#
# print(roles[1])  # Alex
# print(roles[2])  # Jack
#
#
# def shot(by_who):
#     # 开枪后减去十滴血
#     pass
#
#
# def got_shot(who):
#     # 中枪减去10滴血
#     who['life_value'] -= 10
#     pass
#
#
# def buy_gun(who, gun_name):
#     # 检查钱够不够,买了枪后要扣钱
#     pass


"""
构造函数 直接生成相关数据

"""

'''
1 把一个类变成一个具体的对象的过程叫做实例化
2 在类共有的东西构造方法 和构造函数都是公用的
3 想要在类中的构造函数调用那么在构造函数中都必须含有self 就是代表当前对象知道是谁调的。 
4 先找实例本身的变量，如果实例本身没有变量那么就去类里面去找变量
5 修改类变量不是修改类变量而是创建了新的变量


'''


class Role:
    # 类变量 储存在类的内存中
    n = 123
    name = '我是类name'

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        # 构造函数
        # 在实例化时做一些实例的初始工作
        # self代表的是类实例化的对象

        self.name = name   # r1.name = name 实例变量（静态属性） 作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money


    def shot(self):  # 类的方法 功能 (动态属性)
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...", self.name)

    def buy_gun(self, gun_name):
        print("just bought %s" % self.name, gun_name)


r1 = Role('Alex', 'police', 'AK47')  # 实例化(可以称为初始话一个类 相当于创建了一个对象)
r1.name = 'MacHao'
r1.bullet_prove = True
r1.n = '改类变量'
print(r1.n, r1.name, r1.bullet_prove)


r2 = Role('Jack', 'terrorist', 'B22')   # 生成一个角色 role这个类的实例
r2.name = '张浩'
print(r2.name, r2.n)
#
# r1.got_shot()   # Role.got_shot(r2) 调用的方法的具体步骤
# r1.buy_gun('ak51')

# 修改类变量
Role.n = "abc"
print(Role.n)

