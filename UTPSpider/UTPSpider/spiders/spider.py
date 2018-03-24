# -*- coding: utf-8 -*-

from UTPSpider.items import ContentItem
from scrapy_redis.spiders import RedisSpider
from scrapy_splash import SplashRequest
import re
from urllib import parse
import time

class UTPSpider(RedisSpider):
    name = "UTPSpider"
    allowed_domains = set()
    redis_key = 'UTPSpider:start_urls'
    disallowed_domains = [r"\\", "#", "javascript:showAll()"]

    def make_request_from_data(self, data):
        """Returns a Request instance from data coming from Redis.

        By default, ``data`` is an encoded URL. You can override this method to
        provide your own message decoding.

        Parameters
        ----------
        data : bytes
            Message from redis.

        """
        url = str(data, self.redis_encoding)
        # 加入新的 allowed_domains
        self.allowed_domains.add(parse.urlparse(url).netloc)
        return self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        # dont_filter=True URL不参与去重
        return SplashRequest(url, callback=self.parse, args={'wait': 1}, dont_filter=True)

    def parse(self, response):
        # post_urls = response.css("#newsList ul li a::attr(href)").extract()
        # for post_url in post_urls:
        #     yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        print(self.allowed_domains)
        page_content = response.body

        re_patrn = '<a[^>]+?href=["\']?([^"\'#]+)["\']?[^>]*>([^<]+)</a>'
        a_list = re.findall(re_patrn, str(page_content))

        for a in a_list:
            if a[0] not in self.disallowed_domains:
                new_url = parse.urljoin(response.url, a[0])
                # print(new_url)
                yield SplashRequest(url=new_url, callback=self.parse_detail, args={'wait': 1})

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
