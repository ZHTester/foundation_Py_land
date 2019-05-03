# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/2  15:10'
"""
put 接口和 deleted 接口的使用
301 302 303 重定向 重定域  通过
    1 allow_redirects=False的意义为拒绝默认的301/302/303
      重定向从而可以通过response.headers['Location']拿到重定向的URL

"""

import requests

url = ""
data = {

}
# post 请求相当于
r = requests.put(url=url, data=data).text
print(r)

# get请求 相当于
r1 = requests.delete(url).text
print(r1)







