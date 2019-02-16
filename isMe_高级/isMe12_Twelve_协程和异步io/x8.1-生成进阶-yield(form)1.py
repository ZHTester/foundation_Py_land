# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/13  17:26'
"""
******yield from中含有三个概念 ~
1 在函数中嵌套生成器 - 生成器也是一个
2 
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


def g1(gen):  # 调用方
    yield from gen   # 子函数


def main():
    g = g1()
    g.send(None)

# 1 main也就是调用方 g1(委托生成器)委托生成器  g1(gen) gen是委托生成器
# 1 yield from 会在调用方与子生成器之间建立一个通道(双向通道)
# 原本子函数返回给了调用方g1，然后在返回给main，但是现在通过yield from man函数就直接和子函数建立了连接通道了
#

