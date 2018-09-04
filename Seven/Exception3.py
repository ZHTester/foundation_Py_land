"""

自定义异常

"""


class ZhException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise ZhException('我的异常')
except ZhException as e:
    print(e)
