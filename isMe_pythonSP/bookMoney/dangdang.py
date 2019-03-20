# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/7  10:22'
"""
当当网 爬取数据
爬虫 



"""
import requests
from lxml import html


def spider(sn):
    url = "http://search.dangdang.com/?key={sn}=input".format(sn=sn)
    # 获取data
    html_data = requests.get(url).text  # 拿到文本内容
    # 将文本类容转换成xpath对象
    selector = html.fromstring(html_data)
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    for li in ul_list:
        title = li.xpath('a/@title')  # 标题
        print(title[0])
        href = li.xpath('a/@href')  # 连接
        print(href)
        money = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')  # 钱
        print(money[0].replace('¥', ' '))
        cbs = li.xpath('p[@class="search_shangjia"]/a/text()')  #
        print('dangdang自营' if cbs == [] else cbs[0])


if __name__ == "__main__":
    spider("Python编程 从入门到实践")








