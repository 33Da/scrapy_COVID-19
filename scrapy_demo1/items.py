# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorldItem(scrapy.Item):
    #
    # 名称
    name = scrapy.Field()
    # 日期
    crawl_date = scrapy.Field()
    # 哪个州
    continent = scrapy.Field()
    # 更新日期
    date = scrapy.Field()
    # 今日新增
    confirmAdd = scrapy.Field()
    # 现有确认
    nowConfirm = scrapy.Field()
    # 疑似
    suspect = scrapy.Field()
    # 死亡
    dead = scrapy.Field()
    # 治愈
    heal = scrapy.Field()

class ChinaProvinceItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 爬取日期
    crawl_date = scrapy.Field()
    # 疑似病例
    suspect = scrapy.Field()

    # 现有确认
    confirm = scrapy.Field()

    # 死亡
    dead = scrapy.Field()
    # 治愈
    heal = scrapy.Field()
    # 更新日期
    date = scrapy.Field()


class ChinaCityItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 爬取日期
    crawl_date = scrapy.Field()

    # 现有确认
    nowConfirm = scrapy.Field()

    # 一共确认
    confirm = scrapy.Field()

    # 怀疑
    suspect = scrapy.Field()

    # 死亡
    dead = scrapy.Field()
    # 治愈
    heal = scrapy.Field()

    province = scrapy.Field()

    # 更新日期
    date = scrapy.Field()







