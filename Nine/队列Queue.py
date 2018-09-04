import queue

"""
队列
"""

# q = queue.Queue()  # 生成队列对象 正常的生成queue队列对象
# q.put("d1")
# q.put("d2")
# q.put("d3")
#
# print(q.qsize())  # 查看队列大小
#
# print(q.get())
# print(q.get())
#
# print(q.qsize())  # 查看队列大小

# q = queue.LifoQueue()  # 生成一个先入后出的对象
#
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())

q = queue.PriorityQueue()  # 设置优先级的队列 优先级的Q
q.put((-1,"cheng"))
q.put((11,"bei"))
q.put((5,"guo"))


print(q.get())
print(q.get())
print(q.get())



