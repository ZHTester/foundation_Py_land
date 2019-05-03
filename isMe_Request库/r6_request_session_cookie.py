# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/29  14:28'
"""
1 requests 中的 session cookie
2 session是服务器存储的数据信息，cookie是浏览器端存储的一些信息。

"""
import requests
#
sess_url = 'http://1029a.s1119.com/m/php/action.php?action=login'
Data = {
         "username": "dstest0003",
         "password": "aeuio888"
        }

s = requests.Session()
r = s.post(data=Data, url=sess_url)  # 请求登录
print(r.cookies.get_dict())
print(r)






