from scrapy import cmdline
cmdline.execute("scrapy crawl douban -o top250.csv -t csv".split())
