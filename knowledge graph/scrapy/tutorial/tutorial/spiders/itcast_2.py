# -*- coding: utf-8 -*-
import scrapy


class Itcast2Spider(scrapy.Spider):
    name = 'itcast_2'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        ret1 = response.xpath("//div[@class='tea_hd']//h3/text()")
        print(ret1)


