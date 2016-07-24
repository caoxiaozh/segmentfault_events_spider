# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from scrapy.loader import ItemLoader


class SegmentfaultEventsPipeline(object):

    def process_item(self, item, spider):
        try:
            connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          db='blog',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cur:
                date = item['date'].split('：')[1][0:-3]
                week = item['date'].split('：')[1][-2:]
                city = item['city'].split('：')[1]
                sql = 'insert into `segmentfault_events` ' \
                      '(`name`,`c_date`,`week`,`city`,`icon`,`status`,`detail`,`join_link`,`link`) ' \
                      'values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

                cur.execute(sql,(item['name'],date,week,city,item['icon'],item['status'],
                                  item['detail'],item['join_link'],item['link']))

                connection.commit()
        finally:
            connection.close()
        return item
