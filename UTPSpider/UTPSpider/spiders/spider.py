# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from urllib import parse
from newspaper import Article
from UTPSpider.items import ContentItem
from scrapy_redis.spiders import RedisSpider
import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

class UTPSpider(RedisSpider):
    name = "UTPSpider"
    allowed_domains = ["ccgp-jiangsu.gov.cn"]
    redis_key = 'UTPSpider:start_urls'

    def start_requests(self):
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
        r = redis.Redis(connection_pool=pool)
        url = "http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/index.html"
        r.lpush("UTPSpider:start_urls", url)
        yield Request(url=url, callback=self.parse)

        #['http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/index_'+ str(i) +'.html' for i in range(1,100)]

    def parse(self, response):
        post_urls = response.css("#newsList ul li a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

    def parse_detail(self, response):
        item = ContentItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@class="dtit"]/h1/text()').extract()[0].strip()
        article = Article(response.url, language='zh')
        article.download()
        article.parse()
        item['detail'] = article.text
        yield item
