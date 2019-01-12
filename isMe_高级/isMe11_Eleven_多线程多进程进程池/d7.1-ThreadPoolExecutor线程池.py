# coding=utf-8
import time

__author__ = 'landing'
__data__ = '2019/1/10  17:26'

"""
ThreadPoolExecutor 线程池 
  获取已经成功的task返回结果 这个时候我们就要使用as_completed这样的方法 as_completed(这东西就是一个生成器
  把已经完成的task yield出来)
  as_completed --- 主线程生成器
  ***************** 这一部分就是先拿出已经运行好的线程
      if timeout is not None:
        end_time = timeout + time.time()

    fs = set(fs)
    total_futures = len(fs)
    with _AcquireFutures(fs):
        finished = set(
                f for f in fs
                if f._state in [CANCELLED_AND_NOTIFIED, FINISHED])
        pending = fs - finished
        waiter = _create_and_install_waiters(fs, _AS_COMPLETED)
    finished = list(finished)
        try:
        yield from _yield_finished_futures(finished, waiter,
                                           ref_collect=(fs,))    ***** 这里就会yield出去了
                                           
     while pending:   ------ 这里也就是将剩下的线程pending出去
            if timeout is None:
                wait_timeout = None
            else:
                wait_timeout = end_time - time.time()
                if wait_timeout < 0:
                    raise TimeoutError(
                            '%d (of %d) futures unfinished' % (
                            len(pending), total_futures))                  
                                           
"""
from concurrent.futures import ThreadPoolExecutor, as_completed, wait


def get_html(times):
    time.sleep(times)
    print("get page {} sucess".format(times))
    return times


# ThreadPoolExecutor 实例化对象 --> def __init__(self, max_workers=None, thread_name_prefix=''):
# 线程池中同时运行多少个线程 max_workers
# 实例化线程池对象
excutor = ThreadPoolExecutor(max_workers=2)

"""这些就是futures给我们带来的一些方法与函数的好处"""
# 我们使用submit添加函数到线程池中,然后submit这个函数是存在返回值的 这就是futures类对象
# submit是立刻返回，非阻塞的
"""获取已经成功的task返回结果 这个时候我们就要使用as_completed这样的方法"""
urls = [4, 3, 2, 5, 6, 7]  # 这里也就是sleep 请求多少秒
all_task = [excutor.submit(get_html, url) for url in urls]
for future in as_completed(all_task):  # 这样就能完成这样的一个获取然后返回正确的task
    data = future.result()
    print("get {} page ".format(data)) # excutor.map() 这样的方法就是比这样的方式更加的简单

# # 通过excutor获取已经完成的task 这里就是根据Url的顺序进行执行的
# for data in excutor.map(get_html, urls):
#     print("get {} page ".format(data))

