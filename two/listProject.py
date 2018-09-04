"""

购物车 列表操作

"""
prodect_list = [

    ('iphone', 8000),
    ('mac pro', 18000),
    ('back', 7000),
    ('watch pro', 9000),
    ('coof', 32),
    ('book', 1200),


]

salary = input("请输入你的工资:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for item in prodect_list:
            print(prodect_list.index(item), item)

        break












