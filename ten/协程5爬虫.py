"""

网络爬虫 抓取网页

"""

from gevent import monkey;
import gevent
from urllib import request

"""
# 把当前程序所有的io操作给我单独的做上标记 
# monkey.patch_all() 把所有的线程标记成线程来执行

"""


monkey.patch_all()



def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    # f = open('url.html','wb')
    # f.write(data)
    # f.close()
    print('%d bytes received from %s.' % (len(data), url))


# 自动切换带函数 带有参数
gevent.joinall([gevent.spawn(f, 'https://www.python.org/'), gevent.spawn(f, 'https://www.yahoo.com/'),
                gevent.spawn(f, 'https://github.com/'), ])

# f("http://www.baidu.com/")
