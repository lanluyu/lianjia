# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spider import CrawlSpider

class ShenzhenSpider(CrawlSpider):
    name = 'shenzhen'
    allowed_domains = ['https://sz.lianjia.com/']
    start_urls = ['https://sz.lianjia.com/ershoufang/pg1/']

    def parse(self,response):
        #获取每一页的详情链接
        links = response.xpath('.//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.parse_house)
        # 获取下一页的链接
        i = 1
        while i <= 100:
            next_url = 'https://sz.lianjia.com/ershoufang/pg'+ str(i) + '/'
            i = i+1
            yield scrapy.Request(next_url,callback=self.parse)           
        print(response.url)

    def parse_house(self, response):
        print(response.url)
        i = {}
        i['house_title'] = response.xpath('.//h1[@class="main"]/text()').extract_first()
        i['house_room'] = response.xpath('.//div[@class="room"]/div[1]/text()').extract_first()
        i['house_area'] = response.xpath('.//div[@class="area"]/*/text()').extract_first()
        i['house_location'] = response.xpath('.//div[@class="areaName"]/span[@class="info"]/*/text()').extract_first()
        i['house_price'] = response.xpath('.//span[@class="total"]/text()').extract_first()+response.xpath('.//span[@class="unit"]/span/text()').extract_first()
        print(i)
        return i
