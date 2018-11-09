"""
1 需要了解图形化交互式shell ipython来进行编写 ******* 这个是重点
2 魔法函数并不是说我们继承了某些方法，我们才去可以写这些魔法函数的，魔法函数我们可以写到任意的类中
3

常用魔法函数:
魔法函数分为:    1 非数学运算
              2  数学运算

1 非数学运算
-1 字符串表示: __repr__  __str__
-2 集合，序列相关: __len__ __getitem__  __setitem__  __delitem__  __contanis__


"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    """
    这里的魔法函数就会打印出我们字符串为人类习惯的方式来调用
    这个魔法函数是对我们对象字符串格式下所需要使用的
    
    """

    def __str__(self):
        return ".".join(self.employee)

    # def __repr__(self):  #     return ".".join(self.employee)


# 数学运算符
class Num(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


company = Company(['tom', 'bob', 'jane'])
"""
print(str(company)) 这里会打印出字符串形式 ，
当然这里也会隐含的去调用str，这是Python解释器回去做的事情也就是隐含的调用str

"""
print(company)

"""
这样的时候在解释器中是不会被打印的，
因为这个的Python是默认去调用了__repr__ 这样一个魔法函数 默认我们是不会去调用打印的
如果我们重新定义了这样的一个函数，那么是能被定义打印的

这样的模式是我们在开发模式下需要使用的 __repr__
    def __repr__(self):
        return ".".join(self.employee)
    company.__repr() 这样是直接的调用方式，但是了在我们的Python中Python解释器会默认去调用这些魔法函数的。
    魔法函数在定义了就不需要我们显示的去调用，Python在运行的时候解释器就会自动的去调用这些魔法函数    
"""
print(repr(company))  # 这样的形式打印出来的就是 tom.bob.jane

# -----------------------
my_num = Num(-2)
print(abs(my_num))


