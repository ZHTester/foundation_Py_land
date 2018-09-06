"""
字典操作

"""
info = {

    "a": "beij",
    "b": "riben",
    "c": "hanguo",
    "d": "niriniya",
        }

print(info)

print(info["a"])  # 取值

info["b"] = "韩国"  # 存在就是修改数据
info["f"] = "越南"  # 不存在就是增加数据
print(info)

"""删除数据"""

# del info # 删除整个字典
# del info["a"]
# info.pop("a")  # 指定删除相关数据
# info.popitem()  # 随机删除数据

"""查找某个值"""
# print(info["b"])  # 查找某个值
print(info.get("f"))
print("a" in info)  # 判断一个值是否存在于字典中

