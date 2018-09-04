"""

装饰器 演示

"""

import time


def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))
        return warpper


# 添加装饰器 timer()


@timmer
def test1():
    time.sleep(3)
    print('in the test1')

# 对象不可调用


test1()





