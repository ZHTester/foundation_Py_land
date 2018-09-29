"""
1 装饰器
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，
有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。

2 概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能。
"""

# def debug():
#     import inspect
#     caller_name = inspect.stack()[1][3]  # 获取当前运行的类名
#     print("[DEBUG]: enter {}()".format(caller_name))
#
#
# def say_hello():
#     debug()
#     print("hello!")
#
#
# def say_goodbye():
#     debug()
#     print("goodbye!")
"""
1 实际的装饰器 

"""

# def debg(func):
#     def wrapper():
#         # import inspect
#         # caller_name = inspect.stack()[1][3]  # 获取当前运行的类名
#         print("[DEBUG]: enter {}()".format(func.__name__))  # format(func.__name__) 获取类名称
#         return func()
#
#     return wrapper()
#
#
# def say_hello():
#     print("hello!")
#
#
# say_hello = debg(say_hello)  # 添加功能并保持原函数名不变

"""
1 初级中的高级装饰器 

这是最简单的装饰器，但是有一个问题，如果被装饰的函数需要传入参数，那么这个装饰器就坏了。
因为返回的函数并不能接受参数，你可以指定装饰器函数wrapper接受和原函数一样的参数，比如：

"""


def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...', )
        return func(*args, **kwargs)  # 能传入一个或者多个值  返回外接函数的相关执行结果值

    return wrapper  # 返回


@debug
def say(something):
    print('hello {}!'.format(something))


print(say('beijing'))
