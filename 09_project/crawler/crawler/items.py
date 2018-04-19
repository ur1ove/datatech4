# -*- coding: utf-8 -*-

import scrapy

class CrawlerItem(scrapy.Item):
    status = scrapy.Field()
    auctionDate = scrapy.Field()
    auctionInfo = scrapy.Field() 
    addr0 = scrapy.Field() 
    addr2 = scrapy.Field() 
    court = scrapy.Field() 
    addr1 = scrapy.Field() 
    itemNo = scrapy.Field() 
    regDate = scrapy.Field() 
    caDesc = scrapy.Field() 
    addrInfo = scrapy.Field() 
    caNo = scrapy.Field() 
    auctionTel = scrapy.Field() 
    itemType = scrapy.Field() 
    valueMin = scrapy.Field() 
    updDate = scrapy.Field() 
    id = scrapy.Field() 
    addr = scrapy.Field() 
    value = scrapy.Field() 
    auctionLoc = scrapy.Field() 
    remarks = scrapy.Field() 

class MeagakItem(scrapy.Item):
    caNo = scrapy.Field() 
    value = scrapy.Field() 
    refers = scrapy.Field() # array
