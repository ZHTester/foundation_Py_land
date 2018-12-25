"""
魔法函数
1 魔法函数是为了增强我们类的一些特性独有的特性，而且他并不是继承了obj的，他也不属于他所存在的类下面，魔法函数其实就是独立
  的存在。当我们在类下面添加了魔法函数其实就会增强了我们类的一些类型与一些特性
2 双下划线开始和双下划线结束这样的函数就叫做魔法函数
3 python语法会做一些优化，如果就是python拿不到迭代器(也就是迭代方法的时候)，他就回去尝试看我们这个类中是否有这个迭代魔法方法
  如果有的话就回去调用这个方法,一次一次的直到我们的方法被取完.
4 魔法函数会直接影响到我们函数的本身，魔法函数也是会影响到我们python中的一些内置函数的本身的,比如说list 或者说 for循环
  等一些
5 魔法函数也不是和我们的对象存在一定的继承关系，有了这些魔法函数，也就是将我们Python一些类型给我组织起来了
  可迭代的对象，可调用对象，等等一些

"""

"""
这个对象class 也就是可迭代的对象 也就是可迭代的类型


"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    """
    这里含有了这样的一个魔法函数，就使得我们
    不需要在编写for循环，使得该类具有循环的特性
    
    这里也就是给这个类增加了可迭代的特性，也就是对象变为了可迭代的对象
    那么既然是可迭代的对象，那么我们就可以使用for循环进行遍历 
    
    """

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        for i in self.employee:
            return i


company = Company(['tom', 'bob', 'jane'])
company1 = company[:2]

# employee = company.employee
"""
company1 这个对象本身是没有实现len这个方法的，如果直接调用那么就会报错。
但是了self.employee 这个对象是实现了len这个方法的，如果说我们直接调用这样的对象是可以实现len方法的
"""
print(len(company1))  # 其实这样的话魔法函数是会影响到我们内置函数的本身的
print(company)

# for em in company:
#     print(em)





