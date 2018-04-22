# -*- coding: utf-8 -*-

import json 
from urllib.parse import urlencode
from urllib import parse
import datetime, time

import scrapy
from scrapy.conf import settings

from crawler.items import CrawlerItem

class CaucaYearSpider(scrapy.Spider):
    name = 'cauca_day'
    
    base_url = "http://100dream.net:8888/api/courtauction"

    def create_url(self, query_string):
        return self.base_url + '?' + urlencode(query_string)

    def start_requests(self):
        start = settings.get('START', datetime.date.today().strftime('%Y-%m-%d'))
        end = settings.get('END', datetime.date.today().strftime('%Y-%m-%d'))
        
        self.logger.info("START:{} - END:{}".format(start, end))

        #for year in range(2013,2019):
        q = {'itemType':'아파트',
            'auctionStartDate':start,
            'auctionEndDate':end,
            'pageSize':100,
            'page':1 }
        url = self.create_url(q)
        yield scrapy.Request(url, self.parse_data)

    def parse_data(self, response):
        j = json.loads(response.text)

        if len(j['result']) > 0:
            for jo in j['result']:
                item = CrawlerItem()
                item['status'] =jo['status']
                item['auctionDate'] = jo['auctionDate']
                item['auctionInfo'] = jo['auctionInfo'] 
                item['addr0'] = jo['addr0'] 
                item['addr2'] = jo['addr2'] 
                item['court'] = jo['court'] 
                item['addr1'] = jo['addr1'] 
                item['itemNo'] = jo['itemNo']  
                item['regDate'] = jo['regDate'] 
                item['caDesc'] = jo['caDesc'] 
                item['addrInfo'] = jo['addrInfo'] 
                item['caNo'] = jo['caNo'] 
                item['auctionTel'] = jo['auctionTel'] 
                item['itemType'] = jo['itemType'] 
                item['valueMin'] = jo['valueMin'] 
                item['updDate'] = jo['updDate'] 
                item['id'] = jo['id'] 
                item['addr'] = jo['addr'] 
                item['value'] = jo['value']  
                item['auctionLoc'] = jo['auctionLoc'] 
                item['remarks'] = jo['remarks']

                yield item
            
            q = dict(parse.parse_qsl(parse.urlsplit(response.url).query))
            q['page'] = int(q['page'])+1
            url = self.create_url(q)

            yield scrapy.Request(url, self.parse_data)
            
        else:
            self.logger.info('================= end ==================')

