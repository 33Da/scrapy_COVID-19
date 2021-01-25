import scrapy
import time
import json
from ..items import *
import datetime


class ChinaCitysSpider(scrapy.Spider):
    name = 'china_citys_spider'
    allowed_domains = ['view.inews.qq.com']
    start_urls = ['https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5']

    def parse(self, response):
        yiqing_json = json.loads(response.text)
        yiqing_json = json.loads(yiqing_json["data"])
        update = yiqing_json["lastUpdateTime"]

        data = yiqing_json["areaTree"][0]["children"]

        for city in data:
            province = city["name"]

            for child in city["children"]:

                yiqing_item = ChinaCityItem()
                yiqing_item["date"] = update
                yiqing_item["province"] = province
                yiqing_item["name"] = child["name"]
                yiqing_item["nowConfirm"] = child["total"]["nowConfirm"]
                yiqing_item["dead"] = child["total"]["dead"]
                yiqing_item["confirm"] = child["total"]["confirm"]
                yiqing_item["suspect"] = child["total"]["suspect"]
                yiqing_item["heal"] = child["total"]["heal"]

                # 当前时间
                yiqing_item["crawl_date"] = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())


                yield yiqing_item







