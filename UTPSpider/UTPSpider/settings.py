# -*- coding: utf-8 -*-

BOT_NAME = 'UTPSpider'

SPIDER_MODULES = ['UTPSpider.spiders']
NEWSPIDER_MODULE = 'UTPSpider.spiders'


# 禁止cookies,防止被ban
COOKIES_ENABLED = False
COOKIES_ENABLES = False

DOWNLOAD_DELAY = 3.0

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'UTPSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SPLASH_URL = 'http://127.0.0.1:8050'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "UTPSpider.dupefilter.UTPSpiderRFPDupeFilter"
ITEM_PIPELINES = {
    'UTPSpider.pipelines.JsonPipeline': 200,
    'scrapy_redis.pipelines.RedisPipeline': 300
}
REDIS_START_URLS_AS_SET = True
DOWNLOADER_MIDDLEWARES = {
    'UTPSpider.middlewares.RandomUserAgentMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_splash.SplashCookiesMiddleware': 725,
    'scrapy_splash.SplashMiddleware': 730,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': None,
    'UTPSpider.middlewares.DynamicChangeAllowedDomainsMiddleware': 500
}
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
RANDOM_UA_TYPE = "random"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
# 默认请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'UTPSpider.middlewares.UtpspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'UTPSpider.pipelines.UtpspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
