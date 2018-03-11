# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from urllib import parse
from newspaper import Article
from UTPSpider.items import ContentItem


class UTPSpider(scrapy.Spider):
    name = "UTPSpider"
    allowed_domains = ["ccgp-jiangsu.gov.cn"]

    def start_requests(self):
        urls = [
            'http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/index_99.html',
        ]
        i = 1
        while i < 1:
            urls.append('http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/index_' + str(i) + '.html')
            i += 1
        for url in urls:
            yield Request(url=url, callback=self.parse)

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
