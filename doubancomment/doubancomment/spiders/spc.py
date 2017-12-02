# -*- coding: utf-8 -*-
import re
import scrapy
from urlparse import urljoin
# import urllib.parse
# import urllib.request
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
from scrapy.conf import settings
import os.path
import json
from doubancomment.items import DoubancommentItem
class LessionSpider(scrapy.Spider):
    name = 'see'
    data_path = './data/kompas'
    cache = './cache/kompas.cache'
    cache_size = 20
    comparsse_size = 10000
    def start_requests(self):
        rootdir = "/home/hadoopnew/下载/test"
        # 'test':'http://www.baidu.com'
        classifications = { '兄弟，别闹！':'26816087',}
                            # '东方快车谋杀案':'25790761',
                            # '小丑回魂':'3604148'}
        # for parent, dirnames, filenames in os.walk(rootdir):
        #     # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #     for dirname in dirnames:
        #         c = rootdir + "/" + dirname
        #         for p, d, f in os.walk(c):
        #             for file in f:
        #                 ff = open(c + "/" + file, 'r')
        #                 for line in ff.readlines():
        #                     s = line.split("`")
        #                     classifications[s[0]]=s[1].replace("\n","")
# "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"

        for classification, id in classifications.items():
            url="http://movie.douban.com/subject/"+id
            print classification
            yield scrapy.Request(url=url, callback=self.parse,dont_filter = True,meta={
            'data': {
                'name':classification,
                'request_url': url,
            }
        })

    def parse(self, response):
        print response.meta['proxy']
        attrs=response.xpath("//div[@id='info']//span[@class='actor']//span[@class='attrs']//a/@href").extract()
        for i in attrs:
            url = "http://movie.douban.com/"+i
            # print url
            yield scrapy.Request(url=url, callback=self.actor,meta={
                'data': {
                    'starid': i.split("/")[-2],
                }
            })
    def actor(self, response):
        total=response.xpath("//div[@id='recent_movies']//div//h2//span//a/@href").extract_first()
        starname= response.xpath("//title//text()").extract_first().encode("utf-8").replace("\n","").replace("(豆瓣)","").replace(" ","")
        yield scrapy.Request(url=total, callback=self.movielist, dont_filter = True,meta={
            'data': {
                'starid': response.meta['data']['starid'],
                    'starname':starname
            }
        })
    def movielist(self,response):
        list=response.xpath("//ul[@class='']//li//dl//h6//a/@href").extract()
        for i in list:
            yield scrapy.Request(url=i, callback=self.movie,dont_filter = True,meta={
                'data': {
                    'starid': response.meta['data']['starid'],
                    'starname':response.meta['data']['starname'],
                }
            })
        nexturl=response.xpath("//span[@class='next']//a//@href").extract_first()
        if nexturl!=None:
            a = response.url.split("?")[0]
            url= a+ nexturl
            yield scrapy.Request(url=url, callback=self.movielist, dont_filter = True,meta={
                'data': {
                    'starid': response.meta['data']['starid'],
                        'starname':response.meta['data']['starname'],
                }
            })
    def movie(self, response):
        score=response.xpath("//div[@class='rating_self clearfix']//strong//text()").extract_first()
        if score==None:
            return
        time=response.xpath("//span[@property='v:initialReleaseDate']//text()").extract_first()
        time=time.split('-')[0]
        name=response.xpath("//span[@property='v:itemreviewed']//text()").extract_first()
        data={}
        data['time']=time
        data['name']=name
        data['score']=score
        data['id']=response.meta['data']['starid']
        data['starname']=response.meta['data']['starname']
        # print data
        yield DoubancommentItem(data)