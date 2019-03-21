# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/21  10:46'
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge()
driver.get("http://pc.350gtv-intranet.com/#/login")
driver.maximize_window()
time.sleep(5)

print(EC.title_contains("用户名为4-12个小写字母"))
name_element = driver.find_element_by_xpath('//*[@id="login"]/div/div[2]/div[2]/div/div/div/ul/li[1]/input')
name_element.send_keys('dstest0001')
print(EC.title_contains('密码为8-12个英文字母或数字'))
password_element = driver.find_element_by_xpath('//*[@id="login"]/div/div[2]/div[2]/div/div/div/ul/li[2]/input')
password_element.send_keys('aeuio888')

time.sleep(5)
password_element = driver.find_element_by_xpath('//*[@id="login"]/div/div[2]/div[2]/div/div/div/div[2]/button')
password_element.click()






