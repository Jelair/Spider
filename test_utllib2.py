# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_utllib2
   Description :
   Author :       simplefly
   date：          2017/12/26
-------------------------------------------------
   Change Activity:
                   2017/12/26:
-------------------------------------------------
"""
__author__ = 'simplefly'

import urllib.request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法')
response = urllib.request.urlopen(url)
print(response.getcode())
print(len(response.read()))

print('第二种方法')
request = urllib.request.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode(), len(response2.read()))

print('第三种方法')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.read(), cj)

#HTTPCookieProcessor登陆处理
#ProxyHandler代理访问
#HTTPSHandler加密访问
#HTTPRedirectHandler自动调整关系