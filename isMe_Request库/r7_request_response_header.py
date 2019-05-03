# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/2  9:33'
"""
返回headers  ~ 

"""
import requests


# 获取响应体的headers
def get_headers():
    r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
    print(r.headers)  # 返回响应头的headers
    print('-------------------')
    print(r.request.headers)  # 获取请求的headers


# 延长获取请求响应体 以流的形式获取
def request_stream():
    tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
    r = requests.get(tarball_url, stream=True)  # stream(根据流的形式) 响应体被下载下来了
    with open('2.txt', 'wb') as fp:
        for check in r.iter_content(128):
            fp.write(check)  # 这里就写入到文件了
    print(r.reason)  # 查看请求返回体
    print(".......请求体正常下载到文件中.......")


# request 代理设置
def request_proxies():
    # 代理设置
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }

    r = requests.get("http://example.org", proxies=proxies)
    return r.text


if __name__ == "__main__":
    request_proxies()
