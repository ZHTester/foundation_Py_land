# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/13  14:39'
"""
1 生成器clsoe方法 也就是关闭这个生成器
2 


"""


def gen_func():
    try:
        yield "https://www.baidu.com"
    except GeneratorExit as e:
        # raise StopIteration  # print(next(gen))就会报这一句错误了
        pass
    yield 2
    yield 3
    return "landing"


if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    # 只要生成器关闭了，那么不管我们是否try掉,我们都不会再运行下去了
    # RuntimeError: generator ignored GeneratorExit
    # 也就是会出现在调用方报错 这个close的异常都是向上抛的
    gen.close()
    print(next(gen))

    # GeneratorExit 是继承自BaseException  Exception











