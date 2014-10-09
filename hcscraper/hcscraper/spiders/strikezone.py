# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from hcscraper.items import HcscraperItem

class StrikezoneSpider(CrawlSpider):
    name = "strikezone"
    allowed_domains = ["shop.strikezoneonline.com/"]
    start_urls = (
        #'http://www.shop.strikezoneonline.com/Category/Hero_Clix_Singles.html/',
	'http://shop.strikezoneonline.com/Category/2099_Collectors_Set.html',
    )

    def parse(self, response):
	    products = response.css('tr[class^="ItemTableRow"]')
	    group = []
	    for product in products:
		    hc = HcscraperItem()
		    self.log(product.css('td:nth-child(1) a::text').extract())
		    hc["name"] = [product.css('td:nth-child(1) a::text').extract()[0] + ' - ' +  product.css('td:nth-child(2)::text').extract()[0].strip(' \r\n\t')]
		    hc["price"] = product.css('span[name="ItemPrice"]::text').extract()
		    group.append(hc)
	    return group
