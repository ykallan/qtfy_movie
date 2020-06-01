# -*- coding: utf-8 -*-
import scrapy
from ..items import QtfyMovieItem


class QtSpider(scrapy.Spider):
    name = 'qt'
    allowed_domains = ['qtfy6.com']
    start_urls = ['http://www.qtfy6.com/vod-type-1-1.html']
    base_url = 'http://www.qtfy6.com'

    def parse(self, response):
        titles = response.xpath('//div[@class="l"]/h2/a/text()').extract()
        urls = response.xpath('//div[@class="l"]/h2/a/@href').extract()
        for title, url in zip(titles, urls):
            meta = {
                'title': title
            }

            yield scrapy.Request(url=self.base_url+url, callback=self.parse_detail, meta=meta)

        next_url = response.xpath('//a[@class="pagelink_a"][last()-1]/@href').extract_first()
        yield scrapy.Request(url=self.base_url+next_url, callback=self.parse)

    def parse_detail(self, response):
        title = response.meta['title']
        types = response.xpath('//address[@class="msccaddress "]/a/text()').extract()
        typer = ' '.join(types)
        release_time = response.xpath('//address[@class="msccaddress "]/time/text()').extract_first()
        movie_release_time = title[:4]

        thunders = response.xpath('//strong[@class="down_part_name"]/a/@href').extract()
        names = response.xpath('//strong[@class="down_part_name"]/a/@title').extract()
        for link_name, thunder in zip(names, thunders):
            # print(link_name, thunder)
            item = QtfyMovieItem()

            item['title'] = title
            item['typer'] = typer
            item['movie_release_time'] = movie_release_time
            item['release_time'] = release_time
            item['thunder'] = thunder
            item['link_name'] = link_name

            yield item
