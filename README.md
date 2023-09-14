# IPA過去問ダウンロード

## IPA試験の過去問集めるの面倒ですよね。
過去問道場経由でIPAの過去問をダウンロードします。

DBの過去問をダウンロードしますが、URLを変えると他の科目でも大丈夫です。。

## 準備
### 1.ローカルにipa_testを保存

### 2.ライブラリインストール

```
pip install scrapy
```

### 3.ディレクトリ移動
```
cd ipa_test/ipa_test
```

### 4.起動

```
scrapy crawl　ipa_get
```

### 5.完了
downloadフォルダが作成されpdfファイルがDLされます。

以下を参考に欲しい科目の過去問道場のURLに変更してください。

## URL変更箇所
### ipa_get.py
過去問道場のURLです。
```
allowed_domains = ['www.db-siken.com'] #科目のURL
BASE_URL = 'https://www.db-siken.com' #科目のURL
```
