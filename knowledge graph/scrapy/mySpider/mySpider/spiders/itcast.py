# -*- coding: utf-8 -*-
import scrapy
#from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    
    
    def parse(self, response):
        #with open("teacher.html", "w", encoding='utf-8') as f:
            #f.write(response.text)
        
        #item= {}
        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item= {}
            item['name'] = li.xpath(".//h3/text()").extract()[0]           ## 如何知道取第一个词 调试？ scrapy怎么调试？
            item['level'] = li.xpath(".//h4/text()").extract_first()
            #print(item)
            
            yield item       #减少
            
