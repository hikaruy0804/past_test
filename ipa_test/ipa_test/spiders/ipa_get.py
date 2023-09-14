import scrapy
from ipa_test.items import CrawldownloadItem
import logging

class IpaGetSpider(scrapy.Spider):
    name = 'ipa_get'
    allowed_domains = ['www.sc-siken.com'] #科目のURL
    BASE_URL = 'https://www.sc-siken.com' #科目のURL
    start_urls = [BASE_URL]

    def parse(self, response):
        pre_urls = response.xpath('//ul[@id="testMenu"]/li/a')
        for pre_url in pre_urls:
            test_url = self.BASE_URL + pre_url.xpath('./@href').get()
            logging.debug(f"Testing URL: {test_url}")
            
            if test_url != pre_url:
                yield response.follow(url=test_url, callback=self.parse_item)
                
    def parse_item(self, response):
        title_part1 = response.xpath('//div[@class="pan"]/b/text()').get() or ""
        data_list = response.xpath('//td/i[@class="pdf"]')
        for data in data_list:
            item = CrawldownloadItem()
            title_part2 = data.xpath('./following-sibling::a/text()').get() or ""
            item['title'] = title_part1 + title_part2
            pdf_url = response.urljoin(data.xpath('./following-sibling::a/@href').get())
            item['file_urls'] = [pdf_url]
            yield item
