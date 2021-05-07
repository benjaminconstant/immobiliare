# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class HouseItem(Item):
    uid = Field()
    search = Field()
    title = Field()
    link = Field()
    state = Field()
    price = Field()
    price_mq = Field()
    mq = Field()
    text = Field()
    costs = Field()
    date_publish = Field()
