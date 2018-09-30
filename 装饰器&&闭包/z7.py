"""
1 装饰器用来装饰函数
2 返回一个函数对象
3 被装饰函数标识符指向返回的函数好对象
4 语法 @deco

5 装饰器其实就是对闭包的一个使用


"""


def dec(func):
    print('cell dec')

    def in_dec(*arg):
        print('in dec arg=', arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    print ('return in_dec')
    return in_dec


@dec  # 其实执行的就是 in_dec  被装饰的函数指向装饰的函数 这就是装饰器的实质
def my_sum(*arg):
    print('in my_sum')
    return sum(arg)
# my_sum(1,2,3,4,5,6)

def my_average(*arg):
    return sum(arg) / len(arg)

# my_sum = dec(my_sum())
