import book
import scrapy
import string

from scrapy.loader import ItemLoader
from scrapy.item import Item, Field
#from book.items import BookItem

class TableItem(Item):
    row = Field()

class BookSpider(scrapy.Spider):
    name = 'book'

    '''
    custom_settings = {
        'FEED_EXPORT_FIELDS': [
            'author',
            'title',
            'language',
            'subject',
            'category',
            'ebookNo',
            'releaseDate',
            'copyrightStatus',
            'downloadNum',
            'price'
        ]
    }
    '''

    def start_requests(self):

        baseUrl = 'https://www.gutenberg.org/ebooks/bookshelf/'

        prodResponse = scrapy.Request(baseUrl, callback = self.parse)

        yield prodResponse

    def parse(self, response):

        for row in response.css('div.bookshelf_pages > ul > li'):
            shelfUrl = row.css('a::attr(href)').get()
            yield response.follow(shelfUrl, self.parseShelf)           


    def parseShelf(self, response):        
        for row in response.css('li.booklink'):
            bookUrl = row.css('a::attr(href)').get()

            yield response.follow(bookUrl, self.parseBook)
                
        for nav in response.css('div.padded > span.links'):
            if ((nav.css('a::text').get() == 'Next')):                                      
                yield response.follow(nav.css('a::attr(href)').get(), self.parseShelf)        


    def parseBook(self, response):
        item = TableItem()

        tempDict = dict()

        for row in response.xpath('//table[@class="bibrec"]//tr'):
            #print(row.css('td > a::text').get())
            
            if (row.css('td > a::text').get()):
                tempDict[row.xpath('th//text()').get()] = row.css('td > a::text').get()
            else:
                tempDict[row.xpath('th//text()').get()] = row.xpath('td//text()').get()                    
            
            item['row'] = tempDict

        return item