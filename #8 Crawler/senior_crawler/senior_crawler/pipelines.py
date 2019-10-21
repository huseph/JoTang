# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class SeniorCrawlerPipeline(object):
    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table
        
    def process_item(self, item, spider):
        return item
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file = crawler.settings.get('SQLITE_FILE'), # 从 settings.py 提取
            sqlite_table = crawler.settings.get('SQLITE_TABLE', 'items')
        )
    
    def open_spider(self, spider):
        try:
            self.conn = sqlite3.connect(self.sqlite_file)
            self.cur = self.conn.cursor()
            self.cur.execute('create table news(title,time,department,content)')
        except Exception as e:
            print(e)   
            print("数据库建立联接异常\n")
        
        
    def process_item(self, item, spider):

        insert_sql = 'insert into news(title,time,department,content) values("{0}","{1}","{2}","{3}")'.format(item['title'],item['time'],item['department'],item['content'])

        print("items = ",item)
        try:
            self.cur.execute(insert_sql)
            self.conn.commit()
        except Exception as e:
            print(e)   
            print("Error, faile to insert sql = ",insert_sql)
        
        return item 
        
        
    def close_spider(self, spider):
        self.conn.close()
 