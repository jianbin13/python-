# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbookItem(scrapy.Item):
    # define the fields for your item here like:
    shopname = scrapy.Field()
    classify = scrapy.Field()
    categoryName = scrapy.Field()
    book_name = scrapy.Field()
    price = scrapy.Field()


