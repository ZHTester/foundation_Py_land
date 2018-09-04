"""
优化导入模块代码

"""

# import module_b
from .module_b import test


def logger():
    # module_b.test()
    test()
    print('in the logger')


def search():
    # module_b.test()
    test()
    print('in the sear')
