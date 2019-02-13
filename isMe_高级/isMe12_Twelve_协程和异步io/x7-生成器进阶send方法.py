# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/11  9:42'
"""
生成器 (就可以实现暂停-yield)
1 html = yield "https://www.baidu.com" 这是一个异步的方法来进行，这样的情况就实现了一个函数的暂停切换的功能了。
2 html也已传递给另外一个调用函数，另外一个函数调用完成以后，在传递完成后给原有的函数(传回调用方)。
3 html = yield "https://www.baidu.com" yield写在生成器的右边的时候，在外部拿到我们所有生成器的函数
4 send方法 throw方法 close方法

"""


def gen_func():
    # 可以产出值,可以接收值(调用方传递进来的值) html = yield "https://www.baidu.com"
    html = yield "https://www.baidu.com"  # 这里的值就变成了landing 因为这里使用了send
    print(html)
    yield 2
    yield 3
    return "landing"
# 1 生成器不仅仅可以产出值 还可以接受值 ....


if __name__ == "__main__":
    # 也就是说我们能拿到这个生成器对象，我们就能对这个函数进行暂停与恢复
    gen = gen_func()  # 这里就是生成了一个生成器对象
    """
    直接调用send,这里就会报错
    TypeError: can't send non-None value to a just-started generator
    我们在生成器对象生成的时候，第一次调用生成器，我们只能send一个None的值，
    不能send一个非None的值，因为在生成器第一次生成的时候，我们还没有运行生
    成器，那么这个时候我们传入一个非None的值，那么就会报错啦
    """
    # 我们在使用send发送非None值的时候，我们必须启动一次生成器，方式有2种1.gen.send(None)
    url = gen.send(None)
    # 启动生成器方式有2种 next send
    # send将值发送到生成器对象内部 同时启动我们的生成器
    # url = next(gen)
    # download url
    html = "landing"  # 将这个html传入到生成器的内部
    # send方法可以传递值进入生成器内部,同时还可以重启生成器，执行到下一个yield的位置 将这个html传入到这个生成器内部中 next(gen)
    # 有了send方法我们生成器变成协程才有基础
    print(gen.send(html))  # 这里的方法和next是一样的,那么在这里就会yield出yield2出来
















































