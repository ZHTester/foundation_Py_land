"""
dict 常用的方法
a.clear()  清空dict中的所有数据
a.copy()浅拷贝  也就是原始数据都会改变
fromkeys 静态方法 转换成dict对象
setdefault ----
update -----


"""
a = {
    "landing": {"commpany": "beij"},
    "landing2": {"commpany": "chongqing2"},
}

# ----浅拷贝---- 原始数据会正确的拷贝过来，但是了
# new_dict = a.copy()
# new_dict['landing']['commpany'] = 'chongqing3'

# ---深拷贝---- 也就是原始数据不会受到影响 但是我们需要引入python的自带包 copy
# import copy
# new_dict = copy.deepcopy(a)  # 深度拷贝
# new_dict['landing']['commpany'] = 'chongqing3'
# print(new_dict)

# ----清除字典里面的所有数据----
# a.clear()
# print(a)

# ----fromkeys 方法的使用 也就是给先用的list中的数据转换成dict且增加value  还有一种说法就是将可迭代的对象转换成dict
print('********************')
new_list = ['landing1', 'landing2']
new_dict = dict.fromkeys(new_list, {"name": "maomao"})
print(new_dict)  # {'landing1': {'name': 'maomao'}, 'landing2': {'name': 'maomao'}}
print('********************')
# ---get方法 如果没有对应的key 那么我们就默认值，如果没有取到这样的值，那么就返回我们的默认值

get_demo = new_dict.get('landing6', '没有')
print("123", get_demo)

# ---setdefault 也就是将没有的值添加到我们的dict中
set_dict = new_dict.setdefault("mtiang", "成都大学")
print("344", new_dict)  # 这样就是把没有的数据添加到我们dict中去了
print("443", set_dict)

# ---update 也就是将两个dict合并  这里面写入tuple也是可以的  ~ 或者说是可迭代对象
new_dict.update({"dingtai": "测试"})
print("889", new_dict)

# 元组拆包的方法
for key, value in new_dict.items():
    print(key, value)
