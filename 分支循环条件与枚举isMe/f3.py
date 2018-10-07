"""
流程控制语句 if else

if else
最经典的列子就是判断账号登录是否输入用户名和密码

python的命名规范就是下划线的形式来进行



"""
a = 1
b = 2
c = 2

if a or b + 1 == c:  # 这里也可以是表达式
    print("我们走左边")  # 这里是需要table区分的 不然if语句是不完整的 print是单独的一条语句
# print("我们不想走了")
else:
    print("我们走天上 !!!")

print("------------")

account = 'landing'
password = 'admin123'

username_input = input("请输入你的而用户名:")
password_input = input("请输入你的密码")

if username_input and password_input == account and password:
    print("恭喜用户:*%s*登录成功" % username_input)
else:
    print("用户名或密码错误请重新登录")
