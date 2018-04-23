# -*- coding: utf-8 -*-

import requests
import json

from scrapy.conf import settings
from scrapy.exceptions import DropItem

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class FlumeHttpPipeline(object):
    def __init__(self, flume_url):
        self.flume_url = flume_url
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            flume_url=settings.get('FLUME_URL', 'http://localhost:81')
        )

    def open_spider(self, spider):
        pass
    
    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        #spider.log("process_item called..")
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = json.dumps([{
            "headers" : {},
            "body" : json.dumps(dict(item),ensure_ascii=False)
            }])
        
        req = requests.post(self.flume_url, headers = headers, data=data)
        if req.status_code == 200:
            return item
        else:
            raise DropItem("Failed to post item %s" % data)
        
