# encoding: utf-8

"""
# @Time    : 20/4/2020 5:49 上午
# @Author  : Function
# @FileName    : jindutiao.py
# @Software: PyCharm
....................... 进度条 .......................

# \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；
{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，
对应输出的数为c；{}，
对应输出的数为a；{}，
对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；
end=''，用来保证不换行，不加这句默认换行。
"""
import time

scale = 99
print("执行开始".center(scale, "-"))  # 居中对齐
start = time.perf_counter()  # 获取起始时间
for i in range(scale + 1):
    a = i * '*'
    b = (scale - i) * '.'
    c = (i / scale) * 100
    dur = time.perf_counter()  # 每次获取当前时间 time.perf_counter() 性能计数器以秒为单位计算出当前的秒的浮点数类型
    d = "\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')  # 输出百分比，图形进度以及当前所用的时间,控制end为空使得不用换行
    time.sleep(1)
print('\n' + "结束执行".center(scale, '-'))
