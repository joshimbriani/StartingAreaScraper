# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from hcscraper.items import HcscraperItem

class StrikezoneSpider(CrawlSpider):
    name = "strikezone"
    allowed_domains = ["shop.strikezoneonline.com"]
    start_urls = ['http://shop.strikezoneonline.com/Category/2099_Collectors_Set.html']

    rules = (
		Rule(LinkExtractor(allow=('http:\/\/shop\.strikezoneonline\.com\/Category\/\w+.html'), deny=('http:\/\/shop\.strikezoneonline.com\/Category\/Games\.html')), callback='parse_item', follow=True),
	)

    def parse_item(self, response):
	    products = response.css('tr[class^="ItemTableRow"]')
	    group = []
	    for product in products:
		    hc = HcscraperItem()
		    hc["name"] = product.css('td:nth-child(1) a::text').extract()[0] + ' - ' +  product.css('td:nth-child(2)::text').extract()[0].strip(' \r\n\t')
		    hc["price"] = product.css('span[name="ItemPrice"]::text').extract()[0]
		    hc["source"] = "SZ"
		    group.append(hc)
	    return group
