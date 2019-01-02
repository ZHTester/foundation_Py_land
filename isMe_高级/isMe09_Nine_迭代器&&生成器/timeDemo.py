# coding=utf-8
__author__ = 'landing'
__data__ = '2018/12/30  10:04'
# 引入datetime模块
import datetime

# 计算今天的时间
today = datetime.date.today()
# 计算昨天的时间
yesterday = today - datetime.timedelta(days=1)
# 计算明天的时间
tomorrow = today + datetime.timedelta(days=1)
# 打印这三个时间
print(yesterday, today, tomorrow)
