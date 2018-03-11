# -*- coding: utf-8 -*-

import scrapy


class ContentItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    detail = scrapy.Field()
