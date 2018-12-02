#
"""
切片对象

list切片操作以后还是 list
现在我们就想实现切片以后还是list 我们应该怎么做了 ？

class Group:  <------> 实现了序列协议的全部的魔法方法，那么这个类就是序列协议类
Sequence 序列协议所需要需要实现的魔法函数
__reversed__
__contanins__
__len__
__itter__

"""
import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    """
    实现序列化中的抽象方法 不变的序列化对象 Sequence
    
    """

    def __reversed__(self):
        """
        反转的工作直接交给了list来做了
        :return:
        """
        self.staffs.reverse()

    def __getitem__(self, item):
        """
        切片的操作交个list来进行操作
        item 初始化一个切片对象也就是slice 交给我们的getitem来使用
        list为什么能这么用，因为list也实现了这样的一个方法，我们自定义一个序列类型，
        我们就需要实现这一的一个方法，
        :param item:
        :return:
        """
        # return self.staffs[item]  # iteam 这里返回的实际上就是一个切片的对象值
        cls = type(self)  # 获取到当前对象 返回group类型  这个对象就是-slice

        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in staffss:
            return True
        else:
            return False

    def __getattr__(self, item):
        return "你的数据类型没找到"

    # def __str__(self):
    #     return self.company_name


staffss = ['landing1', 'landing2', 'landing3', 'landing4']
group = Group(company_name="北京网", group_name="users", staffs=staffss)
reversed(group)
submit = group[:2]  # 切片后还是group 而不是list 这样的group就是一个切片对象 这里其实还是一个group对象

# 这里也就调用了魔法函数
# group[0]  # 这个时候的对象就是一个int类型对象了  这个时候就实现了一个切片类型了
print(len(group))

# 这里也就调用了魔法函数
print(submit)

# 打印类型的迭代生成器
print(group.staffs[2])

# 这里也就调用了魔法函数
if "landing2" in staffss:
    print("yes")
else:
    print("false")
