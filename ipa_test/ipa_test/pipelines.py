from scrapy.pipelines.files import FilesPipeline
import os
import re

class CrawldownloadPipeline(FilesPipeline):
    def file_path(self, request,response=None, info=None):

        unwanted_pattern = r'shiken/mondai-kaiotu/[a-z0-9\-]+-att/'
        cleaned_path = re.sub(unwanted_pattern, '', request.url) # 不要な部分を置き換え
        path_parts = cleaned_path.split("/")
        return os.path.join(*path_parts[2:]) # 最初の2つの部分（https: と ドメイン名）をスキップして結合
