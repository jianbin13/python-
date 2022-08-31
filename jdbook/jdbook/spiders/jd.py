import scrapy
import json
from copy import deepcopy
from ..items import JdbookItem
from scrapy_redis.spiders import RedisSpider


class JdSpider(RedisSpider):
    name = 'jd'
    # allowed_domains = ['jd.com']
    # start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort']
    redis_key = 'jdbook'

    def parse(self, response, **kwargs):
        json_data = json.loads(response.text)
        data_list = json_data['data']
        for data in data_list:
            item = JdbookItem()
            goryId = int(data['fatherCategoryId'])
            tegoryId = int(data['categoryId'])
            item['classify'] = data['categoryName']
            sonList = data['sonList']
            for son in sonList:
                item['categoryName'] = son['categoryName']
                categoryId = int(son['categoryId'])
                link = 'https://list.jd.com/list.html?cat={},{},{}'.format(goryId, tegoryId, categoryId)
                yield scrapy.Request(url=link, callback=self.parse_detail, meta={'item': deepcopy(item)})

    def parse_detail(self, response):
        item = response.meta['item']
        li_list = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for li in li_list:
            item['book_name'] = li.xpath('./div[@class="gl-i-wrap"]/div[3]/a/em/text()').extract_first()
            item['price'] = li.xpath('./div[@class="gl-i-wrap"]/div[2]/strong/i/text()').extract_first()
            item['shopname'] = li.xpath('./div[@class="gl-i-wrap"]/div[6]/a/text()').extract_first()
            yield item

