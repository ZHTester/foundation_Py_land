"""
导入模块功能  引用其余模块中的变量与函数


def logger():
    print('in the mode_a logger')


def running():
    print('in the mode_a running')

    import module_a = all_code

"""

from Five.module import module_a


# from ..module_a import logger as logger_aaa

print(module_a.x)

print(module_a.say_hello())

module_a.logger()

def logger():
    print('in the mode_a logger main')


logger()
