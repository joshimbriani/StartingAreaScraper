# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from hcscraper.items import HcscraperItem


class TandtSpider(CrawlSpider):
    name = "tandt"
    allowed_domains = ["trollandtoad.com"]
    start_urls = (
	'http://www.trollandtoad.com/Heroclix/1177.html',
    )

    rules = (
		Rule(LinkExtractor(allow=('http:\/\/www\.trollandtoad\.com\/Heroclix\/\w+.html')), callback='parse_item', follow=True),
		    )

    def parse_item(self, response):
        products = response.css('.cat_result_wrapper')
	group = []
	for product in products:
		hc = HcscraperItem()
		hc["name"] = product.css('.cat_result_text h2 a::text').extract()
		hc["price"] = [product.css('.price_text::text')[0].extract()]
		group.append(hc)
	return group
