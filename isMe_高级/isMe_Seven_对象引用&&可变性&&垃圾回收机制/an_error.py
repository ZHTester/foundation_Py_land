# coding=utf-8
"""
一个错误，来说明python中变量引用中的问题 ~
1 我们传递得值，尽量不要是一个list的值，这样的值是会被修改的


"""


def ins(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staff=[]):
        self.name = name
        self.staff = staff

    def add(self,staff_name):
        self.staff.append(staff_name)

    def remove(self,staff_name):
        self.staff.remove(staff_name)


if __name__ == "__main__":
    company = Company('huaxia', ['landing1','landing2'])
    company.add('landing3')
    company.remove('landing3')
    print(company.staff)
    print("----------------------------------")

    """
    * company2 与 company3 都没有传递list进来(而list又是一个可变的对象，所以说
      company2与company3 都是共用了一个list 共用了默认的list  -------> staff=[])
    
    """
    company2 = Company("huaxia1")
    company2.add("landing4")
    print(company2.staff)
    print(Company.__init__.__defaults__)  # 这里面是含有一个默认的值的 也就是没传递值的时候都会指向这样的一个值

    print("----------------------------------")

    company3 = Company("huaxia2")
    company3.add("landing5")
    print(company2.staff)
    print(company3.staff)
    print(company2.staff is company3.staff)  # 这也就是说明company2.staff对象 是 company3.staff的一个子集

    # a = 1
    # b = 2
    # c = ins(a, b)
    """
    这里的打印 ......................................
    3
    1 2
    """
    # print(c)
    # print(a, b)

    """
    [1, 2, 3, 4]
    [1, 2, 3, 4] [3, 4]  ........................
    """
    # a = 1
    # b = 2
    # a = [1, 2]
    # b = [3, 4]
    # c = ins(a, b)
    # print(c)
    # print(a, b)

    """
    (1, 2, 3, 4)
    (1, 2) (3, 4)

    """
    # a = [1, 2]
    # b = [3, 4]
    # a = (1, 2)
    # b = (3, 4)
    # c = ins(a, b)
    # print(c)
    # print(a, b)



