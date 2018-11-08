"""
爬虫
 1 断点调试 ~ 十分重要需要十分去了解
 2


"""
from urllib import request
import requests


class SpiderDemo(object):
    url = "https://www.panda.tv/cate/lol?pdt=1.24.s1.3.2eomf7ua40b"

    def __fech__content(self):
        r = request.urlopen(SpiderDemo.url)  # 实例方法  打开这个URL
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')  # 这样就是转换成了编码

    def __analysis(self,htmls):
        pass

    def go(self):
        """
        这个方法就是__fech__content入口方法
        :return:
        """
        self.__fech__content()
        self.__analysis(self.htmls)


spider = SpiderDemo()
spider.go()
