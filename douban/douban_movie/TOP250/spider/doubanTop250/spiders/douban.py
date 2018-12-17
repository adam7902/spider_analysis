# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from doubanTop250.items import Doubantop250Item


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        item = Doubantop250Item()
        lis = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in lis:
            # 排名
            rank = li.xpath('./div/div[1]/em/text()').extract()
            # 电影名称
            title = li.xpath('./div/div[2]/div[1]/a/span/text()').extract()
            # 电影链接
            link = li.xpath('./div/div[2]/div[1]/a/@href').extract()
            # 电影信息
            # info = li.xpath('./div/div[2]/div[2]/p[1]/text()').extract().strip()
            # 导演演员信息
            director_actor = li.xpath('./div/div[2]/div[2]/p[1]/text()[1]').extract()[0].strip()
            director = director_actor.split('\xa0\xa0\xa0')[0].strip()[3:].strip()
            # 演员
            if len(director_actor.split('\xa0\xa0\xa0')) == 2:
                actor = director_actor.split('\xa0\xa0\xa0')[1].strip()[3:].strip()
            else:
                actor = None
            # actor = director_actor.split('\xa0\xa0\xa0')[1].strip()[3:].strip()
            # 年代国家类型
            info_2 = li.xpath('./div/div[2]/div[2]/p[1]/text()[2]').extract()[0].strip()
            year = info_2.split('/')[0]
            # 国家
            country = info_2.split('/')[1]
            # 类型
            typ = info_2.split('/')[2]
            # 海报
            image_link = li.xpath('./div/div[1]/a/img/@src').extract()
            # 评分
            score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract()
            # 评论人数
            people = li.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract()
            # 评论
            words = li.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract()
            if len(words) != 0:
                words = words[0]
            else:
                words = None
            # words = li.xpath('./div/div[2]/div[2]/p[2]/span/text()')

            item['rank'] = rank
            item['title'] = title
            item['link'] = link
            # item['info'] = info
            item['director'] = director
            item['actor'] = actor
            item['year'] = year
            item['country'] = country
            item['typ'] = typ
            item['image_link'] = image_link
            item['score'] = score
            item['people'] = people
            item['words'] = words

            yield item

        # 翻页
        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        # # 翻页
        # next_page = response.xpath('//span[@class="next"]/a/@href')
        # if next_page:
        #     url = response.urljoin(next_page[0].extract())
        #     yield scrapy.Request(url, self.parse)


# scrapy crawl douban -o douban.csv
# scrapy crawl douban -o douban.json