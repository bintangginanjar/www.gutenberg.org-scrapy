# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst, Join

class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()    
    author = Field()
    title = Field()
    language = Field()
    subject = Field()
    category = Field()
    ebookNo = Field()
    releaseDate = Field()
    copyrightStatus = Field()
    downloadNum = Field()
    price = Field()
    
    pass
