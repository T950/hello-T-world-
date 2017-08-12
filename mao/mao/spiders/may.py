# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.http import Request
from mao.items import MaoItem

class MaySpider(scrapy.Spider):
    name = 'may'
    allowed_domains = ['maoyan.com']
    start_urls = 'http://maoyan.com/board/4/'


    def start_requests(self):
        yield Request(url=self.start_urls,callback=self.parse)

    def parse(self, response):
        # print(response.text)
        for i in range(0,10):
            url = self.start_urls+'?offset='+str(i*10)
            # print(url)
            yield Request(url=url,callback=self.parse_page)
    def parse_page(self,response):
        demo=re.compile('<img data-src="(.*?)".*?/>.*?<a .*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i>.*?<i class="fraction">(.*?)</i>',re.S)
        lists=demo.findall(response.text)
        for a,b,c,d,e,f in lists:
            item=MaoItem()
            item['title']=b
            item['name']=c.strip()
            item['time']=d
            item['score']=e+f
            item['img']=a
            yield item