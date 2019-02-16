# coding=utf-8
__author__ = 'landing'
__data__ = '2019/2/11  9:44'
"""
··· 单线程的方式编写异步的代码
· 协程就是单线程去调度的，不用像操作系统那样的去调度 
· 线程和进程都是内核级别的调度
· 协程是我们喊出级别的一个程序，是程序员自己调度的
· 生成器是可以暂停的函数实际上生成器是有状态的
· 
"""
import inspect


# 生成器 既是生产者也是消费者
# def gen_func():
#     value = yield from
#     # 第一返回给调用方，第二通过send方式返回给gen
#     return "landing"

# 用同步的方式编写异步的代码,在适当的时候暂停函数，在适当的时候启动函数
def download_url(url):

def download_html():
    html = yield from

if __name__ == "__main__":
    gen = gen_func()
    # 这样也就是为了实现了协程提供了基础的保证
    # 获取生成器的状态
    print(inspect.getgeneratorstate(gen))  # GEN_CREATED
    next(gen)
    print(inspect.getgeneratorstate(gen))  # GEN_SUSPENDED
    try:
        next(gen)  # 这里的这个状态就变成了close
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))  #
