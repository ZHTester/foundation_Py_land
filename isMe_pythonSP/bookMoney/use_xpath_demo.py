# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/5  15:54'
"""
xpath的使用方式 
1 读取文件中的类容 
2 解析H3标题 
"""
from lxml import html
import requests


def parse():
    f = open("./static/index.html", "r", encoding="utf-8")
    s = f.read()
    selector = html.fromstring(s)  # 这里我们就得到一个xpath对象
    h3 = selector.xpath('/html/body/h3/text()')  # 获取到html中的数据 通过html文件
    print(h3[0], "\n")

    # 循环获取到ul中的值 text
    url1 = selector.xpath('/html/body/ul/li')
    for li in url1:
        print(li.xpath('text()')[0])
    print(len(url1), "\n")

    # 通过属性来获取值 属性选择器选择对应属性的值
    url2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(url2[0], "\n")

    # 获取标签中的值-解析a标签中的值  //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../@属性n
    a = selector.xpath('//div[@id="container"]/a')
    print(a[0].xpath('text()')[0])  # 获取标签对象值
    print(a[0].xpath('@href')[0], "\n")  # 获取属性值

    # 解析p标签 last() 获取最后一个元素方式
    p = selector.xpath('/html/body/p[last()]/text()')
    print(len(p), "\n")
    print(p[0])

    f.close()


if __name__ == "__main__":
    parse()
