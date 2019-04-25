# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/24  14:01'
"""
requests 响应api
1 response  _1 status_code 
            _2 reason
            _3 headers
            _4 url
            _5 elapsed
            _6 request
            _7 encoding
            _8 raw
            _9 content 
            _10 text  这里经过解析后的就变成了 unicode
            _11 json json我们会获得更多的东西

"""
import requests

url = "http://1029a.s1119.com/m/php/action.php?action=login"
data = {"username": "dstest0002",
        "password": "aeuio888"
        }
r = requests.post(url=url, data=data)

print(r.status_code)  # 返回状态码
print(r.reason)  # 返回是状态是否OK
print(r.headers)  # 返回headers
print(r.url)  # 返回请求地址
print(r.elapsed)  # 计算请求访问时间差
print(r.request)  # 获取请求方法
print(r.encoding)  # 获取编码方式
print(r.raw)
print(r.content)  # 获取编码类型
print(r.json())  # 转换为基本的api

