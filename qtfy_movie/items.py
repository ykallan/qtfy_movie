# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QtfyMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    title = scrapy.Field()
    typer = scrapy.Field()
    movie_release_time = scrapy.Field()
    release_time = scrapy.Field()
    thunder = scrapy.Field()
    link_name = scrapy.Field()
