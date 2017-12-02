# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


# -*-coding:utf-8-*-

import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import random
from scrapy import signals
import random
import scrapy
import logging
import time
import os
class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            # 显示当前使用的useragent
            # print "********Current UserAgent:%s************" % ua
            #
            # # 记录
            # logging.info('Current UserAgent: ' + ua)
            request.headers.setdefault('User-Agent', ua)

    def process_exception(self, request, exception, spider):
        # proxy = self.get_random_proxy()
        # # print("this is response ip:" + proxy)
        # logging.info('retry-----Current ip: ' + proxy)
        # # 对当前request加上代理
        # request.meta['proxy'] = proxy
        print exception
        return request
        # proxy = request.meta['proxy']
        # logging.msg('Removing failed proxy <%s>, %d proxies left' % (
        #     proxy, len(self.proxies)))
        # the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape

    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
class ProxyMiddleWare(HttpProxyMiddleware):
    """docstring for ProxyMiddleWare"""

    def __init__(self, ip=''):
        self.ip = ip
    def process_request(self, request, spider):
        '''对request对象加上proxy'''

        proxy = self.get_random_proxy()
        print("this is request ip:" + proxy)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200 & response.status != 301:
            proxy = self.get_random_proxy()
            print('wrong:'+str(response.status))
            logging.info('Current ip: ' + proxy)
            # 对当前request加上代理
            request.meta['proxy'] = proxy
            return request
        # with open(os.getcwd() + '/doubancomment/spiders/proxies.txt', 'wr') as f:
        #     total=f.read()
        #     f.write(total.replace(request.meta['proxy']+'\n','aaa'))
        return response
    def process_exception(self, request, exception, spider):
        logging.info('gg')
    #     # proxy = self.get_random_proxy()
    #     # # print("this is response ip:" + proxy)
    #     # logging.info('retry-----Current ip: ' + proxy)
    #     # # 对当前request加上代理
    #     # request.meta['proxy'] = proxy
    #     return request
    #     # proxy = request.meta['proxy']
    #     # logging.msg('Removing failed proxy <%s>, %d proxies left' % (
    #     #     proxy, len(self.proxies)))
    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open(os.getcwd()+'/doubancomment/spiders/proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy
# class ProxyMiddleWare(HttpProxyMiddleware):
#  def __init__(self, ip=''):
#         self.ip = ip
#  # overwrite process request
#  def process_request(self, request, spider):
#      # Set the location of the proxy
#      request.meta['proxy'] = "http://221.224.132.174:53281"
#      print request.meta['proxy']
