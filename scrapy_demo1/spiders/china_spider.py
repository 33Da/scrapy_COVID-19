import scrapy
import time
import json
from ..items import *
import datetime


class ChinaSpider(scrapy.Spider):
    name = 'China_spider'
    allowed_domains = ['view.inews.qq.com']
    start_urls = ['https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5']

    def parse(self, response):
        yiqing_json = json.loads(response.text)
        yiqing_json = json.loads(yiqing_json["data"])
        update = yiqing_json["lastUpdateTime"]

        data = yiqing_json["areaTree"][0]["children"]

        for city in data:
            yiqing_item = ChinaProvinceItem()
            yiqing_item["name"] = city["name"]
            yiqing_item["date"] = update
            yiqing_item["dead"] = city["total"]["dead"]
            yiqing_item["suspect"] = city["total"]["suspect"]
            yiqing_item["confirm"] = city["total"]["confirm"]
            yiqing_item["heal"] = city["total"]["heal"]

            yiqing_item["crawl_date"] = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())


            yield yiqing_item
