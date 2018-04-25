# -*- coding: utf-8 -*-

import datetime, time

import json 
import re
from urllib.parse import urlencode
from urllib import parse

import logging
import scrapy
from scrapy.selector import Selector
from scrapy.utils.response import open_in_browser
from scrapy.utils.markup import remove_tags

from scrapy.conf import settings
from crawler.items import AuctionItem

class HouseinfoSpider(scrapy.Spider):
    name = 'houseinfo'
    
    bubwon = {'A01':'서울중앙지방법원',
        'A02':'서울동부지방법원',
        'A03':'서울서버지방법원',
        'A04':'서울남부지방법원',
        'A05':'서울북부지방법원',
        'D01':'의정부지방법원',
        'D02':'고양지원',
        'C01':'인천지방법원',
        'C02':'부천지원',
        'E01':'수원지방법원',
        'E02':'성남지원',
        'E03':'여주지원',
        'E04':'평택지원',
        'E05':'안산지원',
        'E06':'안양지원',
        'F01':'춘천지방법원',
        'F02':'강릉지원',
        'F04':'원주지원',
        'F03':'속초지원',
        'F05':'영월지원',
        'G01':'청주지방법원',
        'G02':'충주지원',
        'G03':'제천지원',
        'G04':'영동지원',
        'H01':'대전지방법원',
        'H05':'홍성지원',
        'H06':'논산지원',
        'H02':'천안지원',
        'H03':'공주지원',
        'H04':'서산지원',
        'I01':'대구지방법원',
        'I05':'안동지원',
        'I02':'경주지원',
        'I03':'김천지원',
        'I04':'상주지원',
        'I07':'의성지원',
        'I06':'영덕지원',
        'I08':'포항지원',
        'I09':'대구서부지원',
        'B01':'부산지방법원',
        'B02':'부산동부지원',
        'B03':'부산서부지원',
        'N01':'울산지방법원',
        'J01':'창원지방법원',
        'J06':'마산지원',
        'J04':'진주지원',
        'J05':'통영지원',
        'J03':'밀양지원',
        'J02':'거창지원',
        'L01':'광주지방법원',
        'L03':'목포지원',
        'L04':'장흥지원',
        'L02':'순천지원',
        'L05':'해남지원',
        'K01':'전주지방법원',
        'K02':'군산지원',
        'K04':'정읍지원',
        'K03':'남원지원',
        'M01':'제주지방법원'}
   
    date_fmt = '%Y-%m-%d'
    base_url = "http://www.houseinfo.co.kr/sub.html"

    def create_url(self, query_string):
        return self.base_url + '?' + urlencode(query_string)
    
    def start_requests(self):
        start = datetime.datetime.strptime(settings.get('START', datetime.date.today().strftime(self.date_fmt)), self.date_fmt).date()
        end = datetime.datetime.strptime(settings.get('END', datetime.date.today().strftime(self.date_fmt)), self.date_fmt).date()

        if start > end:
            self.logger.error("시작날짜(%s)가 종료날짜(%s) 보다 큽니다." % (start.strftime(self.date_fmt), end.strftime(self.date_fmt)))
            return

        current = start
        while current <= end:
            q = {"menu":"9",
                "i_mode":"search",
                "i_zipetc":"",
                "i_bub_cd1":"X",
                "i_bub_cd2":"",
                "region_code1":"",
                "region_code2":"",
                "region_code3":"",
                "i_selday1":current.strftime(self.date_fmt),
                "i_selday2":current.strftime(self.date_fmt),
                "i_money_value1":"",
                "i_money_value2":"",
                "auction_result":"0",
                "i_sort":"3", # 오름차순
                "i_sort2":"0",
                "i_tuksu":"",
                "i_yu_cnt1":"0",
                "i_yu_cnt2":"999",
                "i_area_value1":"",
                "i_area_value2":"",
                "p_usagecode01[]":"01",
                "pageList":"1000",
                "page":"1"}
                    
            current = current + datetime.timedelta(days=1)
           
            yield scrapy.Request(self.create_url(q), callback=self.parse_data, meta={'q': q})
        

    def parse_data(self, response):
        #try:
            # 헤더 삭제
            qs = response.meta['q']
            self.logger.info("current {} - {}".format(qs['i_selday1'],qs['i_selday2']))
            trs = response.xpath('//div[@class="search_list"]//tr')[1:] 
            if len(trs) > 0:
                #open_in_browser(response)
                #self.logger.info("q = %s" % str(response.meta['q']))
                for tr in trs:
                    td = tr.xpath('.//td')
                    
                    if len(td) <= 1:
                        self.logger.info("blank")
                        return
                    
                    td2 = td[2].xpath(".//@onclick").extract_first()
                    #self.logger.debug(re.findall("jf_listopen\('(\S+)','(\d+)','(\d+)','(\d+)',(\d+)\)",td2))
                    tmp = re.findall("jf_listopen\('(\S+)','(\d+)','(\d+)','(\d+)',(\d+)\)",td2)
                    courtCode, t2, t3, itemNo, t5 = tmp[0] if len(tmp) > 0 else ('','','','','') # ('A02', '2017', '4106', '1', '1825')
                    if len(courtCode) == 0:
                        continue
                    
                    caNo = "{}타경{}".format(t2,t3)
                    itemType = remove_tags(td[2].extract()).split(")")[-1] # 아파트
                    court = self.bubwon[courtCode]

                    addr = re.sub('^\s+\[|\]|^\s','',td[3].xpath('.//text()').extract_first())
                    addr0, addr1, addr2, addr3 = addr.split(' ')[:4]
                    if not addr3.endswith('리'):
                        addr3 = ''

                    appraisedValue = minValue = saleValue = saleRate= saleCount = ''
                    
                    tmp = td[3].xpath('.//font[@color="1154FD"]//text()').extract() # 감정가
                    appraisedValue = tmp[0].replace('￦','').replace(',','') if len(tmp) > 0 else ''
                   

                    tmp = td[3].xpath('.//font[@color="FD1414"]//text()').extract() # 최저가
                    minValue = tmp[0].replace('￦','').replace(',','') if len(tmp) > 0 else ''

                    tmpstr = ''.join(td[3].xpath('.//font[@color="000000"]//text()').extract())
                    tmp = re.findall('\w+:￦(\S+)\((\d+)%\)\w+\:(\d+)\S*',tmpstr)
                    saleValue, saleRate, saleCount = tmp[0] if len(tmp) > 0 else ('','','') # [('215,688,000', '94', '5')]
                    saleValue = saleValue.replace(',','')
                    
                    land1 = land2 = floor1 = floor2 = pyeong = ''
                    infos = list(map(lambda x: re.sub('\[|\]','',x),td[3].xpath('.//font[@color="00479F"]//text()').extract())) 
                    self.logger.debug(infos)
                    for item in infos:
                        if item.startswith('토'):
                            v1 = re.findall('\d+\.\d+|\d+',item)
                            land1, land2 = v1 if len(v1) > 0 else ('','')
                        if item.startswith('건'):
                            v1 = re.findall('\d+\.\d+|\d+',item)
                            floor1, floor2 = v1 if len(v1) > 0 else ('','')
                        else:
                            v1 = re.findall('\d+\.\d+|\d+',item)
                            pyeong = v1[0] if len(v1) > 0 else ''


                    auctionInfo = ','.join(infos)	
                    tmp = list(map(lambda x: re.sub('\[|\]','',x),td[3].xpath('.//font[@color="red"]//text()').extract()))	
                    remark = ','.join(tmp)	
                    

                    td4 = re.sub('\s|\r\n','',remove_tags(td[4].extract()))
                    v4 = re.findall('(\S+)\((\d+)\%\)',td4)
                    auctionDate, progressRate = v4[0] if len(v4) > 0 else ('','')  # [('2018-04-03', '70')]

                    td5 = re.sub('\s|\r\n','',remove_tags(td[5].extract()))
                    v5 = re.findall('(\w+)\((\d+)\S\)',td5)
                    status, count = v5[0] if len(v5) > 0 else ('','') # [('매각', '2')]

                    data = AuctionItem()
                    data['status'] = status                     # 상태 매각
                    data['auctionCount'] = count                # 입찰 회
                    data['auctionDate'] = auctionDate           # 경매일 3014-12-07
                    data['addr'] = addr                         # 전체 주소
                    data['addr0'] = addr0                       # 시/도
                    data['addr1'] = addr1                       # 구/군
                    data['addr2'] = addr2                       # 동/읍
                    data['addr3'] = addr3                       # 리
                    data['court'] = court                       # 관할 의성지원
                    data['courtCode'] = courtCode               # 관할 F3    
                    data['itemNo'] = itemNo                     # 물건 번호
                    data['remark'] = remark                     # 경매물건 비고
                    data['caNo'] = caNo                         # 경매번호 2017타경234
                    data['pyeong'] = pyeong                     # 경매 평수
                    data['land1'] = land1                       # 경매 토지 m2
                    data['land2'] = land2                       # 경매 토지 평수
                    data['floor1'] = floor1                     # 경매 건물 m2
                    data['floor2'] = floor2                     # 경매 건물 평수
                    data['auctionInfo'] = auctionInfo           # 경매 물건 정보 
                    data['itemType'] = itemType                 # 경매타입 아파트
                    data['appraisedValue'] = appraisedValue     # 감정가       
                    data['minValue'] = minValue                 # 최저가
                    data['saleValue'] = saleValue               # 매각가
                    data['saleRate'] = saleRate                 # 매각률
                    data['saleCount'] = saleCount               # 응찰자
                    yield data


                pages = response.xpath('//div[@class="paging"]//a/text()').extract()
                if len(pages)>1:
                    self.logger.info("paging = %s" % str(pages))
                    #open_in_browser(response)

                    last_page = 1
                    if "Next" in pages[-1]:
                        last_page = pages[-2]
                    else:
                        last_page = pages[-1]

                    last_page = int(last_page)

                    q = response.meta['q']
                    page = int(q['page'])

                    if last_page > page:
                        q['page'] = str(page +1)
                        yield scrapy.Request(self.create_url(q), callback=self.parse_data, meta={'q': q})


            else:
                self.logger.info("blank")

            
        #except:
        #    open_in_browser(response)

