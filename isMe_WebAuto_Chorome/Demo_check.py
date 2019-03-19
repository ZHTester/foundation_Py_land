# coding=utf-8
from lxml import html

__author__ = 'landing'
__data__ = '2019/3/14  9:46'
import requests
from selenium import webdriver
from PIL import Image
import time


url_selenium = 'http://pc.350gtv-intranet.com/#/login'
driver = webdriver.Edge()  # 启动win10的浏览器
driver.get(url_selenium)
driver.maximize_window()
time.sleep(5)
code_element = driver.find_element_by_xpath('//*[@id="login"]/div/div[2]/div[2]/div/div/div/ul/li[3]/img')  # 获取图片元素
driver.save_screenshot('./1.png')
print(code_element.location)  # 打印出坐标值
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left  # 获取整体的宽度
height = code_element.size['height'] + top
im = Image.open('./1.png')
cm = im.crop((left, top, right, height))  # 切图操作
cm.save('./2.png')  # 保存切图操作


driver.quit()


