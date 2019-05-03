# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/15  14:14'
"""
Log 日志文件 记录错误的时候判断文件 



"""
import logging
logger = logging.getLogger()  # 创建logging的对象
logger.setLevel(logging.DEBUG)
consle = logging.StreamHandler()  # 创建了流这个对象 然后就可以对Logging进行一个写入的操作了
logger.addHandler(consle)  # 然后将流这个对象添加进去 也就是往控制台输出的流了
logger.debug('testing')  # 传入的数据是流媒体
consle.close()
logger.removeHandler(consle)




























