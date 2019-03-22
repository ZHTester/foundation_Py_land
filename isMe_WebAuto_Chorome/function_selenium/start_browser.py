# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/21  10:46'
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()


def driver_ini():
    driver.get("http://pc.350gtv-intranet.com/#/login")
    driver.maximize_window()
    time.sleep(5)


def get_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


def run_main():
    driver_ini()
    print(EC.title_contains("用户名为4-12个小写字母"))
    get_element('//*[@id="login"]/div/div[2]/div[2]/div/div/div/ul/li[1]/input').send_keys('dstest0001')
    print(EC.title_contains('密码为8-12个英文字母或数字'))
    get_element('//*[@id="login"]/div/div[2]/div[2]/div/div/div/ul/li[2]/input').send_keys('aeuio888')
    time.sleep(5)
    get_element('//*[@id="login"]/div/div[2]/div[2]/div/div/div/div[2]/button').click()


run_main()

