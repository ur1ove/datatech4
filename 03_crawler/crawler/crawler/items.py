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


class AuctionItem(scrapy.Item):
    """
    Houseinfo 사이트의 경매 물건 Model 
    """
   
    status = scrapy.Field()         # 상태 매각
    auctionCount = scrapy.Field()   # 입찰 회
    auctionDate = scrapy.Field()    # 경매일 3014-12-07
    addr = scrapy.Field()           # 전체 주소
    addr0 = scrapy.Field()          # 시/도
    addr1 = scrapy.Field()          # 구/군
    addr2 = scrapy.Field()          # 동/읍
    addr3 = scrapy.Field()          # 리
    court = scrapy.Field()          # 관할 의성지원
    courtCode = scrapy.Field()      # 관할 F3    
    itemNo = scrapy.Field()         # 물건 번호
    remark = scrapy.Field()         # 경매물건 비고
    caNo = scrapy.Field()           # 경매번호 2017타경234
    pyeong = scrapy.Field()         # 경매 평수
    land1 = scrapy.Field()          # 경매 토지 m2
    land2 = scrapy.Field()          # 경매 토지 평수
    floor1 = scrapy.Field()         # 경매 건물 m2
    floor2 = scrapy.Field()         # 경매 건물 평수
    auctionInfo = scrapy.Field()    # 경매 물건 정보
    itemType = scrapy.Field()       # 경매타입 아파트
    appraisedValue = scrapy.Field() # 감정가       
    minValue = scrapy.Field()       # 최저가
    saleValue = scrapy.Field()      # 매각가
    saleRate = scrapy.Field()       # 매각률
    saleCount = scrapy.Field()      # 응찰자
    