# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/13  15:20'


def gen_func():
    try:
        yield "https://www.baidu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "landing"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))

