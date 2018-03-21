# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from UTPSpider.items import ContentItem
from scrapy_redis.spiders import RedisSpider
import json
import re
# from fake_useragent import UserAgent
from urllib import parse
from newspaper import Article

import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

class UTPSpider(RedisSpider):
    name = "UTPSpider"
    # allowed_domains = ["ccgp-jiangsu.gov.cn"]
    redis_key = 'UTPSpider:start_urls'
    # ua = UserAgent()

    global splashurl
    splashurl = "http://localhost:8050/render.html"

    # def start_requests(self):
    #     pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    #     r = redis.Redis(connection_pool=pool)
    #     url = "http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/index.html"
    #     r.lpush("UTPSpider:start_urls", url)
    #     # yield Request(url=url, callback=self.parse)
    #     yield self.make_requests_from_url(url)


    # splash 服务器地址
    #此处是重父类方法，并使把url传给splash解析
    def make_requests_from_url(self, url):
        global splashurl
        url = splashurl + "?url=" + url
        body = json.dumps({"url": url, "wait": 5, 'images': 0, 'allowed_content_types': 'text/html; charset=utf-8'})
        headers = {'Content-Type': 'application/json'}
        return Request(url, body=body, headers=headers, dont_filter=True)


    def parse(self, response):
        # post_urls = response.css("#newsList ul li a::attr(href)").extract()
        # for post_url in post_urls:
        #     yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        real_url = re.match("(.*)url=(.*)", response.url).group(2)
        print(real_url)
        page_content = response.body

        re_patrn = '<a[^>]+?href=["\']?([^"\']+)["\']?[^>]*>([^<]+)</a>'
        a_list = re.findall(re_patrn, str(page_content))
        for a in a_list:
            print(parse.urljoin(real_url, a[0]))


    def parse_detail(self, response):
        item = ContentItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@class="dtit"]/h1/text()').extract()[0].strip()
        article = Article(response.url, language='zh')
        article.download()
        article.parse()
        item['detail'] = article.text
        yield item
