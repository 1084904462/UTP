# -*- coding: utf-8 -*-

from UTPSpider.items import ContentItem
from scrapy_redis.spiders import RedisSpider
from scrapy_splash import SplashRequest
import re
from urllib import parse

class UTPSpider(RedisSpider):
    name = "UTPSpider"
    allowed_domains = ["www.ccgp-jiangsu.gov.cn"]
    redis_key = 'UTPSpider:start_urls'

    # @classmethod
    # def add_allowed_domains(cls, url):
    #

    def make_requests_from_url(self, url):
        return SplashRequest(url, callback=self.parse)


    def parse(self, response):
        # post_urls = response.css("#newsList ul li a::attr(href)").extract()
        # for post_url in post_urls:
        #     yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        page_content = response.body

        re_patrn = '<a[^>]+?href=["\']?([^"\']+)["\']?[^>]*>([^<]+)</a>'
        a_list = re.findall(re_patrn, str(page_content))
        for a in a_list:
            new_url = parse.urljoin(response.url, a[0])
            yield SplashRequest(url=new_url, callback=self.parse)

        # TODO:判断列表页还是内容页还是无关页面


    def parse_detail(self, response):
        pass
        # item = ContentItem()
        # item['url'] = response.url
        # item['title'] = response.xpath('//div[@class="dtit"]/h1/text()').extract()[0].strip()
        # article = Article(response.url, language='zh')
        # article.download()
        # article.parse()
        # item['detail'] = article.text
        # yield item
