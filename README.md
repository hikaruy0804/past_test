# past_test

#### IPAの試験の過去問集めるの大変ですね。

面倒くさいことはプログラムに任せましょう。

過去問道場経由でダウンロードします。

DBに申込んだのでDBの過去問を取得しますが、URLを変えると他の科目でも大丈夫だと思います。

#### 起動

```
scrapy crawl　[project名]
```

#### 変更箇所
##### ipa_get.py
```
allowed_domains = ['www.db-siken.com']
start_urls = ['https://www.db-siken.com']
o_url = 'https://www.db-siken.com'
```
