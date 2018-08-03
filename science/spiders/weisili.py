# -*- coding: utf-8 -*-
import scrapy
from science.items import ScienceItem

class WeisiliSpider(scrapy.Spider):
    name = 'weisili'
    allowed_domains = ['kehuan.net.cn']
    start_urls = ['http://www.kehuan.net.cn/book/weisili.html']

    def parse(self, response):
        item = ScienceItem()
        dls =  response.xpath('//dl')
        for dl in dls:
            item['book_name'] = dl.xpath('dt').extract()
        yield item