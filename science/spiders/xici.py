# -*- coding: utf-8 -*-
import scrapy
from science.items import ScienceItem


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://xicidaili.com/']

    def start_requests(self):   # 制作链接
        reqs = []

        for i in range(1, 10):
            req = scrapy.Request("http://www.xicidaili.com/nn/%s" % i)
            reqs.append(req)

        return reqs

    def parse(self, response):
        trs = response.xpath('//table/tr')

        items = []

        for tr in trs[1:]:
            pre_item = ScienceItem()
            pre_item['IP'] = tr.xpath('td[2]/text()').extract_first()
            pre_item['PORT'] = tr.xpath('td[3]/text()').extract_first()
            pre_item['POSITION'] = tr.xpath('td[4]/a/text()').extract_first()
            pre_item['TYPE'] = tr.xpath('td[5]/text()').extract_first()
            pre_item['SPEED'] = tr.xpath('td[7]/div/@title').extract_first()
            pre_item['LAST_CHECK_TIME'] = tr.xpath('td[10]/text()').extract_first()
            items.append(pre_item)
        return items
