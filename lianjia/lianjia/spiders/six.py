# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from lianjia.items import LianjiaItem

class SixSpider(Spider):
    name = 'six'
    allowed_domains = ['sz.lianjia.com']

    def start_requests(self):        
        # 设置链接的爬取规则
        # # 总价500-800万的二手房页面链接
        # 低楼层
        for a in range(1,63):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(a) + 'lc1p5/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True) 
        # 中楼层
        for b in range(1,69):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(b) + 'lc2p5/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True)  
        # 高楼层
        for c in range(1,60):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(c) + 'lc3p5/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True)  
      
    def parse_house(self,response):
        print(response.url)
        houses = response.xpath('.//ul[@log-mod="list"]/li')
        for house in houses:
            item = LianjiaItem()
            item['house_title'] = ''.join(house.xpath('.//div[@class="title"]/a/text()').extract())
            item['house_community'] = ''.join(house.xpath('.//div[@class="houseInfo"]/a/text()').extract())
            item['house_room'] = ''.join(house.xpath('.//div[@class="houseInfo"]//text()').extract()[1].split("|")[1].strip())
            item['house_area'] = ''.join(house.xpath('.//div[@class="houseInfo"]//text()').extract()[1].split("|")[2].strip())
            item['house_location'] = ''.join(house.xpath('.//div[@class="positionInfo"]/a/text()').extract())
            item['house_price'] = ''.join(house.xpath('.//div[@class="totalPrice"]//text()').extract())
            item['price_setp'] = '500-800万'
            print(item)
            yield item

            # 20213-14934 = 5279  (5589)
