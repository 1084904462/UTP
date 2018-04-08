# -*- coding: utf-8 -*-
from newspaper import Article

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

    script = """
    function getAll(splash)
        local next = splash:jsfunc([[
            function()
            {
                return $('a').filter(\":contains('下一页'), :contains('>')\")[0]
            }
        ]])
        local i = 0
        local res = {}
        local btn = next()
        
        while(btn ~= nil)
        do
            if(i >= 200)
            then
                break
            end
            print(i)
            splash:runjs(btn.click())
            splash:wait(splash.args.wait)
            res[i] = splash:evaljs("$('html').html()")
            
            i = i+1
            btn = next()
        end
        
        return res
    end
    function main(splash, args)
        splash.resource_timeout = 1800
        assert(splash:go(args.url))
        splash:wait(args.wait)
        splash:autoload("https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js")
        return getAll(splash)
    end
    """

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
        return SplashRequest(url,
                             callback=self.parse,
                             meta={'download_timeout': 1800},
                             endpoint="execute",
                             args={'lua_source': self.script, 'wait': 1.0, 'images_enabled': False},
                             dont_filter=True)

    def parse(self, response):
        list_pages = eval(str(response.body, "utf8"))
        print(len(list_pages))
        for k in list_pages:
            list_page = list_pages[k]
            re_patrn = '<a[^>]*href=["\']([^"\']+)?["\']?[^>]*>(.*?)</a>'
            a_list = re.findall(re_patrn, list_page)
            for a in a_list:
                if a[0] not in self.disallowed_domains:
                    yield SplashRequest(url=parse.urljoin(response.url, a[0]), callback=self.parse_detail, args={'wait': 1})

        # page_content = response.body
        # re_patrn = '<a[^<]*>(&gt;|下一页)<\/a>'
        # a_list = re.findall(re_patrn, str(page_content, "utf8"))
        # print(eval(str(response.body, "utf8")))
        # print(a_list)
        # if a_list:
        #     print(response.css(".fanye").extract_first("不存在"))
        #     yield SplashRequest(url=response.url,
        #                         callback=self.parse,
        #                         meta={'download_timeout': 1800},
        #                         endpoint="execute",
        #                         args={'lua_source': self.script, 'wait': 0.5, 'images_enabled': False},
        #                         dont_filter=True)

        # TODO:判断列表页还是内容页还是无关页面

    def parse_detail(self, response):
        item = ContentItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@class="dtit"]/h1/text()').extract_first("不存在").strip()
        if item['title'] != "不存在":
            article = Article(response.url, language='zh')
            article.download()
            article.parse()
            item['detail'] = article.text
            yield item
