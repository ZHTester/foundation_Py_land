"""
python自带封装好了的协程库

greenlet是实现了手动切换线程 - 如果按照买车的现状就是 自动挡


执行的顺讯首先程序启动gr1 和gr2 两个线程
然后协程首先调用gr1 -执行test1 打印12-执行gr2打印56 - 切换到gr1 打印34 -在切换到gr2 打印78


"""

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)  # 启动一个协程
gr2 = greenlet(test2)
gr1.switch()  # 直接执行线程gr1


























