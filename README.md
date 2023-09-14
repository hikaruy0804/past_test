# past_test


## IPA試験の過去問集めるの大変ですね。
面倒くさいことはプログラムに任せましょう。
過去問道場経由でダウンロードします。
DBの過去問をダウンロードしますが、URLを変えると他の科目でも大丈夫だと思います。

## 準備
### ローカルにipa_testを保存

### ライブラリインストール

```
pip install scrapy
```

### 起動

### 起動

```
scrapy crawl　[project名]
```

## 変更箇所
### ipa_get.py
```
allowed_domains = ['www.db-siken.com']
start_urls = ['https://www.db-siken.com']
o_url = 'https://www.db-siken.com'
```
