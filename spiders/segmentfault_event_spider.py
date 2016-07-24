# coding:utf-8
import scrapy
from bs4 import BeautifulSoup

from segmentfault_events.items import SegmentfaultEventsItem
from scrapy.loader import ItemLoader


class SegmentfaultEventSpider(scrapy.Spider):
    name = 'seg_evt_spider'
    start_urls = ['https://segmentfault.com/events']

    def parse(self, response):
        bs_obj = BeautifulSoup(response.body,'html.parser')
        events = bs_obj.find_all(class_='widget-event')
        for event in events:
            item = SegmentfaultEventsItem()
            a = event.a
            img = a.img
            item['name'] = event.div.h2.a.get_text()
            item['detail'] = response.urljoin(event.div.h2.a['href'])
            item['link'] = response.urljoin(a['href'])
            item['icon'] = img['data-original']
            item['join_link'] = response.urljoin(event.div.contents[-2]['href'])
            item['status'] = event.div.contents[-2].get_text()
            item['date'] = event.div.ul.contents[1].get_text()
            item['city'] = event.div.ul.contents[3].get_text()
            yield item
        nextlink = bs_obj.find(rel='next')
        if nextlink:
            yield scrapy.Request(response.urljoin(nextlink['href']), callback=self.parse)
