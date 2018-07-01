# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from lianjia.items import LianjiaItem

class Three2Spider(Spider):
    name = 'three2'
    allowed_domains = ['sz.lianjia.com']

    def start_requests(self):        
        # 设置链接的爬取规则
        # 总价200-300万的二手房页面链接
        # 高楼层
        for i in range(1,50):
            url = 'https://sz.lianjia.com/ershoufang/pg'+ str(i) + 'lc3p2/'
            yield Request(url=url,callback=self.parse_house,dont_filter=True)         

    def parse_house(self,response):
        print(response.url)
        #a = response.xpath('.//a[@class="on"]/text()').extract_first()
        #print('正在爬取第',self.i,'页')
        houses = response.xpath('.//ul[@log-mod="list"]/li')
        for house in houses:
            item = LianjiaItem()
            item['house_title'] = ''.join(house.xpath('.//div[@class="title"]/a/text()').extract())
            item['house_community'] = ''.join(house.xpath('.//div[@class="houseInfo"]/a/text()').extract())
            item['house_room'] = ''.join(house.xpath('.//div[@class="houseInfo"]//text()').extract()[1].split("|")[1].strip())
            item['house_area'] = ''.join(house.xpath('.//div[@class="houseInfo"]//text()').extract()[1].split("|")[2].strip())
            item['house_location'] = ''.join(house.xpath('.//div[@class="positionInfo"]/a/text()').extract())
            item['house_price'] = ''.join(house.xpath('.//div[@class="totalPrice"]//text()').extract())
            item['price_setp'] = '200-300万高楼层'
            print(item)
            yield item

            # 6171-4832 = 1339  (1429)

            '''
            https://m.lianjia.com/sz/ershoufang/pg40lc3p2/
            https://m.lianjia.com/sz/ershoufang/pg43lc3p2/
            https://m.lianjia.com/sz/ershoufang/pg44lc3p2/
            部分链接为移动端页面，与网页版规则不同，无法抓取其信息
            '''
