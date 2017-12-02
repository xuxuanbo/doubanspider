# -*- coding: utf-8 -*-

# Scrapy settings for doubancomment project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubancomment'

SPIDER_MODULES = ['doubancomment.spiders']
NEWSPIDER_MODULE = 'doubancomment.spiders'

# USER_AGENT ="Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubancomment (+http://www.yourdomain.com)'
# REDIRECT_ENABLED = False
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'doubancomment.middlewares.RotateUserAgentMiddleware': 400,
   # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
   'scrapy_crawlera.CrawleraMiddleware': 600,
   # 'doubancomment.middlewares.ProxyMiddleWare': 100,
   'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
   'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None,

}
CRAWLERA_ENABLED = True
CRAWLERA_USER = '<ea07f32e390140c7bda828b0a8425720>'
CRAWLERA_PASS = ''
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubancomment.middlewares.DoubancommentSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doubancomment.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
COOKIES_ENABLED=False
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'doubancomment.pipelines.DoubancommentPipeline': 300,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
# COOKIE={'__utmv': '30149280.9174', 'ps': 'y', '__utmz': '30149280.1504065758.9.5.utmcsr', 'ck': 'TAK4', 'ap': '1', 'll': '"118284"', '__utmt': '1', 'dbcl2': '"91745419:UOPIL4xD0oI"', '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1504065754%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl0Lhq3pX88eZadBLfTazyS8mf2Ye-tEVFmYiwXkOtiG%26wd%3D%26eqid%3D96655fcb000312920000000659a61d55%22%5D', '_vwo_uuid_v2': '1E3D217CC82F9CDBC96C1A952D54F885|11fcbef4c29b73b9ed83989cfd754468', 'push_doumail_num': '0', '__yadk_uid': 'wv10DQNPRNRuV04LiseN8eFM4HxhS66b', '_pk_id.100001.8cb4': '31b03f8d980b880c.1503538168.7.1504065754.1504058922.', '_pk_ses.100001.8cb4': '*', 'push_noty_num': '0', 'ue': '"747561582@qq.com"', '__utma': '30149280.1865417050.1503538177.1504058716.1504065758.9', '__utmb': '30149280.2.10.1504065758', '__utmc': '30149280', 'bid': '_rlToGT79Io', 'ct': 'y'}
DOWNLOAD_TIMEOUT = 10
# COOKIES_DEBUG=True
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = [301,302]
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# DEFAULT_REQUEST_HEADERS={'Cookie':'ll="118284"; bid=_rlToGT79Io; __utma=30149280.1865417050.1503538177.1504013512.1504053848.7; __utmz=30149280.1504010475.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ps=y; ue="747561582@qq.com"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.9174; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1504053845%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=baf246aafa2320ed.1503538415.7.1504054394.1504021586.; __utma=223695111.2116685979.1503538415.1504013512.1504053848.7; __utmz=223695111.1504010475.5.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=Tp3mCijCDbvqUxbcfDXNAWiAMZTA8WMS; _vwo_uuid_v2=1E3D217CC82F9CDBC96C1A952D54F885|11fcbef4c29b73b9ed83989cfd754468; ct=y; ap=1; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1504053848; __utmc=30149280; __utmb=223695111.0.10.1504053848; __utmc=223695111; report=ref=%2F&from=mv_a_pst'}