# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/11  14:52'
"""
京东网数据爬取

"""
from lxml import html
import requests


def spider(sn):
    url = "https://search.jd.com/Search?keyword={0}".format(sn)
    print(url)
    # 获取Html_data
    html_data = requests.get(url).text
    print(html_data)
    # 将文本类容转换成xpath对象
    selector = html.fromstring(html_data)
    # 找到列表的集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(ul_list))
    # 解析对于的类容 标题 价格 购买链接
    for li in ul_list:
        print(li)


if __name__ == "__main__":
    spider('Python编程 从入门到实践')











































