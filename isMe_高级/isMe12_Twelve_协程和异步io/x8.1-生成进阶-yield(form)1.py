# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/13  17:26'
"""

"""


def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable


'-----------------------------------------------'

for value in g1(range(10)):
    print(value)  # 这个会原封不动的打印出来

for value in g2(range(10)):
    print(value)  # 这个将循环打印出来




