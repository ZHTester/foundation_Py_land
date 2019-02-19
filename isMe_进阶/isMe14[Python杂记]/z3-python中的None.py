"""
Python 中的None
1 Python中的空就是空 他不代表空的字符串 也不代表空的序列 0 False，
  也就是从值上面来讲或者是从类型上来讲，这2者都是不相等的
2 None本身也是有数据类型(其实也是有数据类型的)的NoneType <class 'NoneType'>


"""
print(type(None))
a = []

# 这就是进行一个判空操作 但是尽量不要使用 a is none (因为None本身就是一个对象 而is就是做对象比较的)
# 这就是判空的操作

if a:
    print("这是一个空......")
else:
    print("这不是一个空....")

if not a:
    print("这是一个空......")
else:
    print("这不是一个空....")


# None 与 False本质上的区别  ----> [] 空序列 -----> '' 空字符串
# None是不存在的概念  而False本质上是真假的判断
# 这两个本质上得到的结果是一样的但是本质上是不一样的


if None:
    pass
else:
    pass

if False:
    pass
else:
    pass



















