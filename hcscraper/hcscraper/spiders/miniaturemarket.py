# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from hcscraper.items import HcscraperItem

class MiniaturemarketSpider(CrawlSpider):
    name = "miniaturemarket"
    allowed_domains = ["miniaturemarket.com"]
    start_urls = ['http://www.miniaturemarket.com/collectible-miniatures/heroclix.html?p=1']

    rules = (
		    Rule(LinkExtractor(allow=('http:\/\/www\.miniaturemarket\.com\/collectible-miniatures\/heroclix\.html\?p=\d+')), callback='parse_item', follow=True),
		    )

    def parse_item(self, response):
	products = response.css('.products-grid .item')
	group = []
	for product in products:
		hc = HcscraperItem()
		hc["name"] = product.css('.product-name a::text').extract()
		if len(product.css('.price-box .regular-price .price::text').extract()) > 0:
			hc["price"] = [product.css('.price-box .regular-price .price::text').extract()[0][1:]]
		else:
			hc["price"] = [product.css('.price-box .special-price .price::text').extract()[0].strip(' \r\n')]
		group.append(hc)
	return group
