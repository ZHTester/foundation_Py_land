"""
高级装饰器



"""

"""
1  带有参数的装饰器
"""


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=level, func=func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@logging(level='INFO')
def say(something):
    print("say {}!".format(something))


# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print("do {}...".format(something))


if __name__ == '__main__':
    say('hello')
    print('---------------------')
    do("my work")
