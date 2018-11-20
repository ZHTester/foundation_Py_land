"""
说明: bisect 其实就是用来处理已排序的序列，其中list只是序列中的一种，用来维持已排序的序列，且这个序列是升序

1 bisect 其实就是使用二分查找来维持我们的可排序的序列 插入 查找应该放在的那个位置
  insort = insort_right   # backward compatibility   --- insort的默认方式
  如果说我们插入的函数或者说数据已经存在了，然后
  def insort_left(a, x, lo=0, hi=None):   ------》 我们就能将这些数据插入在之前
  def bisect_right(a, x, lo=0, hi=None):  ------》 我们就能将这些数据插入在之后
  bisect = bisect_right   # backward compatibility 是biset的默认方式

2 如果我们在项目开发中，需要去维持好一个排序好的序列我们推荐是使用bisect
deque 双档序列数据类型

3 1==1.0 相等的时候我们需要排序这个时候我们就需要使用 bisect
3 分数排序的时候  等等一些吧
"""
import bisect
from collections import deque

# 二分查找性能比较高 升序
# insert_list = [] 这里只需要是序列类型就OK了
insert_list = deque()
bisect.insort(insert_list, 3)
bisect.insort(insert_list, 4)
bisect.insort(insert_list, 2)
bisect.insort(insert_list, 5)
bisect.insort(insert_list, 1)

print(bisect.bisect(insert_list, 33))  # 在right后进行插入 也就是第5个位置
print(bisect.bisect(insert_list, 3))  # 在找到重复位置后在进行一个插入工作 第3个位置
print(bisect.bisect_left(insert_list, 3))  # 在找到重复位置后在进行一个插入工作 第3个位置
print(insert_list)  # [1, 2, 3, 4, 5]
