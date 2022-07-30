# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

#from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import os

class CrawldownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_paths = request.url.split("/")
        file_paths.pop(0) # https:
        file_paths.pop(0) #//
        file_name = os.path.join(*file_paths)
        pos = file_name.find('2')
        file_name[:pos]
        #print('aaddddddddddddddddddddddddd')
        return file_name