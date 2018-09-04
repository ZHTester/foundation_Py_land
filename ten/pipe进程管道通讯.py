"""

pipe  管道通讯  进程
数据的传递 而不是数据的共享
"""
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])  # 儿子send数据
    conn.send([42, None, 'hello2'])  # 儿子send数据
    print("收到父进程消息:",conn.recv())  # 收到父进程的消息
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 生成2个管道实例 一生成就会产生2个管道对象 一个是管道的这一头 一个是管道的另一头
    p = Process(target=f, args=(child_conn,)) # 启动进程来传递儿子进程的消息
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']" 父亲管道收集消息
    parent_conn.send("我很好")  # 发给子进程的消息
    p.join()
