# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from lianjia.items import LianjiaItem

class FourSpider(Spider):
    name = 'four'
    allowed_domains = ['sz.lianjia.com']

    def start_requests(self):        
        # 设置链接的爬取规则
        # 总价300-400万的二手房页面链接
        # 低楼层
        for a in range(1,51):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(a) + 'lc1p3/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True)  

        # 中楼层
        for b in range(1,67):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(b) + 'lc2p3/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True)    

        # 高楼层
        for b in range(1,56):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(b) + 'lc3p3/'
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
            item['price_setp'] = '300-400万'
            print(item)
            yield item

            # 11009-6171 = 4838  (5088)
