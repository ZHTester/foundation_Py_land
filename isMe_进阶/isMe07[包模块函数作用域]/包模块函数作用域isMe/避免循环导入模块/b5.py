"""
__name__ 的经典使用
1 既可以作为一个模块提供给他人调用，也可以使自己作为一个可执行的文件
2 if __name__ == '__main__'  作为入口文件就是这样编写
3 如果只是作为一个可执行的文件，那么其实 if __name__ == '__main__' 这个是可以不用编写的
4 可执行文件当做模块使用 就可以用__name__ == '__main__'
5 python -m seven.m5 当做是一个模块来执行  -m 那我们就需要使用文件路径的方式来使用 还有一个是文件路径的问题
6 相对导入 绝对导入 相对路径和绝对路径的问题


"""

if __name__ == '__mian__':
    print("执行方法")

