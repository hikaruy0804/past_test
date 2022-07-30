import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ipa_test.items import CrawldownloadItem
import logging

class IpaGetSpider(scrapy.Spider):
    name = 'ipa_get'
    allowed_domains = ['www.db-siken.com']
    start_urls = ['https://www.db-siken.com']

    def parse(self, response):
        o_url = 'https://www.db-siken.com'
        #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        pre_urls = response.xpath('//ul[@id="testMenu"]/li/a')
        #print(pre_urls)
        for pre_url in pre_urls:
            test_url = o_url + pre_url.xpath('./@href').get()
            print(test_url)
            if test_url != pre_url:
                yield response.follow(url=test_url, callback=self.parse_item)
                
    def parse_item(self, response):
        #print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        for data in response.xpath('//td/i[@class="pdf"]'):
            print(data)
            item = CrawldownloadItem()
            item['title'] = response.xpath('//div[@class="pan"]/b/text()').get() + data.xpath('./following-sibling::a/text()').get()
            item['file_urls'] = [ data.xpath('./following-sibling::a/@href').get() ]
            #item['files'] = data.xpath('./following-sibling::a/@href').get()
            yield item