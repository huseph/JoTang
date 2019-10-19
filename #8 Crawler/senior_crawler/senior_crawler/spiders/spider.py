import scrapy
from ..items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['ss.uestc.edu.cn']
    start_urls = ['http://www.ss.uestc.edu.cn/noticesList.do?type=93&page=1','http://www.ss.uestc.edu.cn/noticesList.do?type=90&page=1']
    
    def parse(self, response):
        counter = 0
        #page = 1
        for line in response.xpath('//ul[@class="new-list clearfix"]/li'):
            counter += 1
            URL = 'http://www.ss.uestc.edu.cn/' + line.xpath('.//a/@href').extract()[0]
            yield scrapy.Request(URL, callback = self.parse2)
        if (counter == 20) :#显然总数是够200的，所以就这样随便搞搞了，要不然还要加特判和报错，不过出题设计是200，并且确实也够200，就不管了
            lasturl = response.url
            pageSpot = lasturl.rfind('page=')
            page_num = lasturl[pageSpot+5:]
            page_num = int(page_num)+1
            nexturl = lasturl[:pageSpot+5]+str(page_num)
            #page += 1
            #print("我翻页啦！！！", nexturl,lasturl)
            if (page_num <= 10):
                yield scrapy.Request(url=nexturl, callback = self.parse)
            
        
    def parse2(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//div[@class="headline"]/h3/text()').extract()[0].replace('"','')
        item['time'] = response.xpath('//div[@class="blog"]/span[1]/text()').extract()[0]
        item['department'] = response.xpath('//div[@class="blog"]/span[2]/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="text"]').xpath('string(.)').extract()[0].replace('<p>','').replace('</p>','\n').replace('<br>','').replace('\xa0',' ').replace('"','”')      #花里胡哨，为了省掉循环拼接<p>标签中文字哈哈哈
        yield item
            