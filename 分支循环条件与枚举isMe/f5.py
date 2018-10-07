""""
elif的优点

1 动态语言是没有一个具体的类型的 错误代码的关键点在于出错了没有报错
2 固有思维  if or and tuple list str dict int not and or





"""
a = input("请输入你想干的事情")
print(type(a))
a = int(a)
if a ==1:
    print('我要吃苹果')
else:
    if a==2:
        print("我要吃橘子")
    else:
        if a==3:
            print("我要吃栗子")
        else:
            print("go to shopping")

"""
1 elif 不能单独的使用 必须和if一起使用 

2 是的代码更加优美了 

"""

if a ==1:
    print('我要吃苹果')
elif a==2:
    print("我要吃橘子")
elif a==3:
    print("我要吃栗子")
else:
    print("go to shopping")










