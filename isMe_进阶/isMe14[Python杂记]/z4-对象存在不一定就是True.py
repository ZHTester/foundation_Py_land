# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/13  10:45'
"""
对象存在不一定是true .......

if None
if a
这样的对象判断一般都是和布尔值类型相对等的 .......  True  False ...... 但是我们一般对内置的数据类型是相关联的 

自定义的对象，我们如何去判断他的 True 与 False了
print(bool(test)) 这样的形式也就是说明，对象存在也有可能将对象变为false

"""


class Test:
    # pass  # 这样打印出来的数据就是True 通过bool来判断
    # def __len__(self):  # 这样打印出来的数据就是False 通过bool来判断
    #     return 0

    def __bool__(self):
        return False


test = Test()

print(bool(None))
print(bool([]))
print(bool(test))

if test:
    print("test is not None")
else:
    print("test is  None")
