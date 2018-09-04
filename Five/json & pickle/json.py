"""

json 主要的目的是将数据序列化
把你吧python 的数据类型转换成字符串类型
用于不同语言的数据交换
Json模块提供了四个功能：dumps、dump、loads、load

无论对方是用什么语言写的程序 只需要开一个接口 返回json数据格式即可

"""
import json

# 将json.dumps 将数据通过特殊的形式转换成所有程序语言都认识的字符串

data = {'k1': 123, 'k2': 'hello'}
j_str = json.dumps(data)
















