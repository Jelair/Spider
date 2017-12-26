# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     spider_main
   Description :
   Author :       simplefly
   date：          2017/12/26
-------------------------------------------------
   Change Activity:
                   2017/12/26:
-------------------------------------------------
"""
__author__ = 'simplefly'

from baike_spider import url_manager, html_parser, html_outputer, html_downloader

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print(' craw %d: %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count += 1
            except RuntimeError as e:
                print('craw failed', e)

if __name__=='__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)