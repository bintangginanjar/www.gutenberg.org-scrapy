import scrapy
import string

from scrapy.loader import ItemLoader
#from nama.items import NamaItem

class BookSpider(scrapy.Spider):
    name = 'book'

    def start_requests(self):

        baseUrl = 'https://www.gutenberg.org/ebooks/bookshelf/'

        prodResponse = scrapy.Request(baseUrl, callback = self.parse)

        yield prodResponse

    def parse(self, response):
