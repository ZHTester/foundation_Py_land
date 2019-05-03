# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/2  10:43'
"""
--- https请求  证书验证测试 ---
1 配置一个ssl安全证书 
2 verify=False 修改默认请求 不添加https ssl认证 
3 如果你将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证 
4 默认情况下， verify 是设置为 True 的。选项 verify 仅应用于主机证书

"""
import requests

r = requests.get('https://kennethreitz.org', verify=False).text
print(r)

print('-----------------------------------')

r = requests.get('https://kennethreitz.org', verify=True).text
print(r)



































