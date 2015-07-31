# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class IsaacItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class ISAAC_course(Item):
   crn = Field()
   ctype = Field()
   code = Field()
   rseat = Field()
   sTime = Field()
   eTime = Field()



