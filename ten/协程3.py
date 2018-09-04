"""
自动切换协程  自动档的切换
自动切换IO


"""

import gevent


def func1():
    print('runing func1 .......')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('runing func2 .......')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


def func3():
    print('runing func3 .......')
    gevent.sleep(0)
    print('fun3 again')


gevent.joinall([gevent.spawn(func1),
                gevent.spawn(func2),  # gevent.spawn(func3),
                gevent.spawn(func3), ])
