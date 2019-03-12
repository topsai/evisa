# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    thailind_url = 'https://www.evisathailand.com/terms'

    def parse(self, response):
        pass
