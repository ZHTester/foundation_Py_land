# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/27  13:38'

"""
生成器函数的使用 ---> 这个也就是关系到协程 ---这个知识点十分重要 --- gen_func 生成器函数
1 什么是生成器函数 - 函数里面只要有yield关键字，那么他就是一个生成器函数，那么他就不再是普通函数啦。 
2 生成器函数也叫生成器对象 gen = gen_func()  这里的gen其实也就是对象了，也就是生成器返回的生成器对象了。
2 调用生成器函数实际上返回的是生成器对象 也就是在python编译的时候就残生字节码了
3 生成器对象也是实现了我们迭代器协议的。
4 函数中只返回一个值，return 1之后，就不能在return 2了 ~ 因为return后已经就代表该函数的结束
5 生成器中的yield可以不断的返回，因为yield是生成器，所以可以不断的返回值.
6 生成器对象也是实现了迭代器协议的

生成器的概述: 
知道迭代器之后，就可以正式进入生成器的话题了。普通函数用 return 返回一个值，和 Java 等其他语言是一样的，
然而在 Python 中还有一种函数，用关键字 yield 来返回值，这种函数叫生成器函数，函数被调用时会返回一个生
成器对象，生成器本质上还是一个迭代器，也是用在迭代操作中，因此它有和迭代器一样的特性，唯一的区别在于实
现方式上不一样，后者更加简洁
 
"""


def gen_func():
    yield 1
    yield 2


# 斐波拉契经典的算法就是实现了生成器中的魔法函数
# 惰性求值，延迟求值, 这里实现的方式就是递归的方式进行的

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


print(fib(10))


# 这样的编写方式就是性能上会出现很大的问题 因为会首先分配到内存中
# 但是我们使用了yield 这样的惰性求值，就不会消耗内存的。
def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


print(fib2(10))


def gen_fib2(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


for gen_value in gen_fib2(10):
    print(gen_value)


def common_fun():
    return 1


if __name__ == "__main__":
    # 返回的就是生成器对象 gen - 这个生成器对象就是在python编译字节码的时候就产生了这样的一个生成器对象
    # 生成器对象也是实现了我们迭代器协议的,所以取出生成器中的值也是可以通过for循环来实现的
    gen = gen_func()
    for value in gen:
        print(value)
    # 这里就是普通函数调用的时候 生成的返回结果。
    result = common_fun()
    pass
