# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     html_downloader
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

class HtmlDownLoader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        print(response.read())
        if response.getcode() != 200:
            print('request failed', url)
            return None
        return response.read()