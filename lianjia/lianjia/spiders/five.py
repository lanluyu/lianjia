# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from lianjia.items import LianjiaItem

class FiveSpider(Spider):
    name = 'five'
    allowed_domains = ['sz.lianjia.com']

    def start_requests(self):        
        # 设置链接的爬取规则
        # 总价400-500万的二手房页面链接
        # 中低楼层
        for a in range(1,100):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(a) + 'lc1lc2p4/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True) 
        # 高楼层
        for b in range(1,45):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(b) + 'lc3p4/'
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
            item['price_setp'] = '400-500万'
            print(item)
            yield item

            # 14934-11009 = 3925  (4237)

