# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JdbookPipeline:
    def __init__(self):
        self.file = open('jd-book.text', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(str(item) + '\n')
        print(item['book_name'], '爬取成功!!!')
        return item

    def close_spider(self, spider):
        print('爬虫运行结束!!!')
        self.file.close()
