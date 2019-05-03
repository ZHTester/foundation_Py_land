# coding=utf-8
__author__ = 'landing'
__data__ = '2019/4/25  11:39'
"""
1 通过response 的api我们来进行图片的下载 使用request库的方式进行下载
2 r.content 获取文本信息 图片信息是不能被content解析的 这会被转译成2进制编码的
3 文件流存入到文件中 -----> 这样的一个模式要明白

"""
import requests


def download_picture():
    url = 'http://cdn.onlinewebfonts.com/svg/img_326384.png'
    # stream=True 以流的形式传输到我们的返回值中，然后在读取数据
    r = requests.get(url=url, stream=True)  # 流的形式下载文件
    with open('2.png', 'wb') as fp:
        for check in r.iter_content(128):
            fp.write(check)  # 这里就写入到文件了
    print(r.reason)
    print(".......图片下载成功.......")


if __name__ == "__main__":
    download_picture()
