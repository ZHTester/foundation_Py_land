"""
多级字典嵌套函数 2 update


"""

info = {

    "a": "beij",
    "b": "riben",
    "c": "hanguo",
    "d": "niriniya",

        }

b = {

    "a": "请你",
    "b": "日本",
    "c": "韩国",
    "d": "美国",

        }


info.update(b)
c = dict.fromkeys([6,7,8],"test")  # 初始化一个字典的值
print(c)
print(info)


# 把字典转换成元组 items()
print(info.items())







