"""
如果需要通过类形式实现带参数的装饰器，那么会比前面的例子稍微复杂一点。那么在构造函数里接受的就不是一个函数，
而是传入的参数。通过类把这些参数保存起来。然后在重载__call__方法是就需要接受一个函数并返回一个函数。

"""


class logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)

        return wrapper  # 返回函数


@logging(level='INFO')
def say(something):
    print("say {}!".format(something))


say('【说】构造器')
