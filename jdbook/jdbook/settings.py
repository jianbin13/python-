# Scrapy settings for jdbook project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jdbook'

SPIDER_MODULES = ['jdbook.spiders']
NEWSPIDER_MODULE = 'jdbook.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
LOG_LEVEL = 'ERROR'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'referer': 'https://book.jd.com/',
    'cookie': '__jdu=1471728802; shshshfpa=171fca07-4e90-847f-dd02-5cb1aaf4340a-1648908790; shshshfpb=s4Eui0eXFOmI6r8GbPyPefQ; TrackID=1I0zKo7BOkPaMJn_uXWR_JXkvyT6CvkQ6QBuuX_LawP96Tc5xRiZ1jVudh2E05R0bgwPUcalJYXP66PUBYkmmpEF_AUm66mjLWCqFqSoNeJS4i8bpkKn2ijqwy0pwTeR4; pinId=0J3hC92JXK_SNWpFGfb8hi-MCYJsy2Hw; pin=jd_LEVLFcK4MJoXmCv; unick=jd_LEVLFcK4MJoXmCv; _tp=MgAsuOKX06%2FbsWx0enjr0pm3HpWh1GHboGZ0PYHIa74%3D; _pst=jd_LEVLFcK4MJoXmCv; areaId=19; ipLoc-djd=19-1601-50258-51885; PCSYCityID=CN_440000_440100_0; unpl=JF8EAJlnNSttWxlXBxsHTkJCHlUHW1hcS0dQO2MFVVtdTgFWEgBMGkd7XlVdXhRKEx9sZBRXXFNJUw4bBSsSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-SF1UXVsJSxMHbG4GZG1bS2QFGjIbFxZLW1dXVAlIJzNoVzVkXl1LXQ0SMhoiEXsfAAJYC00SC2sqBVFbWE1XDBIDGCIRe14; __jdv=76161171|baidu-search|t_262767352_baidusearch|cpc|211270155282_0_2c2314dacd9b44e1abe510744db83f9f|1653222978271; shshshfp=54bbf3cdfe6a7fb98d0920326139d69e; shshshsID=6223a5e02664cf3b15b414ce3a555d30_5_1653222979061; __jda=122270672.1471728802.1648908789.1653222920.1653222978.9; __jdc=122270672; 3AB9D23F7A4B3C9B=2SLSU46ZUYNPVD4WXSID3W3ZVDVM2TTAGINJZ2IGBKOGDBPDBGR7NU6BRONAT6QMJMK24DQKE2DVWA32RUW7AXACAM; __jdb=122270672.6.1471728802|9.1653222978'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jdbook.middlewares.JdbookSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jdbook.middlewares.JdbookDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'jdbook.pipelines.JdbookPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline': 300,
   'jdbook.pipelines.JdbookPipeline': 301,
}
# -- 指定可共享的调度器
# 增加一个去重容器类的配置，使用Redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化存储
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置调度器是否持久化，再爬虫结束后，是否清空Redis中请求队列和去重指纹的set
SCHEDULER_PERSIST = True

REDIS_HPST = "127.0.0.1"
REDIS_POST = 6379